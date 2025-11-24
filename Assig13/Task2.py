# TASK 2 - ERROR HANDLING IN LEGACY CODE
# Given legacy code for calculating factorial with potential errors
def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


# REFACTORED CODE WITH ERROR HANDLING
with open("sample.txt", "w") as f:
    f.write("Hello, this is test data.")

import os
print("Current working directory:", os.getcwd())

with open("sample.txt", "w") as f:
    f.write("Hello from Python!")

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Unexpected error: {e}"

print("\nReading sample.txt:")
print(read_file("sample.txt"))
