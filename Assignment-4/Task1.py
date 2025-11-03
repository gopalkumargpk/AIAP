def is_leap_year(year: int) -> bool:
	"""Return True if `year` is a leap year (Gregorian rules).

	Rules:
	- Every year divisible by 4 is a leap year,
	  except every year divisible by 100 is NOT a leap year,
	  except every year divisible by 400 IS a leap year.
	"""
	# Not divisible by 4 -> common year
	if year % 4 != 0:
		return False
	# Divisible by 4 but not by 100 -> leap year
	if year % 100 != 0:
		return True
	# Divisible by 100 -> leap only if divisible by 400
	return year % 400 == 0


if __name__ == "__main__":
	# Small self-checks
	test_cases = {
		2000: True,   # divisible by 400
		1900: False,  # divisible by 100 but not 400
		2004: True,   # divisible by 4
		2001: False,  # common year
		2400: True,   # divisible by 400
		1800: False,  # divisible by 100 but not 400
	}

	for year, expected in test_cases.items():
		result = is_leap_year(year)
		print(f"{year}: {result} (expected {expected})")
		assert result == expected, f"Test failed for {year}: got {result}, expected {expected}"

	print("All tests passed")

