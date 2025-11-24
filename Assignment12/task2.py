def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.
    
    Parameters:
        arr (list): The list of values to be sorted.
    
    Returns:
        list: A new sorted list.
    """
    n = len(arr)
    sorted_arr = arr.copy()  # To avoid modifying the original list

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


# Example usage
data = [5, 1, 4, 2, 8]

sorted_data = bubble_sort(data)
print("Original List:", data)
print("Sorted List:", sorted_data)

# Checking whether sorted correctly
print("Is sorted correctly?", sorted_data == sorted(data))
