
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import random as r
import time
import concurrent.futures as future

# Alias for time.perf_counter
pc = time.perf_counter

def sphere_volume(n, d):
    inside = 0
    for _ in range(n):
        point = [r.uniform(-1, 1) for _ in range(d)]
        if sum(x**2 for x in point) <= 1:
            inside += 1
    return (2 ** d) * (inside / n)

def hypersphere_exact(d):
    from math import pi, gamma
    return (pi ** (d / 2)) / gamma(d / 2 + 1)

def sphere_volume_parallel1(n, d, np):
    with future.ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, [n] * np, [d] * np))
    return sum(results) / np

def sphere_volume_parallel2(n, d, np):
    chunk_size = n // np
    with future.ProcessPoolExecutor(max_workers=np) as executor:
        results = list(executor.map(sphere_volume, [chunk_size] * np, [d] * np))
    return sum(results) / np

def main():
    n = 100000
    d1 = 11
    np = 10
    n2 = 1000000

    start = pc()
    for y in range(np):
        sphere_volume(n, d1)
    end = pc()
    print(f"Without parallelisation it took: {round(end - start, 2)} s")
    print("-" * 50)

 
    start = pc()
    sphere_volume_parallel1(n2, d1, np)
    end = pc()
    print(f"The execution time with parallellisering was: {round(end - start, 2)} s")
    print("-" * 50)

    start = pc()
    sphere_volume(n, d1)
    end = pc()
    print(f"With parallel computation it took : {round(end - start,2)} s")
    print("-" * 50)

    
    start = pc()
    sphere_volume_parallel2(n2, d1, np)
    end = pc()
    print(f"With parallel computation it took : {round(end - start,2)} s")
    print("-" * 50)

if __name__ == '__main__':
    main()

