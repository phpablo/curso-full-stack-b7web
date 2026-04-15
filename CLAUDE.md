# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an educational repository documenting the B7Web full-stack development course. It contains:
- **Trilha Python** (`trilha-python/`): Python learning path with fundamentals and exercises
- **Trilha Fundamentos** (`Trilha_Fundamentos/`): Foundation courses (HTML, CSS, JavaScript, PHP)
- **Trilha Complementares** (`Trilha_Complementares/`): Supplementary content including Docker projects

Each trilha is organized by numbered topics/lessons within subdirectories.

## How to Run Code

### Python Files
Python examples in the `trilha-python/` directory are simple educational scripts:
```bash
# Run a Python script
python 1-fundamentos-python/1-print.py

# On Windows with Python in PATH
python filename.py
```

### HTML/CSS/JavaScript Projects
Static projects can be opened directly in a browser or served locally:
```bash
# Simple HTTP server (Python 3)
python -m http.server 8000
```

## Git Conventions

This repository follows conventional commits with emoji prefixes:
- `:tada:` (`tada`) - Initial commits or major milestones
- `:hammer:` (`hammer`) - Feature implementations
- `:pencil:` (`pencil`) - Documentation or learning materials

Example commit:
```bash
git commit -m ":hammer:feat(f-strings): add comprehensive f-string examples"
```

## Repository Structure Guidelines

- Each "trilha" (learning path) is a separate directory with numbered lessons
- Within lessons, create subdirectories for projects or related examples
- Keep Python files simple and well-commented for educational purposes
- Include example outputs or expected behavior in comments

## Common Tasks

**View recent project history:**
```bash
git log --oneline -10
```

**Check repository status:**
```bash
git status
```

**Create a new learning example:**
1. Navigate to the appropriate trilha directory
2. Create or edit the lesson file
3. Add didactic examples with clear comments
4. Commit with appropriate emoji prefix

## Notes

- This is a **learning repository**, not a production codebase
- Focus on clarity and educational value in code examples
- Examples should be self-contained and easy to understand
- When adding new content, follow the existing directory structure and numbering convention
