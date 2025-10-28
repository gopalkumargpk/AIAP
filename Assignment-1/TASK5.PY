# ...existing code...
import re
from typing import List

def max_in_list(nums: List[float]) -> float:
    if not nums:
        raise ValueError("max_in_list() arg is an empty list")
    max_val = nums[0]
    for v in nums[1:]:
        if v > max_val:
            max_val = v
    return max_val

def max_input() -> float:
    while True:
        s = input("Enter numbers separated by spaces or commas: ").strip()
        if not s:
            print("Please enter at least one number.")
            continue
        parts = re.split(r'[,\s]+', s)
        try:
            nums = [float(p) for p in parts if p != ""]
            if not nums:
                print("Please enter at least one number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter only numbers.")
    maxv = max_in_list(nums)
    if all(x.is_integer() for x in nums):
        print(f"Largest number: {int(maxv)}")
    else:
        print(f"Largest number: {maxv}")
    return maxv

if __name__ == "__main__":
    max_input()
# ...existing code...