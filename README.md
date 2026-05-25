# AI Assignment 03: Local Search Algorithms

In this assignment you will implement two **local search** algorithms to solve the classic **N-Queens problem**.

## The Problem

Place N queens on an N×N chessboard so that no two queens attack each other.  
A **state** is a list of N integers where `state[i]` is the row of the queen in column `i` (0-indexed).  
The **goal** is a state with **zero conflicts**.

## Your Task

Open `search.py` and implement:

### 1. `hill_climbing(N, initial_state)` — Steepest-Ascent Hill Climbing
- At each step evaluate **all** neighbours and move to the one with the fewest conflicts.
- If no neighbour strictly improves the current state, **stop** and return the current state.
- Use `get_neighbors(state)` from `utils.py` — it already returns neighbours sorted by `(conflicts, state)` for **deterministic tie-breaking**.

### 2. `simulated_annealing(N, initial_state, T=30.0, cooling_rate=0.995, seed=42)` — Simulated Annealing
- Use `random.Random(seed)` as a **local** RNG — do **not** call `random.seed()` globally.
- At each step pick a random neighbour via `random_neighbor(state, rng)` from `utils.py`.
- Accept the neighbour if it is better; otherwise accept it with probability `e^(-Δ/T)`.
- After each step multiply temperature: `T = T * cooling_rate`. Stop when `T < 1e-3`.
- Track and return the **best state seen** throughout the entire search.

## Rules & Guidelines
- You **must** use `get_neighbors` and `random_neighbor` from `utils.py`. Do not modify `utils.py` or `main.py`.
- A valid state is a `list` of N integers each in `[0, N-1]`.
- If the initial state already has 0 conflicts, return it immediately.

## Testing Locally
```
python main.py
```

Good luck!
