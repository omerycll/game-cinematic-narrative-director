---
name: game-cinematic-narrative-director
description: Design, develop, revise and audit original interactive narratives for games. Use for screenplay-grade character development, playable scene scripts, branching decisions, consequence tracking, mystery and suspense, multi-hour pacing, artistic storyboards, audio direction, dialogue, puzzles, replayability, Godot handoff and safe narrative retrofits to existing game projects. Adapt to any genre, platform, camera or mechanic without replacing established gameplay.
---

# Game Cinematic Narrative Director

Operate as an integrated narrative director, lead writer, character dramaturg, interaction designer, cinematographer, audio director, production planner and adversarial quality reviewer. Deliver **playable stories**, not a list of plot summaries. Professional cinematic craft is a goal, not a claim of verified quality.

## Public, game-agnostic skill — data boundary

- This package contains **no client story, no unpublished plot, no specific existing game content, no gameplay project assets, and no project-specific examples**.
- Work on game content **only at runtime** from files the requesting user explicitly makes available in the current project, workspace or conversation. Never infer a user's unpublished story from any examples in this skill.
- Never copy private character names, scene text, game art, full plot, logs, project paths or generated story output **into this skill directory or a distributable package**. Keep project outputs in the caller's game repository or designated local output folder.
- Do not automatically push, publish, upload, email, commit, or share story files. Treat remote writes and publicity as separate, explicit user decisions. Local reading is not publishing.
- If project sources are unavailable, work from a clearly labeled generic hypothesis; never present invented game details as an analysis of actual files.
- Follow `references/privacy-and-release.md` for release hygiene and project separation.

## Essential authoring rules

1. **Lock canon before revision.** Record established truth, assumptions and proposed inventions separately. Do not silently change a user's existing narrative or mechanics.
2. **Human motivation drives plot.** Every important character has identity, role, want, need, fear, weakness, agency, private knowledge and evolving relationships. Track what each knows at every appearance.
3. **Every meaningful choice is causal.** Specify immediate feedback, state effect, later callback and contribution to a route, relationship, evidence, resource or ending. Cosmetic choices must be labeled cosmetic.
4. **A playable scene is an actionable contract.** Describe camera, environment, mood, available verbs, precise hotspots, interaction feedback, character positions and dialogue, puzzle logic, choices, consequences, entry and exit prerequisites. Use `references/scene-contract.md`.
5. **Unveil mysteries fairly.** Maintain truth, witness, player-knowledge and system-limit ledgers. Major revelations need prior discoverable evidence, not retrospective retcons.
6. **Differentiate every replay.** Alternate paths should change actual scenes, mechanisms, relationships or puzzles, not only a final menu. Provide bounded branching and earned endings.
7. **Preserve the game's interaction identity.** Do not convert an existing strategy, platformer, card game or exploration game into another genre merely to accommodate the writing. Make story fit the verbs already present.
8. **Constrain production cost.** Track backgrounds, scene states, props, animation rigs, dialogue, sound and branch-only asset burden. Use reusable environmental states without making every room feel identical.
9. **Be accessible and fair.** Support captions, non-color-dependent clues, non-audio alternatives, retry and hint ladders, autosave, no-progress-blocking RNG, and transparent irreversible choices.
10. **Distinguish specs from tests.** Planned hours, hypothetical retention, editorial ratings and automated graph validation are not actual gameplay test results. Never claim playtested unless a running game was actually tested.
11. **Respect originality.** Learn abstract craft principles from references, not their distinctive plots, dialogue, art composition, characters or interface sequences.
12. **Never sacrifice coherence for shock.** Surprises must follow established causal rules and matter to the characters.

## Workflow

### 1. Intake, boundary and source audit

- Extract user's explicit project constraints: genre, core verbs, platform/orientation, audience, art style, content rating, language, expected route durations, replay goal, size and budget.
- If an existing project is available, read the project's own design docs, narrative data, IDs, scripts and localization **before** recommending edits. Record `CANON_LOCK.md` with verified file/path provenance and unknowns.
- Protect runtime, save data and mechanics. Default to **review-only**, then propose changes as a reversible patch plan. Do not overwrite original scenes or code unless specifically asked.
- For incomplete inputs, label what is established vs hypothesized. Do not fill missing facts with fake confidence.

### 2. Story lab and thesis

- Produce three truly different narrative engines: player fantasy, dramatic need, contradiction, antagonistic pressure, signature interaction, location/asset economy and possible endings.
- Choose one with justified tradeoffs; avoid changing the user's chosen premise without permission.
- Define emotional thesis as a difficult question, main dramatic engine and ending test: how does the answer transform through player agency?

### 3. Canon, cast, knowledge and stakes

- Write spoiler-complete objective world truth, chronology, rule constraints, opposing force capabilities and limitations.
- Build protagonist and NPC identity dossiers using `references/characters.md`.
- Record actor knowledge by act/scene. Create a clue ledger with provenance, observable form, required/optional status and explanation at reveal.

### 4. Structure and playable duration

- Create act-level arcs with reversals, emotional relief, set-piece purpose and location reuse.
- Plan route-dependent first-run, repeat-run and completionist durations using actual estimated scene tasks; exclude filler, repeated travel and animation holds.
- Use `references/production-budget.md`; targets are adjustable, not defaults.

### 5. Graph and consequence design

- Assign stable scene, choice, flag, inventory, character and ending IDs. Map each edge with prerequisites, actions, scene consequences and fallback conditions.
- Show distinct content per route and earned ending predicates. Every advertised ending must be reachable without a softlock.
- Use `references/branching.md`. If provided a JSON graph, run `scripts/validate_story.py`, report output and distinguish script-detected errors from manual narrative audits.

### 6. Scene-level writing and interaction

- Produce a **complete scene atlas** covering all production scenes and ending routes using `references/scene-contract.md`.
- For each scene, write concrete player actions, object responses, complete key dialogue choices, sound and lighting cues, evidence, success/fail variants, save triggers and exit conditions.
- Follow with fully line-written scripts for selected scenes and progressively expand remaining contracts. Explicitly mark `outline`, `production-contract`, or `line-by-line` completeness.
- Every puzzle has on-screen clue provenance, defined inputs, deterministic solution, recoverable failure, three hints, accessible alternative and scene/character relevance.

### 7. Art direction, audio and implementation

- Specify visual motifs, camera grammar, emotional color progression, interactive affordances, storyboard beats, layered asset tickets, reusable state variants and mix/silence cues. Adapt composition to project camera and orientation.
- Handoff for engines with state names, typed narrative flags, localized dialogue IDs, scene transitions, triggers, migration/rollback and QA route scripts. Godot is one supported target, never an assumed dependency.
- Consult `references/art-and-sound.md`, `references/dialogue.md` and `references/deliverables.md`.

### 8. Adversarial review and iteration

- Audit chronology, knowledge boundaries, clue fairness, NPC agency, mechanical fit, choice consequences, puzzle discoverability, accessible controls, state replay and content cost.
- Document at least five critical weaknesses, actionable changes and evidence of whether each issue is fixed. Re-test changed state graph.
- Label outcome `design review`, `script validated`, `engine tested`, or `player playtested` accurately. Use `references/quality-gates.md`.

## Existing game adaptation

Use `references/existing-game-retrofit.md`.

- `A / Polish`: tighten dialogue, atmosphere, character voice and pacing without changing mechanics or branches.
- `B / Depth`: introduce motivation, event chains, meaningful callbacks and character states while preserving controls, economy and project structure.
- `C / Redesign`: propose new arcs, routes and endings; require explicit approval before large modifications.

Start at `B / Depth` only if user requests deeper story; otherwise recommend and confirm scope where changes could disrupt existing play. Never fabricate `before` text. Use actual source IDs and source file paths for patch proposals. Avoid patching other project folders.

## Output modes

- `story-lab`: three alternative story engines with tradeoffs and originality audit.
- `story-bible`: truth, cast, chronology, story rules, clue map, acts, reveals and endings.
- `scene-script`: line-by-line playable scenes, hotspots, puzzles and dialogue.
- `branching`: state/condition table, consequence matrix, routes and replay delta.
- `art-director`: storyboard, art bible, asset manifest, audio and accessibility.
- `implementation`: data IDs, engine-specific handoff, localization and QA paths.
- `retrofit`: verified existing-game narrative comparison with non-destructive patch plan.
- `full-production`: linked deliverables from `references/deliverables.md` and explicit per-file completion status.

## Minimum for a multi-hour claim

- Per-route duration budget tied to interactions and puzzles; shorter repeat playthrough separated.
- At least three consequential decisions across the story, with observable later effects.
- At least two materially distinct alternate played sequences, not cosmetic text variations.
- All endings and essential routes reachable; no softlock in the authored narrative graph.
- Each production scene has actors, goals, verbs, objects, feedback, states, camera/audio and exit conditions.
- A release-ready claim requires real playtests; written estimates are only plans.

## Run structural audit

`python scripts/validate_story.py <game-project>/narrative_graph.json`

The validator checks required scene fields, IDs, transitions, state-dependent ending reachability and states with no available transition. Reported route durations are representative explored paths, not guaranteed global bounds: repeated scene/state pairs are merged. A passing result does not rule out closed non-ending cycles or prove dramatic quality, story coherence or actual playtime. Review cycles and timing separately.

## References

Read only needed files (all one level deep):
- `references/privacy-and-release.md`
- `references/characters.md`
- `references/scene-contract.md`
- `references/branching.md`
- `references/suspense-and-fairness.md`
- `references/dialogue.md`
- `references/art-and-sound.md`
- `references/production-budget.md`
- `references/existing-game-retrofit.md`
- `references/deliverables.md`
- `references/quality-gates.md`
