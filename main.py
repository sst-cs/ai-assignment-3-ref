"""
Demo runner for AI Assignment 03 – Local Search (N-Queens).
Run:  python main.py
"""
import random
from utils import num_conflicts
from search import hill_climbing, simulated_annealing

N = 8
random.seed(0)
initial = [random.randint(0, N - 1) for _ in range(N)]

print(f"N = {N}")
print(f"Initial state    : {initial}")
print(f"Initial conflicts: {num_conflicts(initial)}\n")

hc = hill_climbing(N, initial[:])
if hc is not None:
    print(f"Hill Climbing result   : {hc}")
    print(f"Conflicts              : {num_conflicts(hc)}\n")
else:
    print("Hill Climbing returned None – check your implementation.\n")

sa = simulated_annealing(N, initial[:])
if sa is not None:
    print(f"Simulated Annealing result: {sa}")
    print(f"Conflicts                 : {num_conflicts(sa)}")
else:
    print("Simulated Annealing returned None – check your implementation.")
