def cm_to_inches(cm: float, ndigits: int = 3) -> float:
	"""Convert centimeters to inches.

	Parameters
	- cm: length in centimeters (int or float)
	- ndigits: number of decimal places to round the result to (default 3)

	Returns the length in inches, rounded to `ndigits` decimals.

	Example: cm_to_inches(10) -> 3.937
	"""
	if not isinstance(cm, (int, float)):
		raise TypeError("cm must be a number")

	inches = cm / 2.54
	return round(inches, ndigits)


if __name__ == "__main__":
	# Example from the prompt
	value_cm = 10
	converted = cm_to_inches(value_cm)
	print(f"{value_cm} cm = {converted} inches")  # expected: 10 cm = 3.937 inches

	# Simple assertion to verify behavior
	assert cm_to_inches(10) == 3.937, "Expected 10 cm to be 3.937 inches"
	print("All tests passed")

def cm_to_inches(cm: float, ndigits: int = 3) -> float:
    """Convert centimeters to inches and round to `ndigits` decimals."""
    if not isinstance(cm, (int, float)):
        raise TypeError("cm must be a number")
    inches = cm / 2.54
    return round(inches, ndigits)

# Example
print(cm_to_inches(10))  # prints: 3.937