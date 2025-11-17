def divide_numbers(numerator, denominator):
    """
    Divide two numbers with proper error handling.
    
    This function performs division of two numbers and handles the case
    where division by zero is attempted. If division by zero occurs,
    it returns None and prints an error message.
    
    Args:
        numerator: The number to be divided (dividend)
        denominator: The number to divide by (divisor)
    
    Returns:
        float: The result of the division, or None if division by zero occurs
    
    Raises:
        No exceptions are raised; errors are handled internally
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print(f"Error: Cannot divide {numerator} by zero.")
        return None
    except TypeError:
        print(f"Error: Invalid input types. Both arguments must be numbers.")
        return None


# Example usage
result = divide_numbers(10, 0)
if result is not None:
    print(f"Result: {result}")
else:
    print("Division operation failed.")

# Valid division example
result = divide_numbers(10, 2)
if result is not None:
    print(f"Result: {result}")