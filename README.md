# Game Cinematic Narrative Director

A public, game-agnostic agent skill for interactive narrative direction, screenplay craft, branching design, production scene contracts, character continuity, suspense, storyboards, sound and engine handoff.

This public package **does not include any game plots or private game projects**. The skill uses the invoking user's project files at runtime if those files are explicitly available; no project source is bundled with the skill.

## Use locally in Codex

Clone this public repository into the user-level Codex skills directory:

```bash
git clone https://github.com/omerycll/game-cinematic-narrative-director.git ~/.codex/skills/game-cinematic-narrative-director
```

Alternatively, copy the directory into `~/.agents/skills/` or the project-local `.agents/skills/` when limiting use to a single project. Restart Codex/open a new session, then ask the assistant to use `game-cinematic-narrative-director` to **audit the current project's narrative read-only before changing any files**.

## Suggested first task

> In this repository, use Game Cinematic Narrative Director. Read only this project's narrative, design and event files. Produce a canon lock, scene/choice graph, weak-point audit, and a non-destructive improvement plan under `docs/narrative-review/`. Keep existing controls and mechanics intact. Do not change code or story files without my approval. Do not publish or upload any content.

## Structural verification

`python scripts/validate_story.py path/to/narrative_graph.json`

The validator checks basic graph and conditional reachability. It cannot verify narrative artistry or actual gameplay duration. It merges repeated scene/state pairs, so reported shortest/longest durations are representative explored routes, not guaranteed global bounds. It detects states with no available transition; it does not prove that every reachable state can eventually reach an ending (for example, a closed cycle may escape detection). Always review cycles and route timing manually.

## Licensing

See `LICENSE.txt` for reuse rights. Example output or generated game-specific story belongs in the invoking project's designated output and is not part of this public skill.
