# AI-assisted (Claude, 2026-11-18/19): deliverables part (orders + output into deliverables/<id>/, empty/unfinished checks) written by Thomas, explained and reviewed by Claude; file-name/id check (2026-11-19) written by Claude. Verified: Claude ran the checks and the zip loop on fake orders in a temp folder.
"""Build the hand-in zip from the main repo and both submodules.

Run from anywhere:  python tools/make_handin.py
Includes every file tracked by git (main repo + python/ + cpp/), plus the processed orders:
python/orders/<id>.json and python/output/<id>/ go to deliverables/<id>/ (they are gitignored).
Writes COMMIT.txt with the full commit IDs. Refuses to run with uncommitted changes,
with no orders, or with an order that isn't done or rejected.
"""
import subprocess
import sys
import zipfile
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ORDERS_DIR = ROOT / "python" / "orders"
OUTPUT_DIR = ROOT / "python" / "output"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


if git("status", "--porcelain", "--ignore-submodules=none").strip():
    sys.exit("Uncommitted changes (in the main repo or a submodule). Commit first, then rerun.")

order_files = sorted(ORDERS_DIR.glob("*.json"))
if not order_files:
    sys.exit("No orders in python/orders/. Process the example orders first (README, Deliverables), then rerun.")

for path in order_files:
    order = json.loads(path.read_text(encoding="utf-8"))
    if order["id"] != path.stem:
        sys.exit(f"{path.name} has id {order['id']}. Order files must be named <id>.json; delete the copy and process again.")
    if order["status"] not in ("done", "rejected"):
        sys.exit(f"Order {path.stem} is {order['status']}. Start Spoolman and process orders again, or delete the order.")

commit = git("rev-parse", "HEAD").strip()
files = git("ls-files", "--recurse-submodules").splitlines()
zip_path = ROOT / f"pendulum-factory-{commit[:8]}.zip"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(ROOT / f, f"pendulum-factory/{f}")

    for path in order_files:
        folder = f"pendulum-factory/deliverables/{path.stem}"
        z.write(path, f"{folder}/order.json")
        out = OUTPUT_DIR / path.stem
        if out.is_dir():
            for f in sorted(out.iterdir()):
                z.write(f, f"{folder}/{f.name}")

    z.writestr("pendulum-factory/COMMIT.txt",
               f"main repo: {commit}\n" + git("submodule", "status"))

print(f"Wrote {zip_path.name}: {len(files)} files, {len(order_files)} orders in deliverables/, main commit {commit}")
