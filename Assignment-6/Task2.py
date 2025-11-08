"""Task2: Print first 10 multiples of a number using different controlled loops.

This module provides several implementations that produce the first 10
multiples of a supplied integer. It includes:
 - a for-loop implementation (printing)
 - a while-loop implementation (printing)
 - a list-comprehension implementation (returns list)

It also contains a small analysis as comments and simple assertions to
validate correctness.
"""

from typing import List


def print_first_10_multiples_for(n: int) -> None:
    """Print the first 10 multiples of n using a for loop.

    Example output for n=3:
        3 x 1 = 3
        3 x 2 = 6
        ...
    Complexity: O(1) in space (constant), O(10) = O(1) time in terms of n
    because the number of iterations is fixed (10).
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def print_first_10_multiples_while(n: int) -> None:
    """Print the first 10 multiples of n using a while loop.

    This demonstrates a controlled loop where an external counter
    variable is incremented until the stop condition is reached.
    """
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1


def get_first_10_multiples_list(n: int) -> List[int]:
    """Return the first 10 multiples of n as a list (list comprehension).

    This variant does not print directly — it returns a list which is
    often more useful for testing and downstream processing.
    """
    return [n * i for i in range(1, 11)]


# Analysis (brief):
# - Correctness: All three implementations enumerate i from 1..10 and
#   multiply by n, so they produce identical sequences.
# - Edge cases: If n==0 the sequence is all zeros; if n<0 the sequence
#   is negative multiples — still valid. The functions accept any
#   integer; if a non-integer is passed Python will still multiply but
#   typing hints recommend integers.
# - Complexity: Each implementation does a fixed 10 iterations -> O(1)
#   time and constant extra space (except the list-returning variant
#   which uses O(10) space = O(1)).


def _run_basic_checks() -> None:
    """Simple assertions to validate core behavior."""
    assert get_first_10_multiples_list(1) == [1 * i for i in range(1, 11)]
    assert get_first_10_multiples_list(0) == [0] * 10
    assert get_first_10_multiples_list(3)[-1] == 30


if __name__ == "__main__":
    # Demo: run each implementation for n=7 and show output, plus run checks
    n_demo = 7
    print("-- Using for loop --")
    print_first_10_multiples_for(n_demo)
    print("\n-- Using while loop --")
    print_first_10_multiples_while(n_demo)
    print("\n-- Using list comprehension (returned list) --")
    print(get_first_10_multiples_list(n_demo))

    # Run assertions
    _run_basic_checks()
    print("\nAll assertions passed.")
