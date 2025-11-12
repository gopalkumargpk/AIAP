from typing import List, Tuple
import difflib


def sum_even_odd(numbers: List[int]) -> Tuple[int, int]:
	"""
	Calculate the sums of even and odd integers in a list.

	This function iterates over the provided list of integers and returns
	two integers: the sum of all even numbers and the sum of all odd numbers.

	Args:
		numbers (List[int]): A list of integers to be summed. Non-integer
			elements will raise a TypeError.

	Returns:
		Tuple[int, int]: A tuple where the first element is the sum of even
			numbers and the second element is the sum of odd numbers.

	Raises:
		TypeError: If any element in `numbers` is not an int.

	Examples:
		>>> sum_even_odd([1, 2, 3, 4])
		(6, 4)
	"""
	if not isinstance(numbers, list):
		raise TypeError("numbers must be a list of integers")

	sum_even = 0
	sum_odd = 0
	for i, v in enumerate(numbers):
		if not isinstance(v, int):
			raise TypeError(f"element at index {i} is not an int: {v!r}")
		if v % 2 == 0:
			sum_even += v
		else:
			sum_odd += v
	return sum_even, sum_odd


# --- AI-generated docstring (example produced by an AI-assisted tool) ---
ai_docstring = '''
Compute sums of even and odd numbers from a list.

Given a list of numeric values, this function separates even and odd
integers and returns two totals: the total of evens and the total of odds.
The function expects integer inputs and will raise an error for other types.

Parameters
----------
numbers : list
	List of integers to evaluate.

Returns
-------
tuple
	(sum_even, sum_odd) where sum_even is the sum of even integers and
	sum_odd is the sum of odd integers.
'''


def compare_docstrings(manual: str, ai: str) -> None:
	"""Print a brief comparison between two docstrings.

	The comparison shows both docstrings, a simple length/word-count
	summary, whether common sections (Args/Parameters/Returns) exist,
	and a small line-by-line diff.
	"""
	print("--- Manual (Google-style) docstring ---")
	print(manual.strip())
	print()
	print("--- AI-generated docstring ---")
	print(ai.strip())
	print()

	# Basic metrics
	def metrics(text: str):
		words = text.split()
		return len(text), len(words)

	m_chars, m_words = metrics(manual)
	a_chars, a_words = metrics(ai)
	print(f"Manual: {m_chars} chars, {m_words} words")
	print(f"AI:     {a_chars} chars, {a_words} words")
	print()

	# Check for common sections
	def has_section(text: str, markers):
		lower = text.lower()
		return any(m.lower() in lower for m in markers)

	print("Contains 'Args' or 'Parameters' section:",
		  has_section(manual, ["Args:", "Parameters"]))
	print("Contains 'Returns' section:", has_section(manual, ["Returns:", "Returns\n", "Returns:"]))
	print("AI contains 'Args' or 'Parameters':", has_section(ai, ["Args:", "Parameters"]))
	print("AI contains 'Returns' section:", has_section(ai, ["Returns:", "Returns\n"]))
	print()

	# Small line diff
	manual_lines = manual.strip().splitlines()
	ai_lines = ai.strip().splitlines()
	diff = difflib.unified_diff(manual_lines, ai_lines, fromfile='manual', tofile='ai', lineterm='')
	print('--- Short unified diff (manual -> ai) ---')
	for i, line in enumerate(diff):
		# limit output to first 40 lines of diff to keep output small
		if i >= 40:
			print('... (diff truncated)')
			break
		print(line)


if __name__ == '__main__':
	# Demo input and verification run
	sample = [1, 2, 3, 4, 5, 6]
	evens, odds = sum_even_odd(sample)
	print(f"Sample: {sample}")
	print(f"Sum of evens: {evens}, sum of odds: {odds}")
	print()
	# Compare the docstrings
	compare_docstrings(sum_even_odd.__doc__ or "", ai_docstring)
