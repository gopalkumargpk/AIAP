def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test with different inputs
test_inputs = [5, 0]

print("Python Output:")
for num in test_inputs:
    result = factorial(num)
    print(f"Input: {num} → Output: Factorial = {result}")
