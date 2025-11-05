def fibonacci_recursive(n: int) -> int:
    """
    Calculate the nth number in the Fibonacci sequence using recursion.
    
    The Fibonacci sequence is defined as:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n (int): The position in the Fibonacci sequence to calculate (n >= 0)
    
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    
    Time Complexity: O(2^n) - Exponential time complexity
    Space Complexity: O(n) - Due to recursive call stack
    
    Examples:
        >>> fibonacci_recursive(0)
        0
        >>> fibonacci_recursive(1)
        1
        >>> fibonacci_recursive(6)
        8  # Because the sequence is: 0, 1, 1, 2, 3, 5, 8
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base cases
    if n == 0:
        return 0  # First number in Fibonacci sequence
    elif n == 1:
        return 1  # Second number in Fibonacci sequence
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_optimized(n: int, memo: dict = None) -> int:
    """
    Calculate the nth number in the Fibonacci sequence using recursion with memoization.
    This is an optimized version that prevents redundant calculations.
    
    Args:
        n (int): The position in the Fibonacci sequence to calculate (n >= 0)
        memo (dict): Memoization dictionary to store previously calculated values
    
    Returns:
        int: The nth Fibonacci number
    
    Time Complexity: O(n) - Linear time complexity due to memoization
    Space Complexity: O(n) - For storing previously calculated values
    """
    # Initialize memoization dictionary if not provided
    if memo is None:
        memo = {}
    
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Check if value is already memoized
    if n in memo:
        return memo[n]
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case with memoization
    memo[n] = fibonacci_optimized(n - 1, memo) + fibonacci_optimized(n - 2, memo)
    return memo[n]


# Example usage and testing
def main():
    """
    Main function to demonstrate and test the Fibonacci functions.
    Includes example usage and performance comparison.
    """
    # Test cases
    test_cases = [0, 1, 5, 10]
    
    print("Testing recursive Fibonacci function:")
    print("-" * 40)
    
    for n in test_cases:
        try:
            result = fibonacci_recursive(n)
            print(f"F({n}) = {result}")
        except Exception as e:
            print(f"Error for n={n}: {str(e)}")
    
    print("\nTesting optimized Fibonacci function:")
    print("-" * 40)
    
    for n in test_cases:
        try:
            result = fibonacci_optimized(n)
            print(f"F({n}) = {result}")
        except Exception as e:
            print(f"Error for n={n}: {str(e)}")
    
    # Demonstrate error handling
    print("\nTesting error handling:")
    print("-" * 40)
    
    try:
        fibonacci_recursive(-1)
    except ValueError as e:
        print(f"Handled negative input: {str(e)}")
    
    try:
        fibonacci_recursive(1.5)
    except TypeError as e:
        print(f"Handled non-integer input: {str(e)}")


if __name__ == "__main__":
    main()