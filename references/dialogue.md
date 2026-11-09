# Dialogue craft and implementation

## Line function
Every line must do at least one of: reveal character, alter power dynamics, give a playable clue, conceal a fact for a motivated reason, deepen empathy, change relationship state, or create purposeful silence. Remove repeated explanations and convenient exposition.

## Interactive dialogue contract
For every exchange, specify speaker ID, exact text, emotional subtext, audio/gesture, state prerequisite, player responses, reaction, flag mutations and later callbacks. Distinguish incidental dialogue from consequential decisions and irreversible actions.

## Voice differentiation
Give each major character a sentence rhythm, verbal habits, vocabulary limits, avoidable cliches, favored emotional defense and sample lines **created at runtime from the project**, not embedded in the public skill. Avoid interchangeable speeches. Record when and why voice patterns change with trust, fatigue or new knowledge.

## Implementation schema (no dialogue examples)

```text
DIALOGUE_ID | SCENE_ID | SPEAKER_ID | LINE_TEXT | CONDITION | VOICE_DIRECTION
RESPONSE_ID | PLAYER_LABEL | REQUIREMENTS | IMMEDIATE_REPLY_ID | FLAG_DELTA
CALLBACK_ID | LATER_SCENE_ID | CONDITION | CHARACTER_MEMORY | LOC_KEY
```

## Presentation and localization
Use stable keys independent of display text. Keep lines readable within the target screen size, allow skipping replayed text, provide captions for voiced content, and avoid puzzles that hinge solely on sound, color or flicker. Specify page breaks and variable substitutions.
