# Onboarding: Øivind (Windows)

Gets you from nothing to the same working setup Thomas has: the three repos cloned, the C++ simulator built, `pytest` passing, and Claude knowing the project. About 1–1.5 h, mostly installs. If you use Claude in the desktop app, add the repo folder (step 4) and ask it to walk you through the rest.

## 1. GitHub access

1. Send Thomas your GitHub username.
2. Thomas invites you to **all three** repos: `pendulum-factory`, `pendulum-factory-python`, `pendulum-factory-cpp`.
3. Accept **all three** invitations (email, or https://github.com/notifications). Without all three, the submodules can't be cloned.

## 2. Install the tools

Run these in Command Prompt, one at a time. Accept prompts with `Y`.

```
winget install GitHub.GitHubDesktop
winget install Git.Git
winget install Python.Python.3.12
winget install Kitware.CMake
winget install Docker.DockerDesktop
```

Then install by hand:
- **Visual Studio Build Tools** (the C++ compiler): https://visualstudio.microsoft.com/downloads/ → *Tools for Visual Studio* → **Build Tools for Visual Studio**. In the installer, tick **Desktop development with C++** and install. This is only the compiler; you don't need the Visual Studio editor. (Thomas uses MSYS2 g++ instead, so between you both build routes in the README get tested.)
- **Bambu Studio**: https://bambulab.com/download/studio
- **VS Code extensions** (if you use VS Code): Python, C/C++, CMake Tools (all by Microsoft).

**Restart the PC** afterwards. Docker Desktop needs it (it sets up WSL 2), and every program then sees the new tools.

Check in a **new** Command Prompt:
```
git --version
py --list
cmake --version
docker --version
```
`py --list` must show 3.12.

## 3. Clone the repos

1. Open **GitHub Desktop** and sign in (File → Options → Accounts). Under **Git**, use the email on your GitHub account, so your commits count as yours.
2. File → **Clone repository** → **URL** tab → `thomastte/pendulum-factory`.
3. Local path: `C:\Users\<you>\Documents\pendulum-factory`. Keep it **outside** OneDrive and any Obsidian vault.
4. Check that `python\` and `cpp\` are **not empty**. If they are, Repository → **Open in Command Prompt** and run:
   ```
   git submodule update --init
   ```
5. File → **Add local repository** → `...\pendulum-factory\python`, then the same for `...\cpp`. GitHub Desktop now lists three repos.
6. In each of `python` and `cpp`: if **Current branch** says *detached HEAD*, pick **main**. Always work on a branch, never on a detached HEAD.

How the three repos fit together, and the daily workflow: [repo-setup.md](repo-setup.md) §1 and §2b ("Daily workflow in Desktop").

## 4. Claude

1. In the Claude desktop app, add the folder `Documents\pendulum-factory`.
2. Start with: **"Read CLAUDE.md in the repo first."** It has the project, who owns what, the git rules and our AI policy. (Claude may or may not load it by itself; asking makes sure.)
3. The AI policy in short: Claude makes no changes you didn't ask for; you decide how much you use it; every use is marked in the code and logged in `docs/ai-log.md`.

## 5. Build and test

In Command Prompt:
```
cd "%USERPROFILE%\Documents\pendulum-factory"
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release
cmake --build cpp/build --config Release
cpp\build\Release\pendulum_sim.exe
```
The last line should print `usage: pendulum_sim I M d g theta0 ...`.

```
cd python
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```
`pip install` takes a few minutes (CadQuery is large). The goal is **`4 passed`**. `2 passed, 2 skipped` means Python didn't find the simulator.

In VS Code: open the `python` folder → Ctrl+Shift+P → **Python: Select Interpreter** → `.venv`. New terminals then activate it automatically.

## 6. Spoolman (your first task)

```
cd "%USERPROFILE%\Documents\pendulum-factory"
docker compose up -d
```
Open http://localhost:7912. If the image isn't found, the tag in `docker-compose.yml` may need a `v` (`v0.27.0`); check the release name on https://github.com/Donkie/Spoolman/releases. Then compare the REST field names in [plan.md](plan.md) §5.1 with the API docs your Spoolman serves.

## 7. What's next

See [roadmap.md](roadmap.md) and the **Status** section in `CLAUDE.md`. Week 1 for you: Spoolman running, `stock_seed.json` + seed script, `SpoolmanClient` with timeout handling, the use case diagram, and reviewing the plan email with Thomas before it goes out **Wed 4 Nov**.
