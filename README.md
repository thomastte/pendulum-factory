# Pendulum Kit Factory: MAS417 Project 2026 (Group 5)

A small "flexible production" system for MAS417 at UiA.
- Customers order a 3D-printable pendulum kit with a chosen **swing period** in a web page.
- The program designs the kit automatically from parameters and checks it against the material in stock (Spoolman).
- It estimates the mass of each part, calculates and **simulates** the period, and writes **3MF files** ready for printing.

| | |
|---|---|
| Languages | Python 3.12 (main program), C++20 (pendulum simulator) |
| Stock | [Spoolman](https://github.com/Donkie/Spoolman) 0.27.0 in Docker, REST API |
| Printers | Bambu Lab P1S / A1 (build volume 256 × 256 × 256 mm) |

---

## Repository structure

This is the **main repository**. The Python program and the C++ simulator are separate repositories, included here as **git submodules** at fixed versions.

```
pendulum-factory/                 (this repo)
├── python/                       submodule → pendulum-factory-python   (main program)
├── cpp/                          submodule → pendulum-factory-cpp      (C++ simulator)
├── docker-compose.yml            Spoolman, pinned version
├── docs/uml/                     UML diagrams (PlantUML sources)
├── docs/ai-log.md                log of AI tool use
├── deliverables/                 processed example orders and their 3MF files (only in the hand-in zip)
└── tools/make_handin.py          builds the hand-in zip
```

---

## Requirements

| | Windows 10/11 | macOS (Intel or Apple Silicon) | Linux (Ubuntu/Debian) |
|---|---|---|---|
| Python 3.12 | python.org installer | `brew install python@3.12` | `sudo apt install python3.12 python3.12-venv` (Ubuntu 24.04) |
| C++ compiler | Visual Studio Build Tools, "Desktop development with C++" | `xcode-select --install` | `sudo apt install build-essential` |
| CMake ≥ 3.16 | cmake.org installer | `brew install cmake` | `sudo apt install cmake` |
| Docker | Docker Desktop | Docker Desktop | Docker Engine + Compose plugin |
| Git | git-scm.com | included with Xcode tools | `sudo apt install git` |

Use Python 3.12: the pinned NumPy and SciPy versions need 3.12 or newer, and CadQuery does not support 3.13 yet.

---

## Get the code

From git (the submodules must be included):

```bash
git clone --recurse-submodules https://github.com/thomastte/pendulum-factory.git
cd pendulum-factory
```

If you already cloned without `--recurse-submodules`, run `git submodule update --init`.

From the hand-in zip: unzip it. It already contains `python/` and `cpp/`.

---

## Quick start

Run every command from the `pendulum-factory` folder unless stated otherwise.

**1. Start the material stock (Spoolman):**
```bash
docker compose up -d
```
Spoolman is now at http://localhost:7912. Its API is at `/api/v1/`.

**2. Build the C++ simulator:**
```bash
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release
cmake --build cpp/build --config Release
```
This step is optional. Without the simulator the program falls back to a Python (SciPy) simulation and logs a warning.

**3. Set up Python:**
```bash
cd python
python3.12 -m venv .venv          # Windows: py -3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Steps 4–6 run from the `python/` folder, with the virtual environment active.

**4. Load the stock (see below):**
```bash
python scripts/seed_stock.py
```

**5. Start the web interface:**
```bash
flask --app pendulum.app run --port 5050
```
Open http://localhost:5050.
- The **order page** is `/`. The **operator page** is `/orders`.
- Port 5050 is used because macOS uses port 5000 for AirPlay Receiver.

**6. Process orders:** click **Process orders** on the operator page. To process the example orders without the web interface, run `python scripts/process_orders.py examples/orders`. The six example orders in `python/examples/orders/` give three `done` (two 80 × 80 × 200 kits and one 100 × 80 × 240 kit) and three `rejected` (a period the kit can't reach, a filament that is not in stock, and a kit too tall for the printer).

The results of each order are in `python/orders/<order id>.json`: `status` (`done`, `rejected` or `postponed`), `reason`, and `result` with the masses, the target, calculated and simulated period, the difference, and the spools used. The files of a `done` order are in `python/output/<order id>/`:

| File | Contents |
|---|---|
| `design.json` | The shared parameter file used by CAD, calculation and simulation |
| `u_stand.3mf`, `pendulum.3mf` | One printable file per part |
| `sim.csv`, `plot.png` | Simulated motion |

---

## How the material stock is loaded

The stock is the filament found in the UiA makerspace on 3 November 2026. It is listed in `python/config/stock_seed.json`, with:
- material, brand and colour;
- density from the manufacturer's datasheet;
- net spool weight from the label.

`scripts/seed_stock.py` registers each filament and its spools in Spoolman with POST requests: one 1000 g spool per colour, and two for PLA+ Black (a full 1000 g spool and a used one with 150 g left, so the order page shows 1150 g). It skips filaments that already exist, so running it twice is safe.

In a fresh Spoolman the filament ids are 1 White, 2 Black, 3 Red and 4 Blue. The example orders use these ids.

To start again from an empty stock:
```bash
docker compose down
# delete the spoolman-data/ folder
docker compose up -d
cd python && python scripts/seed_stock.py
```

---

## Tests

```bash
cd python
pytest                     # unit tests; no Docker needed
pytest -m slow             # the 6 design() tests, which build the CAD many times (about 25 s)
pytest -m integration      # only the tests against Spoolman; needs it running
```

---

## Deliverables

The processed example orders are only in the hand-in zip, not in the repository (`python/orders/` and `python/output/` are gitignored). Each order has its own folder, `deliverables/<order id>/`:

| File | Contents |
|---|---|
| `order.json` | The order after processing. `status` is `done` or `rejected`, `reason` explains it, and `result` holds the results: masses, target/calculated/simulated period and the difference, spools used, and the list of files |
| `design.json` | The shared parameter file used by CAD, calculation and simulation |
| `*.3mf` | One printable file per part |
| `sim.csv`, `plot.png` | Simulated motion |

A rejected order has only `order.json`.

The deliverables were produced from the commit listed in `COMMIT.txt` inside the zip:
1. Empty `python/orders/` and `python/output/`.
2. Start Spoolman and the web interface (Quick start, steps 1–5).
3. Copy `python/examples/orders/*.json` into `python/orders/` and click **Process orders** on `/orders`.
4. Run `python tools/make_handin.py`. It stops if there are uncommitted changes, no orders, or an order that is not `done` or `rejected`.

---

## Team

| | Role | Main responsibilities |
|---|---|---|
| Thomas | Product & physics | parameters, CAD, mass and period, design solver, C++ simulator |
| Øivind | Factory & stock | Spoolman, web interface, order processing, variants, packaging |

Both reviewed each other's pull requests. See the git history of all three repositories.

Planning documents (plan, roadmap, study guide) are in `docs/project/`. Team rules and the AI policy are in `CLAUDE.md`.

---

## Third-party software

| Software | Used for | Licence |
|---|---|---|
| CadQuery | parametric CAD, 3MF export | Apache-2.0 |
| NumPy, SciPy | calculations, fallback simulation | BSD-3-Clause |
| Flask | web interface | BSD-3-Clause |
| Requests | REST calls | Apache-2.0 |
| Matplotlib | plots | Matplotlib licence (PSF-based) |
| pytest | tests | MIT |
| Spoolman | material stock (run as a Docker image, not modified) | MIT |

No third-party source code is copied into this project unless it is marked in a comment.

## Use of AI

AI tools were used during this project. Each use is logged in `docs/ai-log.md`, and AI-assisted code is marked with a comment. See the report, section "Use of AI".
