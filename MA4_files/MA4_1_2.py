
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
from functools import reduce

def sphere_volume(n, d):

    inside_count = sum(
        1 for _ in range(n)
        if sum(map(lambda x: x**2, [r.uniform(-1, 1) for _ in range(d)])) <= 1
    )
    

    volume_estimate = (2 ** d) * (inside_count / n)
    
    return volume_estimate

def hypersphere_exact(n, d):
    exact_volume = (m.pi ** (d / 2)) / m.gamma(d / 2 + 1)
    return exact_volume

def main():
    cases = [(100000, 2), (100000, 11)]
    
    for n, d in cases:
        approx_volume = sphere_volume(n, d)
        exact_volume = hypersphere_exact(n, d)

        print(f"Approximation of V_{d}(1) with n={n}: {approx_volume}")
        print(f"Exact value of V_{d}(1): {exact_volume}")
        print("-" * 40)

if __name__ == '__main__':
	main()
