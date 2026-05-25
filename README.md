# AI Assignment 03: Local Search Algorithms

Implement **four** local search algorithms to solve the classic **N-Queens** problem.

## The Problem

Place N queens on an N×N chessboard so that no two queens attack each other.  
A **state** is a list of N integers where `state[i]` is the row of the queen in column `i` (0-indexed).  
The **goal** is a state with **zero conflicts** (no two queens share a row or diagonal).

---

## Files

| File | Your role |
|---|---|
| `search.py` | **Edit this** — implement all four functions |
| `utils.py` | **Do not modify** — helper functions provided for you |
| `main.py` | **Do not modify** — demo runner |

---

## Functions to Implement (`search.py`)

### 1. `hill_climbing(N, initial_state)` → `list[int]`

**Steepest-Ascent Hill Climbing**

- At each step evaluate **all** neighbours and move to the one with the fewest conflicts.
- If the best neighbour is **not strictly better** than the current state, stop.
- Return the state at which you stopped (the local minimum).
- Use `get_neighbors(state)` from `utils.py` — it returns neighbours sorted by `(conflicts, state)` for deterministic tie-breaking.
- If the initial state already has 0 conflicts, return it immediately.

---

### 2. `random_restart_hc(N, max_restarts, seed=42)` → `(list[int], int)`

**Random-Restart Hill Climbing**

- Create one local RNG: `rng = random.Random(seed)`. Use it for **all** restarts — do **not** re-seed between restarts.
- For each restart: generate a random starting state with `random_state(N, rng)`, then run `hill_climbing`.
- Keep track of the best (lowest-conflict) result across all restarts.
- Return a **tuple** `(best_state, restart_index)` where `restart_index` is the **1-based** number of the restart that found `best_state`.
- If a 0-conflict state is found, stop immediately and return it.

---

### 3. `simulated_annealing(N, initial_state, T=30.0, cooling_rate=0.995, seed=42)` → `list[int]`

**Simulated Annealing**

- Create one local RNG: `rng = random.Random(seed)`.
- At each step pick one random neighbour via `random_neighbor(state, rng)`.
- Accept the neighbour if it is **better** (fewer conflicts).
- Otherwise accept it with probability `e^(−Δ/T)` where `Δ = new_conflicts − current_conflicts`.  
  Use `rng.random()` for the acceptance roll.
- After each step: `T = T * cooling_rate`. Stop when `T < 1e-3` or conflicts reach 0.
- Throughout the search keep track of the **best state** seen (fewest conflicts). Return that best state, **not** the final state.

---

### 4. `beam_search(N, beam_width=4, seed=42)` → `list[int]`

**Local Beam Search**

- Create one local RNG: `rng = random.Random(seed)`.
- **Initialise** the beam with `beam_width` random states using `random_state(N, rng)`.
- **Each step:**
  1. Generate **all** neighbours of **every** state currently in the beam.
  2. From the combined pool keep the `beam_width` states with the **fewest** conflicts.  
     Break ties by state tuple value for determinism.
  3. Update the running best state seen.
- **Stop** when any beam state reaches 0 conflicts **or** the best conflict count in the beam did not improve compared to the previous step.
- Return the **best state** seen across all steps (not just the final beam).

---

## Rules

- You **must** use the helpers from `utils.py`: `get_neighbors`, `random_neighbor`, `random_state`, `num_conflicts`.
- Do **not** call `random.seed()` globally — always use a **local** `random.Random(seed)` instance.
- A valid state is a `list` of N `int` values each in `[0, N-1]`.
- Do **not** modify `utils.py` or `main.py`.

## Testing Locally

```
python main.py
```

Good luck!
