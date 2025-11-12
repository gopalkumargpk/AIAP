"""Calculator module with four basic operations and docstring comparison.

This module provides simple arithmetic helpers: ``add``, ``subtract``,
``multiply`` and ``divide``. Manual docstrings are written in NumPy style.
An example AI-generated module-level docstring and AI-generated function
docstrings are included as strings to compare programmatically.
"""

from typing import Union, Tuple
import difflib

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
	"""
	Add two numbers.

	Parameters
	----------
	a : int or float
		First addend.
	b : int or float
		Second addend.

	Returns
	-------
	float
		The sum of ``a`` and ``b``.

	Raises
	------
	TypeError
		If either ``a`` or ``b`` is not a number.

	Examples
	--------
	>>> add(1, 2)
	3.0
	"""
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("a and b must be numbers")
	return float(a + b)


def subtract(a: Number, b: Number) -> float:
	"""
	Subtract one number from another.

	Parameters
	----------
	a : int or float
		Minuend.
	b : int or float
		Subtrahend.

	Returns
	-------
	float
		The difference ``a - b``.

	Raises
	------
	TypeError
		If either argument is not numeric.
	"""
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("a and b must be numbers")
	return float(a - b)


def multiply(a: Number, b: Number) -> float:
	"""
	Multiply two numbers.

	Parameters
	----------
	a : int or float
		First factor.
	b : int or float
		Second factor.

	Returns
	-------
	float
		The product ``a * b``.

	Raises
	------
	TypeError
		If either argument is not numeric.
	"""
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("a and b must be numbers")
	return float(a * b)


def divide(a: Number, b: Number) -> float:
	"""
	Divide one number by another.

	Parameters
	----------
	a : int or float
		Dividend.
	b : int or float
		Divisor.

	Returns
	-------
	float
		The quotient ``a / b``.

	Raises
	------
	TypeError
		If either argument is not numeric.
	ValueError
		If ``b`` is zero.
	"""
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("a and b must be numbers")
	if b == 0:
		raise ValueError("division by zero")
	return float(a / b)


# --- Simulated AI-generated module-level and per-function docstrings ---
ai_module_doc = '''
Calculator utilities module.

Provides four functions that perform basic arithmetic: add, subtract,
multiply and divide. Functions accept numeric inputs (int or float) and
return float results. Division raises an error on zero divisor.
'''

ai_docstrings = {
	'add': '''Add two numeric values and return their sum.

Parameters
----------
a, b : number
	Operands to add.

Returns
-------
float
	Sum of a and b.
''',
	'subtract': '''Return the result of subtracting b from a.

Parameters
----------
a, b : number
	Numeric operands.

Returns
-------
float
	Difference a - b.
''',
	'multiply': '''Multiply two numbers and return the product.

Parameters
----------
a, b : number
	Values to multiply.

Returns
-------
float
	Product a * b.
''',
	'divide': '''Divide a by b and return the quotient.

Parameters
----------
a, b : number
	Dividend and divisor.

Returns
-------
float
	Quotient a / b.

Raises
------
ZeroDivisionError
	If b is zero.
''',
}


def compare_docstrings(manual: str, ai: str, label: str = "module") -> None:
	"""Print a comparison between manual and AI-generated docstrings.

	Shows both docstrings, simple character/word counts and a small unified
	diff to surface structural differences.
	"""
	print(f"--- Manual ({label}) docstring ---")
	print(manual.strip())
	print()
	print(f"--- AI ({label}) docstring ---")
	print(ai.strip())
	print()

	# Metrics
	def metrics(s: str) -> Tuple[int, int]:
		return len(s), len(s.split())

	m_chars, m_words = metrics(manual)
	a_chars, a_words = metrics(ai)
	print(f"Manual: {m_chars} chars, {m_words} words")
	print(f"AI:     {a_chars} chars, {a_words} words")
	print()

	# Unified diff
	m_lines = manual.strip().splitlines()
	a_lines = ai.strip().splitlines()
	diff = difflib.unified_diff(m_lines, a_lines, fromfile='manual', tofile='ai', lineterm='')
	print('--- Unified diff (manual -> ai) ---')
	for i, line in enumerate(diff):
		if i >= 60:
			print('... (diff truncated)')
			break
		print(line)


if __name__ == '__main__':
	# Demo values
	x, y = 12, 5
	print(f"Inputs: x={x}, y={y}")
	print('add:', add(x, y))
	print('subtract:', subtract(x, y))
	print('multiply:', multiply(x, y))
	print('divide:', divide(x, y))
	print('\nComparing module-level docstrings:\n')
	compare_docstrings(__doc__ or '', ai_module_doc, label='module')
	print('\nComparing function docstrings (manual -> ai):\n')
	for fn in ('add', 'subtract', 'multiply', 'divide'):
		manual_ds = globals()[fn].__doc__ or ''
		ai_ds = ai_docstrings.get(fn, '')
		print(f'## Function: {fn}')
		compare_docstrings(manual_ds, ai_ds, label=fn)
		print('\n')
