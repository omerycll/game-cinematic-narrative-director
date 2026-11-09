# Mandatory playable scene contract (camera-agnostic)

Require these fields for every production scene (not only the pilot):

```
SCENE_ID / TITLE / ACT / CANON_VERSION / STATUS / estimated route duration range
LOCATION + visible state + entry conditions + exits
CAST: stable character IDs and current physical/remote/recorded presence; knowledge and scene goal
DRAMATIC PURPOSE: dramatic question; entry-to-exit emotion and tension/release
CAMERA/ART: format-specific composition, depth layers, readability and state-change cues
AUDIO: ambience, musical motif, silence, captions, accessible visual alternative
FIRST 10 SECONDS: what the player sees, hears and can immediately attempt
OBJECTIVE: observable, player-controlled purpose
PLAYER VERBS: inspect/move/talk/choose/assemble/etc, as supported by actual game
HOTSPOTS: ID, affordance, examination text, use effect, invalid-action response, flags, animation
PUZZLES: exact rule, visible clue source, solution, partial feedback, recoverable failure,
         three hints, alternative access and downstream callback
DIALOGUE: usable lines, stable IDs, variants, character-specific voices and pauses
EVIDENCE: origin, acquired state, required/optional, reveal relationship, alternate access
CHOICES: player wording, requirement, immediate reaction, persistent effect, later callback
EXITS: guards, successor IDs, save trigger, safe fallback, replay and localization notes
ASSETS: base/variant ticket IDs, rigs, animations, SFX, production cost/reuse
QA: wrong-order, quitting/reloading, skipped clue, localization, small-screen input
```

A scene is incomplete if it lacks precisely what the player does, what feedback occurs and why that matters. A scene may deliberately have no branching choice, but must still contain meaningful interaction and stateful progression. Do not pad duration with unexplained waiting.
