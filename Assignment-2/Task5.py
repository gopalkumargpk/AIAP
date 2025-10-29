def sum_of_squares(numbers):
    """
    Calculate the sum of squares for a sequence of numbers.
    
    Args:
        numbers (list/tuple): A sequence of numbers
        
    Returns:
        float: The sum of squares of all numbers
        
    Raises:
        TypeError: If input contains non-numeric values
    """
    try:
        # Using list comprehension and sum function
        return sum(num ** 2 for num in numbers)
    except TypeError:
        raise TypeError("All elements must be numbers")

def sum_of_squares_range(n):
    """
    Calculate the sum of squares from 1 to n.
    
    Args:
        n (int): The upper limit of the range
        
    Returns:
        int: The sum of squares from 1 to n
        
    Raises:
        ValueError: If n is less than 1
        TypeError: If n is not an integer
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 1:
        raise ValueError("Input must be greater than 0")
    
    # Using the mathematical formula: sum of squares = n(n+1)(2n+1)/6
    return (n * (n + 1) * (2 * n + 1)) // 6

def main():
    # Test cases
    try:
        # Test with a list of numbers
        numbers = [1, 2, 3, 4, 5]
        result1 = sum_of_squares(numbers)
        print(f"1. Sum of squares for {numbers}: {result1}")
        # 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55
        
        # Test with range function
        n = 5
        result2 = sum_of_squares_range(n)
        print(f"2. Sum of squares from 1 to {n}: {result2}")
        
        # Test with floating point numbers
        float_numbers = [1.5, 2.5, 3.5]
        result3 = sum_of_squares(float_numbers)
        print(f"3. Sum of squares for {float_numbers}: {result3}")
        # 1.5² + 2.5² + 3.5² = 2.25 + 6.25 + 12.25 = 20.75
        
        # Test error handling
        print("\nTesting error handling:")
        # Test with invalid input
        invalid_input = [1, 2, "3", 4, 5]
        result4 = sum_of_squares(invalid_input)
        print("This line won't be reached due to error")
        
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()