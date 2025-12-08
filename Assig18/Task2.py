def check_number(num):
    """Check if a number is positive, negative, or zero."""
    if num > 0:
        return "The number is positive"
    elif num < 0:
        return "The number is negative"
    else:
        return "The number is zero"


# Test with different inputs
test_inputs = [-5, 0, 7]

print("Python Output:")
for num in test_inputs:
    result = check_number(num)
    print(f"Input: {num} → Output: {result}")
