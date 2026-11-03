# AI use log

One line per significant use. This feeds the report's "Use of AI" section (required by the spec, §4).

| Date | Who | Tool | What it was used for | What we used | How we checked it |
|---|---|---|---|---|---|
| 2026-10-29 | Thomas | Claude | Project plan, roadmap, study guide, repo/README drafts, UML drafts, hand-in zip script | Plan structure, README drafts, PlantUML diagrams (edited) | Read against the spec; diagrams rendered and checked against UML notation |
| 2026-10-29 | Thomas | Claude | C++ RK4 simulator (`cpp/src/main.cpp`) and `simulate.py` | Code, marked in comments | Period compared with exact formula (agrees to ~1e-13); code read and explained by Thomas |
| 2026-11-02 | Thomas | Claude | Replaced role placeholders A/B with Thomas/Øivind in plan, roadmap, email draft and README; advice on what to start with | Text edits only, no code | Diff read through; no Person A/B left in the edited notes |
| 2026-11-02 | Thomas | Claude | Restored the study guide (What to Know) from the 29 Oct chat after it was overwritten; GitHub Desktop walkthrough in Repo Setup | Restored text (names updated), setup steps | Restored text compared with the 29 Oct transcript; setup steps followed by hand |
| 2026-11-02 | Thomas | Claude | Repo hosting changed from a GitHub organisation to Thomas's account (Repo Setup, Roadmap); fixed 13 single-letter A/B table cells the first rename missed (plan, Python README) | Text edits only | Searched all notes and drafts for leftover A/B and organisation references |
| 2026-11-02 | Thomas | Claude | Review of .gitignore files: found that `orders/` in the Python draft also ignored `examples/orders/` | Fix: anchored `/output/` and `/orders/` to the repo root | Checked with `git check-ignore -v` before and after |
| 2026-11-02 | Thomas | Claude | Step-by-step guidance for creating the three repos and submodules with GitHub Desktop; commit messages | Instructions only; Thomas did every step | Repos checked on github.com; submodule links open the right commits |
| 2026-11-03 | Thomas | Claude | Toolchain setup guidance: Python 3.12 venv, CMake + Ninja via MSYS2, first build and test run | Instructions only | pytest: 4 passed |
| 2026-11-03 | Thomas | Claude | `CLAUDE.md` (project context, team rules, AI policy), `docs/project/onboarding.md`, and GitHub copies of the Obsidian planning notes in `docs/project/` | Generated text; AI policy wording from Thomas's instructions | Links and images checked; Thomas reads before committing |
| | | | | | |
