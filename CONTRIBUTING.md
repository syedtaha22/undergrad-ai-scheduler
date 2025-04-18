# Contributing Guidelines

To ensure consistency, clarity, and maintainability across the **Undergrad-AI-Scheduler** project, contributors are required to follow the structured guidelines outlined below.

---

## Branching Strategy

- The default and protected branch is: `main`  
- The primary working branch is: `dev`
- For new feature development: create a branch named `feature/<module-name>`  
- For bug fixes: create a branch named `bugfix/<brief-description>`

**Note:**  
Do **not** commit directly to `main`. All changes must go through `dev` and follow the standard pull request process.

---

## Naming Conventions

To maintain uniformity throughout the codebase:

### Branches
- Format: lowercase with hyphens  
- Examples:  
  - `feature/csp-engine`  
  - `bugfix/teacher-filtering-issue`

### Directories
- Format: lowercase with underscores  
- Examples:  
  - `ai_engine/`  
  - `data_models/`  
  - `api/`  
  - `frontend/`  
  - `tests/`

### Files
- Format: lowercase with underscores  
- Examples:  
  - `scheduler_core.py`  
  - `constraint_parser.py`

### Classes
- Format: PascalCase  
- Example: `CourseConstraintSolver`

### Functions and Methods
- Format: snake_case  
- Example: `generate_schedule()`

### Variables
- Format: snake_case  
- Example: `preferred_teachers`

---

## Commit Message Format

Use the following format for all commit messages:

```
<type>: <short summary>

<optional detailed explanation>
```

### Accepted Types
- `feat`: New feature implementation
- `fix`: Bug fixes
- `refactor`: Code restructuring without changing behavior
- `docs`: Documentation-related changes
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks or minor non-functional changes

**Examples:**
- `feat: implement CSP constraint evaluation logic`
- `fix: correct issue in teacher conflict resolution`
- `refactor: separate scheduling engine from API handler`

---

## Project Structure (Tentative)

```
Undergrad-AI-Scheduler/
│
├── ai_engine/            # AI logic and CSP implementation
├── api/                  # Backend logic and request handlers
├── data_models/          # Python classes for course, teacher, and user constraints
├── frontend/             # React frontend application
├── configs/              # Configuration files
├── scripts/              # One-off scripts (e.g., data preprocessing)
├── tests/                # Unit and integration tests
└── README.md
```

> Structure may evolve during development but should be updated and documented accordingly.

---

## Code Review Policy

- All pull requests must be reviewed by at least one contributor before merging into `dev`.
- Merges to `main` may only occur once the `dev` branch is verified as stable.
- Reviews should prioritize readability, logic correctness, and compliance with project conventions.

---

## Contribution Notes

- All contributors are expected to adhere to this guideline.
- Any deviation must be discussed and approved before implementation.
- Updates to this document must go through the same contribution process.
