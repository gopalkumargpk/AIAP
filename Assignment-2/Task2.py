def is_palindrome(string):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Check if the string reads the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

def main():
    # Get input from user
    text = input("Enter a string to check if it's a palindrome: ")
    
    # Check if it's a palindrome and print the result
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")

# Run the program
if __name__ == "__main__":
    main()