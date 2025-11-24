# Fibonacci Sequence with Positive Integer Validation

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# User input
try:
    n = int(input("Enter a positive integer: "))
    
    if n <= 0:
        print("Error: Please enter a number greater than 0.")
    else:
        result = fibonacci(n)
        print("Fibonacci sequence:", result)

except ValueError:
    print("Error: Invalid input. Please enter a positive integer only.")
