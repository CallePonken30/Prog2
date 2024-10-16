
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import random as r
import time

# Alias for time.perf_counter
pc = time.perf_counter

def sphere_volume(n, d):
    # Approximate the volume of a d-dimensional hypersphere
    inside = 0
    for _ in range(n):
        point = [r.uniform(-1, 1) for _ in range(d)]
        if sum(x**2 for x in point) <= 1:
            inside += 1
    return (2 ** d) * (inside / n)

def hypersphere_exact(d):
    from math import pi, gamma
    # Exact volume of a d-dimensional unit hypersphere
    return (pi ** (d / 2)) / gamma(d / 2 + 1)

def sphere_volume_parallel1(n, d, np):
    from concurrent.futures import ProcessPoolExecutor
    # Increase the number of samples per process for better accuracy
    n_per_process = n // np
    with ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, [n_per_process] * np, [d] * np))
    # Average the results from each process to get the final volume approximation
    return sum(results) / np

def sphere_volume_parallel2(n, d, np):
    from concurrent.futures import ProcessPoolExecutor
    # Split the total number of samples across processes
    chunk_size = n // np
    with ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, [chunk_size] * np, [d] * np))
    # Average the results from each process to get the final volume approximation
    return sum(results) / np

def main():
    n = 100000
    d = 11
    np = 8
    # Output results for verification
    print(f"Sequential volume approximation: {sphere_volume(n, d)}")
    print(f"Exact volume: {hypersphere_exact(d)}")
    print(f"Parallel volume approximation (method 1): {sphere_volume_parallel1(n, d, np)}")
    print(f"Parallel volume approximation (method 2): {sphere_volume_parallel2(n, d, np)}")

if __name__ == '__main__':
    main()
