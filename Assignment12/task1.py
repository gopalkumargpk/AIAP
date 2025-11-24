def linear_search(lst, target):
    """
    Performs linear search on a given list to find the index of the target value.
    
    Parameters:
        lst (list): List of elements to search within.
        target (any): Value to find in the list.
    
    Returns:
        int: Index of target if found, otherwise -1.
    """
    for index in range(len(lst)):
        if lst[index] == target:
            return index  # Return the position where found
    
    return -1  # Return -1 if not found


# Example usage
numbers = [10, 20, 30, 40, 50]
value = 30

result = linear_search(numbers, value)
if result != -1:
    print(f"Value {value} found at index {result}")
else:
    print("Value not found")
