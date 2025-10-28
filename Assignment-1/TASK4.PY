# ...existing code...
from typing import Union

def factorial_recursive(n: int) -> int:
    """Return n! computed recursively. Raises ValueError for n < 0."""
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """Return n! computed iteratively. Raises ValueError for n < 0."""
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_input() -> int:
    """Prompt the user for a non-negative integer, print and return its factorial."""
    while True:
        s = input("Enter a non-negative integer to compute its factorial: ").strip()
        try:
            n = int(s)
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    value = factorial_iterative(n)
    print(f"{n}! = {value}")
    return value

if __name__ == "__main__":
    factorial_input()
# ...existing code...