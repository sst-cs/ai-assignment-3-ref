"""
Demo runner for AI Assignment 03 – Local Search (N-Queens).
Run:  python main.py
"""
from utils import num_conflicts
from search import hill_climbing, random_restart_hc, simulated_annealing, beam_search

N = 8
INITIAL = [3, 6, 4, 1, 5, 0, 2, 7]   # a board with several conflicts

print(f"N = {N}")
print(f"Initial state    : {INITIAL}")
print(f"Initial conflicts: {num_conflicts(INITIAL)}\n")
print("=" * 50)

# ── Hill Climbing ─────────────────────────────────────────────────────────────
hc = hill_climbing(N, INITIAL[:])
if hc is not None:
    print(f"[HC]   Result     : {hc}")
    print(f"[HC]   Conflicts  : {num_conflicts(hc)}")
else:
    print("[HC]   Returned None – check your implementation.")

print()

# ── Random-Restart Hill Climbing ─────────────────────────────────────────────
rrhc = random_restart_hc(N, max_restarts=20, seed=42)
if rrhc is not None:
    state, idx = rrhc
    print(f"[RRHC] Result     : {state}")
    print(f"[RRHC] Conflicts  : {num_conflicts(state)}")
    print(f"[RRHC] Best found on restart #{idx}")
else:
    print("[RRHC] Returned None – check your implementation.")

print()

# ── Simulated Annealing ───────────────────────────────────────────────────────
sa = simulated_annealing(N, INITIAL[:], T=30.0, cooling_rate=0.995, seed=42)
if sa is not None:
    print(f"[SA]   Result     : {sa}")
    print(f"[SA]   Conflicts  : {num_conflicts(sa)}")
else:
    print("[SA]   Returned None – check your implementation.")

print()

# ── Beam Search ───────────────────────────────────────────────────────────────
beam = beam_search(N, beam_width=6, seed=42)
if beam is not None:
    print(f"[BEAM] Result     : {beam}")
    print(f"[BEAM] Conflicts  : {num_conflicts(beam)}")
else:
    print("[BEAM] Returned None – check your implementation.")
