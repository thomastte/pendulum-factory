# CLAUDE.md: read this first

Context for any Claude (or other AI) working in this repo, for Thomas or Øivind. Keep it short and current. Update the **Status** section when a milestone is reached.

## The project

MAS417 (UiA) group project, "Flexible Production": a web app where a customer orders a 3D-printable pendulum kit with a given swing period. The program designs the parts, checks the filament stock in Spoolman, writes one 3MF file per part, and simulates the swing.

- **Team:** Thomas (product & physics) and Øivind (factory & stock).
- **Hand-in:** report + zip + full commit ID of this repo in WISEflow. We aim for **Wed 18 Nov 2026**; the deadline is **Fri 20 Nov 2026, 13:00**.
- **Plan, roadmap, study guide:** `docs/project/`. The roadmap checkboxes are the task list. These are copies of Thomas's Obsidian notes; if something here and in Obsidian disagree, ask Thomas.

## Repo layout

This is the **main repo**. `python/` and `cpp/` are **git submodules**: separate repos on GitHub (`thomastte/pendulum-factory-python`, `thomastte/pendulum-factory-cpp`) with their own history and pull requests. The main repo only stores which commit of each to use.

| Path | What | Owner |
|---|---|---|
| `python/pendulum/params.py`, `cad.py`, `physics.py`, `simulate.py` | parameters, CAD + 3MF, mass/period/bisection, C++ wrapper | Thomas |
| `cpp/` | C++ RK4 simulator (`pendulum_sim`) | Thomas |
| `python/pendulum/stock.py`, `processing.py`, `app.py`, `variants.py`, `templates/` | Spoolman client, order processing, Flask GUI, variant plots | Øivind |
| `python/scripts/`, `docker-compose.yml`, `README.md`, packaging | seed script, Spoolman, how to run | Øivind |
| `docs/uml/`, `docs/ai-log.md`, report | diagrams, AI log | both |

The function signatures the two halves agree on are in `docs/project/plan.md` §8. Don't change them without both agreeing.

## How we work

- **Branch per task** in the submodule (`feat/params`, `fix/spoolman-timeout`), pull request on GitHub, **the other person reviews and merges**. Merge commits, not squash.
- **Commit messages** say what and why: `Add RK4 step to C++ simulator`, not `update`. The git history is graded.
- **After a merge in `python/` or `cpp/`**, commit the new pointer in this repo: `Update python submodule: <what>`. Push the submodule before the main repo.
- **Never commit** `.venv/`, `cpp/build/`, `spoolman-data/`, `output/`, passwords or API keys. The `.gitignore` files handle the first four.
- **Units:** mm and g in JSON and CAD; m and kg only inside the physics.

## AI policy (agreed by the team)

1. **No unprompted changes.** Claude only edits or creates files, runs commands that change anything, or installs software when the person it is working with asks for that in the conversation. It may suggest; changes wait for a yes.
2. **Each person decides how to use AI for their own work**: explaining, reviewing, debugging or writing code are all allowed, as long as rules 3 and 4 are followed.
3. **Mark AI-assisted code** where it appears, in the same style as the existing files:
   `# AI-assisted (Claude, 2026-11-03): <what>. Verified: <how>.` (`//` in C++)
4. **Log every AI use** in `docs/ai-log.md`: one row with date, who, tool, what it was used for, what was used, how it was checked. When Claude makes or suggests a change, it also gives the log row. The log feeds the report's mandatory "Use of AI" section.
5. AI is not a source in the report, and never paste passwords or keys into an AI tool.

## Notes for Claude in the desktop app (folder access)

- **Don't run git commands that write.** The app's folder access can't delete files, and git deletes its own lock files: `commit`, `pull`, `checkout`, `merge`, `stash` and even a plain `git status` can leave `.git/*.lock` files that break the repo. For reading, use `GIT_OPTIONAL_LOCKS=0 git status` / `git log`. The person commits and pushes in GitHub Desktop.
- If a `.lock` file is ever left behind, tell the person; they delete it in Explorer (with GitHub Desktop closed).

## Environment (Windows)

```
:: C++ simulator (once, and after changes to main.cpp)
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release
cmake --build cpp/build --config Release

:: Python (once per computer)
cd python
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

- Python **3.12** (CadQuery's documented range).
- Thomas builds with MSYS2 g++ + Ninja: add `-G Ninja` to the first cmake command. With Visual Studio Build Tools, the commands above work as written and the program ends up in `cpp/build/Release/`.
- `pytest` should report `4 passed`; `2 passed, 2 skipped` means the C++ simulator isn't built.
- Spoolman: `docker compose up -d` in this folder, then http://localhost:7912.

## Status (3 Nov 2026)

**Done**
- Three repos on GitHub (`thomastte/...`), submodules linked, drafts committed.
- Thomas: toolchain works on Windows (Python 3.12.10, g++ 15.2, CMake 4.1, Ninja); `pytest` 4 passed.
- Øivind: onboarding done on Windows (Python 3.12.10, VS Build Tools/MSVC, CMake 4.4, Docker 29.9); `pytest` 4 passed. Two Windows snags: Smart App Control blocked the self-built `pendulum_sim.exe` (turned off), and Docker Desktop needed WSL (`wsl --install --no-distribution`, then restart).
- Spoolman runs in Docker; tag `0.27.0` (no `v`) is correct. The REST calls in plan §5.1 match Spoolman v0.27.0. Catch: `remaining_weight` is missing from responses unless the spool has `initial_weight` or the filament has `weight`, so the seed script must always set `initial_weight`.

**Next**
- Thomas: invite the lecturer to all three repos (Øivind's access works); `params.py`, then the first CadQuery part to 3MF. Undecided whether Thomas rewrites the AI-drafted simulator himself.
- Øivind: `config/stock_seed.json` + seed script, `SpoolmanClient` with timeout handling, use case diagram.
- Both: makerspace survey; plan email to the lecturer **Wed 4 Nov** (needs the Canvas group number; draft in `docs/project/plan-email-draft.md`).

**Known unverified**
- `requirements.txt` isn't pinned yet; both computers now work, so it can be pinned with `==`.
