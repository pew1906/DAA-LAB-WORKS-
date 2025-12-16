# Assignment 09: Simulated Annealing for Scheduling (Makespan)

import random
import math
import numpy as np
import matplotlib.pyplot as plt

def generate_jobs(n, min_time=1, max_time=100, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    return [random.randint(min_time, max_time) for _ in range(n)]

def initial_solution(n, m, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.randrange(m) for _ in range(n)]

def makespan(assignment, jobs, m):
    loads = [0]*m
    for j_idx, machine in enumerate(assignment):
        loads[machine] += jobs[j_idx]
    return max(loads), loads

def neighbor_swap(assignment, m):
    n = len(assignment)
    new_assign = assignment.copy()
    i = random.randrange(n)
    new_machine = random.randrange(m)
    # ensure change
    while new_machine == new_assign[i] and m > 1:
        new_machine = random.randrange(m)
    new_assign[i] = new_machine
    return new_assign

def neighbor_swap_two_jobs(assignment):
    new_assign = assignment.copy()
    n = len(assignment)
    i, j = random.sample(range(n), 2)
    new_assign[i], new_assign[j] = new_assign[j], new_assign[i]
    return new_assign

def acceptance_probability(old_cost, new_cost, temp):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temp)

def simulated_annealing(jobs, m,
                        t0=1000.0, alpha=0.995,  
                        iterations_per_temp=200,
                        min_temp=1e-3,
                        max_iters=20000,
                        neighbor_fn=neighbor_swap,
                        seed=None,
                        verbose=False):

    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    n = len(jobs)

    current = initial_solution(n, m, seed=seed)
    current_cost, current_loads = makespan(current, jobs, m)
    best = current.copy()
    best_cost = current_cost
    temp = t0

    history = []  
    evals = 0

    while temp > min_temp and evals < max_iters:
        for _ in range(iterations_per_temp):
            neighbor = neighbor_fn(current, m) if neighbor_fn == neighbor_swap else neighbor_fn(current)
            new_cost, _ = makespan(neighbor, jobs, m)
            ap = acceptance_probability(current_cost, new_cost, temp)
            if random.random() < ap:
                current = neighbor
                current_cost = new_cost
            if current_cost < best_cost:
                best = current.copy()
                best_cost = current_cost
            history.append(best_cost)
            evals += 1
            if evals >= max_iters:
                break
        temp *= alpha
        if verbose:
            print(f"Temp: {temp:.4f}, Best cost: {best_cost}, Current cost: {current_cost}")
    return {
        "best_assignment": best,
        "best_cost": best_cost,
        "history": history,
        "evaluations": evals
    }

if __name__ == "__main__":
    n_jobs = 200
    m_machines = 8
    seed = 42

    jobs = generate_jobs(n_jobs, min_time=1, max_time=200, seed=seed)
    print(f"Generated {n_jobs} jobs. Sample processing times: {jobs[:10]} ...")

    result1 = simulated_annealing(
        jobs, m_machines,
        t0=500.0, alpha=0.995,
        iterations_per_temp=300,
        min_temp=1e-3,
        max_iters=50000,
        neighbor_fn=neighbor_swap,
        seed=seed,
        verbose=False
    )

    result2 = simulated_annealing(
        jobs, m_machines,
        t0=500.0, alpha=0.995,
        iterations_per_temp=300,
        min_temp=1e-3,
        max_iters=50000,
        neighbor_fn=neighbor_swap_two_jobs,
        seed=seed+1,
        verbose=False
    )

    print("\n--- Results ---")
    print(f"Best makespan (move-one-job): {result1['best_cost']}")
    print(f"Best makespan (swap-two-jobs): {result2['best_cost']}")

    plt.figure(figsize=(10, 5))
    plt.plot(result1['history'], label='move-one-job neighbor')
    plt.plot(result2['history'], label='swap-two-jobs neighbor', alpha=0.7)
    plt.xlabel('Iteration')
    plt.ylabel('Best makespan found so far')
    plt.title('Simulated Annealing Convergence for Scheduling (Makespan)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    best_assign = result1['best_assignment']
    _, loads = makespan(best_assign, jobs, m_machines)
    print("\nFinal machine loads for the best (move-one-job) solution:")
    for i, load in enumerate(loads):
        print(f" Machine {i}: load = {load}")
