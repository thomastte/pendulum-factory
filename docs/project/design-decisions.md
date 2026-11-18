---
type: decisions
course: MAS417
related: "plan.md, roadmap.md"
created: 2026-11-03
tags:
  - MAS417
  - project
  - design
---

# MAS417 Design Decisions

> [!NOTE]
> **Shared copy.** Thomas keeps the original of this note in his Obsidian vault; this copy was synced on 2026-11-17. **Where this note and [plan.md](plan.md) disagree, this note is the current design**: the plan's §3 (pendulum) and §6 (GUI) still describe the first draft (disc weight, hub, amplitude and infill in the order, five filament dropdowns).

The physical design of the pendulum kit, decided one question at a time. The spec only fixes that the kit has a base, two stand sides, an arm with a hole for the axle, a weight on the arm and an axle, and that *"how the parts are shaped and assembled is part of your design"*. Everything else is ours to decide. Each decision here is Thomas's; Claude explained the options. This note feeds the report's design section.

## Decided

**Design goal (Thomas):** the widest possible period range for any given size of the kit.

| # | Decision | Why | Date | Depends on |
|---|---|---|---|---|
| 1 | Base and both stands are printed as **one U-shaped part**. The stands are wide, not as small as possible. | Fewer parts. It's a desk ornament, so it should look and stand solid. | 2026-11-03 | Lecturer OK (see open question 1) |
| 2 | Axle, arm and weight are printed as **one rigid piece**. The axle rests in notches at the top of the stands and turns with the pendulum. | Fewer parts, simple assembly: the pendulum lifts in and out. No printed hole that can bind on the axle. | 2026-11-03 | Lecturer OK (see open questions 1 and 2) |
| 3 | The pendulum is printed **lying down** (axle horizontal on the bed), with a **hammer-shaped weight**: a block as tall as the arm, which gets its mass from its thickness along the axle and its length along the arm. Nothing needs support. | Thomas wanted a weight shape that prints well. Upright (axle vertical) always needs support under the arm and weight; lying down needs none, and its layers run along the axle, its strong direction. Both were close, so Thomas asked Claude to choose. | 2026-11-03 | — |
| 4 | The axle rests in a **U-slot**: a rounded cradle slightly wider than the axle. | Sits at one contact point under the axle, so friction is no higher than a round hole (a V-notch gives about 1.4×). The walls hold the axle in the swing direction. The pivot stays at the axle centre, so the normal pendulum formula holds (a flat top would let the axle roll, giving about 4 % longer period). | 2026-11-03 | — |
| 5 | The **axle diameter is our design choice**, not something the customer orders. | Not a requirement: the spec lists it only as an example of what an order *could* ask for ("for example the swing period, the largest allowed size, the axle diameter and the amount of material"). | 2026-11-03 | — |
| 6 | The **customer orders the pendulum size** (through the kit height, decision 8). The program finds the **weight position** along the arm that gives the ordered period. | Size is what a customer naturally cares about. One equation (the period) can solve one unknown, and the weight position covers a useful range: about 0.53–0.75 s for a 150 mm arm in an example. Orders outside the range are rejected with the reason. | 2026-11-03 | — |
| 7 | **No material limit in the order.** | A customer has no reason to choose grams of filament. The spec mentions "the amount of material" only as an example. The stock check in Spoolman (enough grams on the chosen spools) is still required. | 2026-11-03 | — |
| 8 | The customer orders the kit's **height H, width W and depth D**. The arm length follows: **L = H − t − c − a** (t = base thickness, c = clearance under the arm, a = axle offset from the top of the uprights down to the axle centre). **H is measured from the table**, so the base thickness counts. | Size is what a customer cares about, and the table is where they would measure from. W also sets the gap between the uprights, and so how thick the weight can be. | 2026-11-05 | — |
| 9 | The weight is **always as big as the U allows**; the customer does not choose it. | Fits the design goal: the heaviest weight gives the widest period range for a given size. One order field fewer. Thomas leaned this way; Claude agreed. | 2026-11-05 | — |
| 10 | The weight block's **length along the arm is fixed at 35 % of the arm length L**. No search over lengths; the program only finds the weight position. | Simplest: one bisection per order. In a simple model (uniform arm, block as a thicker section), 35 % of L gives within 0.5 % of the widest possible period range for any arm length and for block/arm thickness ratios from 3 to 20. A fixed length in mm loses range on small and large kits (45 mm: ratio 1.24 at L = 80 mm vs 1.29 at 35 %). Cost: a few percent at the extreme ends compared with trying several lengths per order. | 2026-11-05 | — |
| 11 | **Axle diameter 8 mm.** Arm and weight block are also **8 mm tall** (so all three rest flat on the bed). **Arm thickness along the axle: 4 mm.** | A thicker axle adds friction (braking torque grows with the radius) and filament for no gain. A thin arm widens the period range; 4 mm is about ten perimeters, so it prints solid. | 2026-11-05 | — |
| 12 | A small **collar on the axle just inside each upright**, flat on the print-bed side. | Stops the pendulum drifting sideways. Rubbing then happens at the axle, not between the block and an upright ~100 mm below the axle (about 10× the braking torque). The flat keeps the pendulum support-free. | 2026-11-05 | — |
| 13 | **U starting values:** upright wall 6 mm, base thickness t = 5 mm, clearance under the arm c = 5 mm, slot 0.4 mm wider than the axle, slot depth = axle diameter (axle flush with the top, so a = 4 mm), side clearance block ↔ upright 2 mm each side. | Plausible for a desk ornament. The slot width is a guess: test it with a small print of one slot and a short axle. | 2026-11-05 | Test print (slot) |
| 14 | The U is printed **standing on its base**. | Slots at the top open upward, so they print cleanly. Layer lines across the uprights make them weaker in bending, but the only load is the pendulum's own weight. | 2026-11-05 | — |
| 15 | The axle sticks out **2 mm** past the outside of each upright. The collars sit **1 mm** from the inside of each upright and are **Ø14 × 3 mm**, flat on the print-bed side. | Thomas chose the 2 mm overhang. A 2 mm collar gap would let the block (2 mm side clearance) touch an upright at the same moment as a collar, so Claude set 1 mm, and the collar size, at Thomas's request. With 1 mm of play the axle never leaves its slots. | 2026-11-05 | — |
| 16 | The uprights are **narrow posts** centred on the base, **30 mm deep** (starting value). D sets only the base depth. | A full-depth wall is a waste of filament. The posts don't affect the swing. | 2026-11-05 | — |
| 17 | The **period and the filaments stay in the order**. `PendulumParams` describes only the physical kit. | The period is a target, not a dimension; the filaments only matter for mass, and `design(order, densities)` gets the densities separately. Same split as the old plan, so Øivind's code is unaffected. | 2026-11-05 | — |
| 18 | **Start angle 45°.** The swing amplitude is a result, not something the customer orders. | Thomas's choice. Consequence: at 45° the period is 4.0 % longer than the small-angle value (5°: 0.05 %), so the ordered period is defined as the period when released from 45°, and the calculation must use the exact large-angle formula (the simulator already handles this). As friction shrinks the swing, a real print's period drifts toward the small-angle value, by up to 4 %. | 2026-11-09 | — |
| 19 | **Infill is fixed by us** (print settings), not chosen by the customer. The order's period is always understood as the period at the 45° start. | The customer has no reason to choose infill, and it does not change the period (decision 6). Order fields: id, customer_ref, target period, H, W, D, filaments, status, reason. | 2026-11-09 | — |
| 20 | **Two 3MF files per order, one per printed piece**: the U and the pendulum, each one solid body. | Matches what is printed (decisions 1 and 2) and one filament per piece; no plate-layout code. Plan §8 `export_3mf` changes from "one file per part" (tell Øivind). | 2026-11-12 | — |
| 21 | **The spec's parts are built as separate solids, cut so they don't overlap, then fused** into the two printed bodies. Axle = full cylinder; collars = rings; arm = bar minus axle (full length); weight = block minus arm (two halves). Posts start on the base's top face. | Per-part masses (spec §3.1) add up exactly to the printed piece. The period and the Spoolman grams come from the fused bodies. Limitation: per-part masses count contact faces as walls (about 2 g too much in total at BaseHeight 200). | 2026-11-12 | — |
| 22 | **CadQuery measures the solids** (volume, centre of mass, moment of inertia); no hand formulas for I. Uniform density per printed piece = its mass / its volume. | One geometry source, exact for any shape. | 2026-11-12 | — |
| 23 | **CAD origin at the pivot (axle centre)**: x along the axle, y the swing direction, z up, parts modelled in their assembled position. For export the U is moved up onto z = 0 and the pendulum is rotated 90° to lie flat. | The physics reads the moment of inertia about the x-axis directly, and `WeightPos` is the block centre's distance below the origin. | 2026-11-12 | — |
| 24 | **The search for the weight position runs over the whole arm** (block just below the collars + 0.1 mm → block at the tip), without first finding the period dip. | The dip lies above the collars for most kit sizes (e.g. 80 × 200, 50 × 200); for narrow kits (W ≲ 40) it lies inside the range but is at most 4.4 ms deep. Searching from the collars gives exactly one solution for every target above the period there; only targets in that thin band are rejected. Finding the dip would cost about 3.5 s per order for a gain far below the model's own accuracy (up to 4 % drift as the swing decays, decision 18). The 0.1 mm margin avoids a CadQuery union failure when the block exactly touches the collars. | 2026-11-18 | Replaces "dip → tip" in decision 6 |

**What follows:**
- The code still builds the base, the two stand sides, the arm, the weight and the axle as separate solids from parameters (spec §3.1), then joins them into the two printed pieces. Each part keeps its own volume and mass.
- From 3: axle, arm and weight all rest flat on the bed. The simplest way is to make the arm and the weight exactly as tall as the axle diameter (see open question 6).
- From 6 and 24: the period first dips, then rises as the weight moves from the axle to the tip, so two positions can give the same period. For most kit sizes the dip lies above the collars, so it is never reached; for narrow kits it is inside the range but at most 4.4 ms deep. The search runs from the collars to the tip (decision 24).
- From 6: **infill can't tune the period.** The pendulum is one piece with one filament and one infill, so changing the infill scales mass and moment of inertia equally, and T = 2π·√(I / (M·g·d)) stays the same. It only matters if arm and weight get different infill, which needs per-region slicer settings.
- From 4: the slot needs a clearance (slot radius = axle radius + clearance). The value is a guess until a small test print.
- From 8, 11 and 13: **L = H − 14 mm** (5 + 5 + 4), and the block thickness along the axle = **W − 16 mm** (two 6 mm walls, two 2 mm side clearances).
- The old "weight must fit between the stands" problem (weight 14 mm vs 12 mm gap) no longer applies. The gap between the uprights becomes a parameter of its own.

**Note on friction:** the notches do not reduce friction compared with a hub on a fixed axle. Sliding friction does not depend on contact area: the braking torque is about μ·N·r (r = axle radius) either way, and a V-notch raises it by 1/cos β (β = flank angle from horizontal; about 1.4× for a 90° V). Friction mostly sets how long it keeps swinging, and barely changes the period.

## Open

1. **Ask the lecturer:** one printed piece means one filament. Does that satisfy *"selects a filament for each part"*?
2. **Ask the lecturer:** is a one-piece pendulum OK, given *"a pendulum arm with a hole for the axle"*?
3. **Tell Øivind:** this changes the parts list and order fields in plan §8 (order: period, H, W, D and filaments; no axle diameter, material limit, weight size, amplitude or infill) and the five filament dropdowns in his order form.
