# ...existing code...
def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]

def reverse_input() -> str:
    """Prompt the user for a string, print and return its reverse."""
    s = input("Enter a string to reverse: ")
    rev = reverse_string(s)
    print(rev)
    return rev

if __name__ == "__main__":
    reverse_input()
# ...existing code...