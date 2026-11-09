# Narrative retrofit without changing an existing game's identity

## Preserve before proposing

This is a narrative layer improvement workflow, not a mechanic-conversion command. Match the actual project verbs (choice, combat, exploration, crafting, management, dialogue or hybrid) and existing camera, economy, level sequence and saves.

Before editing, locate authorized project sources. Evidence order:
1. Verified narrative data / scene files / IDs, with paths and versions.
2. User descriptions, suitable only for concept proposals.
3. Hypothetical proposals, never a fact about the real game.

Create `CANON_LOCK.md` with sources; protected mechanics and progression; known lore; unknowns; permitted narrative changes; and reserved IDs. Save game output under a designated **project-local** docs directory, not this reusable skill.

## Required before/after card

```
SOURCE_ID: an existing event/scene/quest ID, or HYPOTHETICAL_ID if no evidence exists
SOURCE_PATH: exact path and version, or "not available"
BEFORE: exact verified source excerpt, or "not available"
PROBLEM: agency, character logic, pacing, stakes or readability issue
AFTER: actual revised player-facing text and options
PRESERVED: input verb, screen, economy, challenge and canon constraints
IMMEDIATE: animation / feedback / local data mutation
DELAYED: where consequences return and how they manifest
IMPLEMENTATION: localization IDs, assets, save flags, backwards compatibility
VALIDATION: reachable paths, reload, skips, no-asset fallback, rollback
STATUS: proposal / approved / implemented / tested
```

Do not imply that an imagined sample was extracted from a repository.

## Adapt across mechanics

- **Choice-heavy games:** existing choices become character-driven dilemmas; maintain current meter/cost semantics and explicit save flags. Attach consequences to later events.
- **Single-location simulations:** existing interactions and state changes express story through evolving props, dialogue, ambient changes and new decisions, not a forced world-map or unrequested construction loop.
- **Exploration or puzzle games:** integrate clues and motivations into reachable rooms and objects; make every important reveal playable and reconstructible.
- **Action or strategy games:** express arcs through missions, enemy intent, level dressing, outcomes and debriefs without replacing core inputs.
- **Procedural/roguelike games:** build event grammars and mutually exclusive conditions; prevent contradictions, repeated beats and impossible character returns.

## Safe application protocol

1. Audit read-only and show proposed changes.
2. Ask for approval before rewriting established canon, save schema or large portions of game code.
3. Work in a feature branch or backups if the user authorizes implementation; retain original text.
4. Validate state paths and presentation. Explain migration requirements and scope risk.
5. Produce non-numeric before/after evidence matrix. If numeric editorial scoring is used, label it subjective.
6. Do not publish source game narrative in skill repositories, distributable examples or public test reports.
