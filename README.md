# Skills Repository

This repository contains reusable agent skills.  
Each skill lives in its own folder and is centered around a `SKILL.md` file.

## Repository layout

- `*/SKILL.md`: Primary instructions for a skill
- `*/references/`: Optional deep-dive docs used by the skill
- `*/assets/`: Reusable templates and snippets
- `*/scripts/`: Utility scripts used by the skill
- `*/agents/`: Agent-specific configuration files (when needed)

## Current skills

- `arcgis-doc-lookup`
- `bootstrap-ng-bootstrap`
- `clean-code-handbook`
- `google-typescript-style-guide`

## Adding a new skill

1. Create a new folder named after the skill.
2. Add a `SKILL.md` with:
   - purpose and trigger conditions
   - workflow steps
   - safety notes and constraints
3. Add optional `references/`, `assets/`, `scripts/`, and `agents/` folders as needed.
4. Keep instructions concise and executable.

## Local checks

- Use `rg --files` to inspect repo contents quickly.
- Run skill-specific scripts directly from each skill folder when present.

## License

This project is licensed under the MIT License. See `LICENSE`.
