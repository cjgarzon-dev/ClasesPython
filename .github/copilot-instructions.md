<!-- Copilot instructions tailored for the ClasesPython teaching repository -->
# Copilot instructions for this repository

Purpose
- Help AI coding agents quickly understand this learning-oriented Python repository and be immediately productive.

Big picture
- This repo is a collection of teaching modules (folders named `Modulo*`) with per-session examples, exercises, and small projects. Each module groups multiple lessons (folders like `03_Sesion`, `04_sesion`, `05_Sesion`, etc.).
- Files are primarily standalone Python scripts and Jupyter notebooks used as examples — there is no single packaged application or service boundary.

Key directories and examples
- `Modulo2/03_Sesion/01animal.py` — small example script showing object-oriented patterns.
- `Modulo3/05sesion/01proyecto/` — a tiny project that includes `test/` and demonstrates unit testing with `unittest`.
- `Modulo4/08_sesion/` and `Modulo5/` — contain SQL schema files (`BaseDatos1.sql`, etc.) and examples of DB exercises.
- Notebooks: many teaching notebooks live under `Modulo4/**` and `Modulo3/**` (files ending `.ipynb`).

Repository conventions (important)
- Filename prefixes: many files use numeric prefixes (e.g., `01heredity.py`, `02composition.py`) to indicate lesson order — preserve prefixes when adding related lesson files.
- Language & style: code is instructional — prefer clear, minimal edits that preserve the didactic intent (don’t over-optimize examples unless fixing bugs).
- Tutorial folders: `tutoria`, `tutoria2`, and `tutoriaReto2` contain guided exercises; treat them as example-driven, not production code.

Run & test guidance (concrete commands)
- Run a script from repository root (Windows PowerShell):
```
py -3 path\to\script.py
```
- Typical example: run the session starter:
```
py -3 Modulo3\01_sesion\01inicio.py
```
- Run unit tests (example in `Modulo3/05sesion/01proyecto`):
```
py -3 -m unittest discover -s Modulo3\05sesion\01proyecto\test
```
- Jupyter notebooks: install Jupyter and run:
```
py -3 -m pip install jupyterlab
py -3 -m jupyter lab
```

Dependency & environment notes
- There is no single `requirements.txt` or `pyproject.toml` at the repo root. Before installing, search for a requirements file in the target module. If none exists, use a minimal environment: `pip install ipython jupyter pytest` as needed.

Patterns & code smells to expect
- Small self-contained examples (single-file scripts) rather than packages — changes should avoid introducing heavy packaging unless requested.
- Many examples are oriented to teaching patterns (strategy, observer, factory, singleton). When editing, keep examples explicit (avoid obscure one-liners).

Integration points
- SQL files in `Modulo4`/`Modulo5` are standalone schema/examples; altering them is safe but note they are used for exercises rather than runtime integration.
- No external services or CI config were found; assume local execution unless the PR adds CI.

Guidance for AI agents making changes
- Keep edits minimal and explicit: prefer small focused fixes or incremental improvements with clear explanations in commit messages.
- When adding tests, place them alongside the lesson/project under a `test/` folder and use `unittest` to match existing examples.
- Preserve educational value: add clarifying comments where appropriate, but do not convert instructional code to production patterns (e.g., dependency injection frameworks) unless requested.

Examples to reference in PRs or code suggestions
- Fix a bug in `Modulo2/03_Sesion/03payProcess.py` — show before/after with a short unit test added to `Modulo2/03_Sesion/test/`.
- Add a small exercise runner in `Modulo3/05sesion/01proyecto` — keep CLI usage simple: `python -m projeckt.module` style is not required; prefer `py -3 script.py` for consistency.

If you are unsure
- Ask a human. This is a teaching repository where intent matters; when in doubt about changing examples, open a short issue or request clarification.

Please review and tell me which sections need more detail or examples.
