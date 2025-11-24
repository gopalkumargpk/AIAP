# TASK 4 - INEFFICIENT LOOP REFACTORING
# LEGACY CODE
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for i in nums:
    squares.append(i * i)


# REFACTORED CODE
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x * x for x in nums]

print("Numbers:", nums)
print("Squares:", squares)
