"""Task1: Example class with constructor and display_details method.

This file defines a simple Person class with a constructor (__init__)
and a display_details() method that prints the object's fields.
"""

class Person:
	"""A simple person model.

	Attributes:
		name (str): Person's name.
		age (int): Person's age.
		email (str|None): Optional email address.
	"""

	def __init__(self, name: str, age: int, email: str | None = None):
		"""Initialize a Person.

		Args:
			name: The person's name.
			age: The person's age.
			email: Optional email address.
		"""
		self.name = name
		self.age = age
		self.email = email

	def display_details(self) -> None:
		"""Print the details of the person to stdout.

		This method intentionally prints in a readable multi-line format.
		"""
		print(f"Name : {self.name}")
		print(f"Age  : {self.age}")
		print(f"Email: {self.email if self.email is not None else 'N/A'}")


if __name__ == "__main__":
	# Demo runner: construct an instance and show details
	p = Person("Alice Example", 30, "alice@example.com")
	p.display_details()

