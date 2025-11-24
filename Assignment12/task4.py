def f(x):
    return x**2 + 4*x + 5

def df(x):
    return 2*x + 4

def gradient_descent(learning_rate=0.01, iterations=1000, initial_x=0.0):
    x = initial_x
    for i in range(iterations):
        grad = df(x)
        x = x - learning_rate * grad
    return x

if __name__ == "__main__":
    min_x = gradient_descent(learning_rate=0.01, iterations=1000, initial_x=0.0)
    print(f"Value of x where f(x) is minimum (approx): {min_x:.6f}")
    print(f"Minimum value of f(x) (approx): {f(min_x):.6f}")
