# Original code that causes IndexError
numbers = [1, 2, 3]
# print(numbers[5])  # This would raise IndexError: list index out of range

# Fixed code with safe access logic using try-except
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print(f"Error: Index 5 is out of range. List has {len(numbers)} elements (indices 0-{len(numbers)-1})")

# Alternative: Check bounds before accessing
numbers = [1, 2, 3]
index = 5
if 0 <= index < len(numbers):
    print(numbers[index])
else:
    print(f"Error: Index {index} is out of range. List has {len(numbers)} elements (indices 0-{len(numbers)-1})")

