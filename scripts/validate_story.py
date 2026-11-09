#!/usr/bin/env python3
"""Validate branching narrative scene graphs and enumerate reachable endings.

No external dependencies. Expected JSON: {
  "title": str, "start": str, "initial_state": {flag:int},
  "scenes": [{"id", "title", "act", "minutes", "location", "camera",
              "player_goal", "emotion", "hotspots": [str],
              "on_enter": {"add"?:{k:v}, "set"?:{k:v}},
              "choices": [{"id", "label", "to", "requires"?:{flag:int|{"min":int}},
                           "effects"?: {"add"?:{k:v}, "set"?:{k:v}}}],
              "ending": bool?}]
}
"""
import argparse
import collections
import json
import sys
from pathlib import Path

SCENE_REQUIRED = ("id", "title", "act", "minutes", "location", "camera", "player_goal", "emotion", "hotspots")


def apply_effect(state, effect):
    new = dict(state)
    for k, v in effect.get("set", {}).items():
        new[k] = int(v)
    for k, v in effect.get("add", {}).items():
        new[k] = int(new.get(k, 0)) + int(v)
    return new


def permitted(state, needs):
    for k, v in needs.items():
        n = state.get(k, 0)
        if isinstance(v, dict):
            if "min" in v and n < v["min"]:
                return False
            if "max" in v and n > v["max"]:
                return False
            if "eq" in v and n != v["eq"]:
                return False
        elif n < v:
            return False
    return True


def review(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    errors, warnings = [], []
    nodes = data.get("scenes", [])
    byid = {}
    all_edge_count = 0
    choice_ids = set()
    for s in nodes:
        sid = s.get("id")
        if sid in byid:
            errors.append(f"duplicate scene ID: {sid}")
        byid[sid] = s
        for k in SCENE_REQUIRED:
            if k not in s or s[k] in ("", None, []):
                errors.append(f"scene {sid}: missing {k}")
        if not isinstance(s.get("minutes", 0), (int, float)) or s.get("minutes", 0) <= 0:
            errors.append(f"scene {sid}: duration must be positive")
        if s.get("ending") and s.get("choices"):
            errors.append(f"ending scene {sid} must not have choices")
        if not s.get("ending") and not s.get("choices"):
            errors.append(f"non-ending scene {sid} has no transitions")
        for c in s.get("choices", []):
            all_edge_count += 1
            cid = c.get("id")
            if not cid:
                errors.append(f"scene {sid} has choice without ID")
            if cid in choice_ids:
                errors.append(f"duplicate choice ID: {cid}")
            choice_ids.add(cid)
            if c.get("to") not in {x.get("id") for x in nodes}:
                errors.append(f"scene {sid}: dangling target {c.get('to')}")
            if not c.get("label"):
                errors.append(f"choice {cid}: missing player-facing label")
    if data.get("start") not in byid:
        errors.append("invalid start ID")
    if not any(s.get("ending") for s in nodes):
        errors.append("no endings")
    if errors:
        return {"passed": False, "errors": errors, "warnings": warnings}

    start = data["start"]
    init = dict(data.get("initial_state", {}))
    queue = collections.deque([(start, init, [], [], 0)])
    seen_states = set()
    reached_scenes, reached_choices, endings, blocked = set(), set(), {}, []
    paths_checked = 0
    MAX_STATES = 250000

    while queue:
        sid, state, route, picked, duration = queue.popleft()
        scene = byid[sid]
        state = apply_effect(state, scene.get("on_enter", {}))
        key = (sid, tuple(sorted(state.items())))
        if key in seen_states:
            continue
        seen_states.add(key)
        paths_checked += 1
        if paths_checked > MAX_STATES:
            errors.append("state exploration exceeded 250000; graph might have unbounded loop")
            break
        reached_scenes.add(sid)
        route = route + [sid]
        duration += scene["minutes"]
        if scene.get("ending"):
            record = {"minutes": duration, "route": route, "choices": picked, "final_state": state}
            if sid not in endings:
                endings[sid] = {"min": record, "max": record, "samples": 1}
            else:
                endings[sid]["samples"] += 1
                if record["minutes"] < endings[sid]["min"]["minutes"]:
                    endings[sid]["min"] = record
                if record["minutes"] > endings[sid]["max"]["minutes"]:
                    endings[sid]["max"] = record
            continue
        viable = [c for c in scene["choices"] if permitted(state, c.get("requires", {}))]
        if not viable:
            blocked.append({"scene": sid, "state": state, "route": route})
        for c in viable:
            reached_choices.add(c["id"])
            queue.append((c["to"], apply_effect(state, c.get("effects", {})), route, picked + [c["id"]], duration))

    missing_nodes = sorted(set(byid) - reached_scenes)
    missing_ends = sorted({s["id"] for s in nodes if s.get("ending")} - set(endings))
    missing_choices = sorted(choice_ids - reached_choices)
    if missing_nodes:
        errors.append("unreachable scenes: " + ", ".join(missing_nodes))
    if missing_ends:
        errors.append("unreachable endings: " + ", ".join(missing_ends))
    if missing_choices:
        errors.append("unreachable choice IDs: " + ", ".join(missing_choices))
    if blocked:
        errors.append(f"{len(blocked)} softlock states (first {blocked[0]['scene']})")
    minutes = [item[k]["minutes"] for item in endings.values() for k in ("min", "max")]
    if minutes and min(minutes) < data.get("min_first_run_minutes", 0):
        warnings.append(f"shortest valid route {min(minutes)}m shorter than authored target {data.get('min_first_run_minutes')}m")
    return {
        "passed": not errors,
        "title": data.get("title"),
        "scenes": len(nodes), "edges": all_edge_count, "state_combinations_explored": len(seen_states),
        "reachable_scenes": len(reached_scenes), "reachable_choices": len(reached_choices),
        "ending_routes": {k: {"shortest_minutes": v["min"]["minutes"],
                              "longest_minutes": v["max"]["minutes"],
                              "shortest_route": v["min"]["route"],
                              "example_choices": v["min"]["choices"]} for k, v in sorted(endings.items())},
        "softlock_states": len(blocked), "errors": errors, "warnings": warnings
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("graph")
    p.add_argument("--report", help="Write JSON report here")
    args = p.parse_args()
    result = review(args.graph)
    txt = json.dumps(result, indent=2, ensure_ascii=False)
    print(txt)
    if args.report:
        Path(args.report).write_text(txt + "\n", encoding="utf-8")
    return 0 if result["passed"] else 1

if __name__ == "__main__":
    sys.exit(main())
