# Branching, replayability, endings and causal state

## 3 branch tiers
1. **Immediate:** visible feedback and a later single-line callback (low cost).
2. **Material:** changes NPC trust, object availability, a puzzle's solution, or a scene's physical state (medium cost).
3. **Route:** entirely different playable room sequence, companion, confrontation, or earned ending (high value). Require at least two material route splits for replay claims.

## Flag schema
- Store scene IDs and immutable choice IDs separately from localized UI strings.
- Prefer integer `trust_character_a`, `evidence_count`, `consent_level`, `safety_status` bounded to 0..3 or 0..5 plus booleans for critical facts. Document possible range and all mutation sources.
- Use **earned ending predicates** based on earlier action bundles. Include a fallback ending in every valid run; do not let the player get trapped when a choice was missed.
- Optional clue may enrich an ending but should not withhold the only viable ending. Major gates should be clearly telegraphed before commitment.
- Prefer foldback branching: costly unique scenes at split, then shared environment with altered dialogue, hazards, allies and consequences. Never secretly pretend a branch is unique when only one line differs.

## Required tests
1. Reachability of all scenes and all endings from default state.
2. No required clue known only in unreachable path.
3. Every irreversible choice writes a persistent variable and a downstream observable consequence.
4. No dead ends or negative flags preventing completion after story revisits.
5. One safe or painful-but-viable exit is always reachable.
6. Save/reload before/after each flag mutation; do not double count scores.
7. Restart and chapter replay options; chapter replay either isolates simulation or restores checkpoint with explicit warning.
8. Distinct-play route audit: list location, interaction, revelation and character outcome unique to each route; total minutes of genuinely new scenes.

## Choice matrix template
`Choice ID | scene | player wording | immediate reaction | state mutation | callback scene | route difference | ending contribution | production cost`

## Time model
For a route, time = played scene inspection + mandatory puzzle engagement + dialog/choice + transition; no idle padding. Estimate first run, replay with known puzzle solutions, replay pursuing different route, and completionist run separately. Never multiply first-run time by number of endings or imply all content appears in each run.
