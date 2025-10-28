# ...existing code...
import math

def _is_prime_num(n: int) -> bool:
    """Check primality for a given integer n (helper)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True

def is_prime():
    """
    Ask the user for an integer, print whether it's prime, and return True/False.
    Example interaction:
      Enter an integer to check for primality: 17
      17 is prime.
    """
    while True:
        s = input("Enter an integer to check for primality: ").strip()
        try:
            n = int(s)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    result = _is_prime_num(n)
    print(f"{n} is {'prime' if result else 'not prime'}.")
    return result

if __name__ == "__main__":
    is_prime()
# ...existing code...