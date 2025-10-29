def calculate_sums(numbers):
    """
    Calculate the sum of odd and even numbers in a list.
    
    Args:
        numbers (list): List of integers to process
        
    Returns:
        tuple: (sum of even numbers, sum of odd numbers)
        
    Raises:
        TypeError: If the list contains non-numeric values
    """
    try:
        # Initialize sums for even and odd numbers
        even_sum = 0
        odd_sum = 0
        
        # Process each number in the list
        for num in numbers:
            # Check if the number is even using modulo operator
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
                
        return even_sum, odd_sum
    
    except TypeError:
        raise TypeError("List must contain only numbers")

def calculate_sums_comprehension(numbers):
    """
    Alternative implementation using list comprehension.
    
    Args:
        numbers (list): List of integers to process
        
    Returns:
        tuple: (sum of even numbers, sum of odd numbers)
    """
    try:
        # Calculate sums using list comprehension
        even_sum = sum(num for num in numbers if num % 2 == 0)
        odd_sum = sum(num for num in numbers if num % 2 != 0)
        
        return even_sum, odd_sum
    
    except TypeError:
        raise TypeError("List must contain only numbers")

def print_results(numbers, even_sum, odd_sum):
    """
    Print the results in a formatted way.
    
    Args:
        numbers (list): Original list of numbers
        even_sum (int): Sum of even numbers
        odd_sum (int): Sum of odd numbers
    """
    print(f"\nOriginal list: {numbers}")
    print(f"Even numbers sum: {even_sum}")
    print(f"Odd numbers sum: {odd_sum}")
    print(f"Total sum: {even_sum + odd_sum}")
    print("-" * 40)

def main():
    try:
        # Test case 1: Mixed numbers
        numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        even_sum1, odd_sum1 = calculate_sums(numbers1)
        print("Test 1: Mixed numbers")
        print_results(numbers1, even_sum1, odd_sum1)
        
        # Test case 2: Only even numbers
        numbers2 = [2, 4, 6, 8, 10]
        even_sum2, odd_sum2 = calculate_sums(numbers2)
        print("Test 2: Only even numbers")
        print_results(numbers2, even_sum2, odd_sum2)
        
        # Test case 3: Only odd numbers
        numbers3 = [1, 3, 5, 7, 9]
        even_sum3, odd_sum3 = calculate_sums(numbers3)
        print("Test 3: Only odd numbers")
        print_results(numbers3, even_sum3, odd_sum3)
        
        # Test case 4: Empty list
        numbers4 = []
        even_sum4, odd_sum4 = calculate_sums(numbers4)
        print("Test 4: Empty list")
        print_results(numbers4, even_sum4, odd_sum4)
        
        # Test case 5: Using list comprehension method
        numbers5 = [1, 2, 3, 4, 5]
        even_sum5, odd_sum5 = calculate_sums_comprehension(numbers5)
        print("Test 5: Using list comprehension")
        print_results(numbers5, even_sum5, odd_sum5)
        
        # Test case 6: Error handling
        invalid_list = [1, 2, "3", 4, 5]
        even_sum6, odd_sum6 = calculate_sums(invalid_list)
        
    except TypeError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    main()