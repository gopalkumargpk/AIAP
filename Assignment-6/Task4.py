"""Task4: Calculate sum of first n numbers using different approaches.

This module implements sum_to_n(n) using different techniques:
1. Iterative (for loop)
2. Recursive
3. Mathematical formula (n * (n + 1) / 2)
4. While loop
5. Reduce function

Each implementation is analyzed for performance and demonstrated
with benchmarking.
"""

from functools import reduce
from time import perf_counter
from typing import Callable, List


def sum_to_n_loop(n: int) -> int:
    """Calculate sum of first n numbers using a for loop.
    
    Args:
        n: A non-negative integer
        
    Returns:
        Sum of numbers from 1 to n inclusive
        
    Raises:
        ValueError: If n is negative
        
    Analysis:
    - Time Complexity: O(n) - must visit each number
    - Space Complexity: O(1) - only uses a single sum variable
    - Pros: Simple to understand, works for small to medium n
    - Cons: Linear time complexity, slower for large n
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_formula(n: int) -> int:
    """Calculate sum using mathematical formula: n * (n + 1) / 2.
    
    Analysis:
    - Time Complexity: O(1) - constant time regardless of n
    - Space Complexity: O(1) - uses fixed number of variables
    - Pros: Fastest possible solution, works for very large n
    - Cons: May have floating point precision issues for huge n
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    return n * (n + 1) // 2  # Using // for integer division


def sum_to_n_recursive(n: int) -> int:
    """Calculate sum using recursion: sum(n) = n + sum(n-1).
    
    Analysis:
    - Time Complexity: O(n) - makes n recursive calls
    - Space Complexity: O(n) - uses call stack space
    - Pros: Elegant mathematical definition
    - Cons: Stack overflow for large n, space inefficient
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0
    return n + sum_to_n_recursive(n - 1)


def sum_to_n_while(n: int) -> int:
    """Calculate sum using a while loop.
    
    Analysis:
    - Time Complexity: O(n) - must visit each number
    - Space Complexity: O(1) - uses fixed variables
    - Pros: Demonstrates explicit loop control
    - Cons: Same performance as for loop but more verbose
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def sum_to_n_reduce(n: int) -> int:
    """Calculate sum using reduce() function.
    
    Analysis:
    - Time Complexity: O(n) - must visit each number
    - Space Complexity: O(n) - creates range object
    - Pros: Functional programming style
    - Cons: Less readable, same performance as loop
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    return reduce(lambda x, y: x + y, range(1, n + 1), 0)


def benchmark(func: Callable[[int], int], n: int, iterations: int = 1000) -> float:
    """Measure average execution time of function over multiple iterations."""
    start = perf_counter()
    for _ in range(iterations):
        func(n)
    end = perf_counter()
    return (end - start) / iterations


def run_tests() -> None:
    """Verify implementations with test cases."""
    test_cases = [
        (0, 0),
        (1, 1),
        (5, 15),
        (10, 55),
        (100, 5050)
    ]
    
    implementations = [
        ("Loop", sum_to_n_loop),
        ("Formula", sum_to_n_formula),
        ("Recursive", sum_to_n_recursive),
        ("While", sum_to_n_while),
        ("Reduce", sum_to_n_reduce)
    ]
    
    # Correctness tests
    print("Running correctness tests...")
    for name, func in implementations:
        print(f"\nTesting {name} implementation:")
        for n, expected in test_cases:
            result = func(n)
            print(f"n={n}: {'✓' if result == expected else '❌'} "
                  f"(got {result}, expected {expected})")
            
        # Test negative input
        try:
            func(-1)
            print("❌ Failed to raise ValueError for negative input")
        except ValueError:
            print("✓ Correctly handled negative input")
    
    # Performance benchmark
    print("\nRunning performance benchmark...")
    test_n = 1000
    iterations = 1000
    
    results: List[tuple[str, float]] = []
    for name, func in implementations:
        if name != "Recursive":  # Skip recursive for large n
            time = benchmark(func, test_n, iterations)
            results.append((name, time))
    
    # Sort by time and display
    results.sort(key=lambda x: x[1])
    print(f"\nAverage time over {iterations} iterations with n={test_n}:")
    fastest = results[0][1]
    for name, time in results:
        print(f"{name:8} : {time*1e6:8.2f} µs "
              f"({time/fastest:6.2f}x vs fastest)")


if __name__ == "__main__":
    # Quick demo of each implementation
    n_demo = 5
    print(f"Calculating sum to {n_demo} using different methods:")
    print(f"Loop     : {sum_to_n_loop(n_demo)}")
    print(f"Formula  : {sum_to_n_formula(n_demo)}")
    print(f"Recursive: {sum_to_n_recursive(n_demo)}")
    print(f"While    : {sum_to_n_while(n_demo)}")
    print(f"Reduce   : {sum_to_n_reduce(n_demo)}")
    
    print("\n=== Tests and Benchmarks ===")
    run_tests()
