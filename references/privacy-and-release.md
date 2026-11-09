# Public skill / private project separation

## Public package rules

Only ship reusable methodology, general templates, generic schema and validators. Exclude all unpublished scripts, plots, characters, gameplay balancing, client names, project screenshots, story exports, sample save files, private notes, local paths and examples derived from projects.

## Runtime when invoked by an agent

- Read only files in the project/workspace the user authorizes. Do not crawl adjacent repositories for "helpful" context.
- Output narratives and tests under the game project, not under the installed skill.
- Never copy a game's source or generated output into SKILL.md, examples, references, assets, git history or released ZIP files.
- If asked to publish the skill, audit **both current files and git history** if it is being pushed to an existing repository. Removing a secret from the latest commit does not remove it from public history.
- Do not use actual game content in public examples, demos, screenshots, issue reports or unit fixtures without explicit permission.
- No remote upload/commit/push as a side effect of a local analysis. Obtain separate authorization for release action.
- Do not claim local-only processing implies a provider never sees data; review runtime, connector access and product privacy settings separately.

## Release checklist

1. Create release from a new empty export directory, not by archiving an entire game folder.
2. List files including hidden files; inspect their contents, metadata and archive entries.
3. Search for names, key phrases, internal paths and personal notes in every file.
4. Remove all project-specific examples. Prefer placeholder schema or entirely synthetic IDs.
5. If using version control, check commits and tags for accidental prior inclusion.
6. Apply an explicit license only after the owner decides publishing rights.
7. Test the archive in an isolated temp directory with no access to game repositories.
8. Publish only after the owner approves the exact archive/repository diff.
