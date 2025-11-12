"""task2.py

Demonstrates an `sru_student` class with manual comments and a simulated
AI-generated inline-comment version, then compares them.
"""
from typing import Any
import difflib


# MANUAL: Define the student class holding basic student info and fee state
class sru_student:
    # MANUAL: Initialize a student with name, roll number and hostel status
    def __init__(self, name: str, roll_no: int, hostel_status: bool, fee_due: float = 0.0) -> None:
        # MANUAL: store the student's name
        self.name = name
        # MANUAL: store the student's roll number
        self.roll_no = roll_no
        # MANUAL: boolean indicating whether student stays in hostel
        self.hostel_status = hostel_status
        # MANUAL: amount of fee currently due for the student
        self.fee_due = float(fee_due)

    # MANUAL: Update the fee (apply a payment or charge) and return the new due
    def fee_update(self, amount: float) -> float:
        # MANUAL: ensure amount is numeric
        if not isinstance(amount, (int, float)):
            # MANUAL: raise error on invalid input
            raise TypeError("amount must be a number")
        # MANUAL: apply the payment (positive amount reduces due, negative increases)
        self.fee_due -= float(amount)
        # MANUAL: return updated fee due
        return self.fee_due

    # MANUAL: Return a dictionary with student details for display or testing
    def display_details(self) -> dict:
        # MANUAL: prepare a details mapping
        details = {
            'name': self.name,
            'roll_no': self.roll_no,
            'hostel_status': self.hostel_status,
            'fee_due': self.fee_due,
        }
        # MANUAL: return the mapping
        return details


# --- Simulated AI-generated inline comments version (as a single string) ---
# AI: The AI tool was asked to add inline comments explaining each line/step.
ai_commented_code = '''
class sru_student:
    # AI: Constructor: set up the student object with provided values
    def __init__(self, name: str, roll_no: int, hostel_status: bool, fee_due: float = 0.0) -> None:
        # AI: save name parameter on the instance
        self.name = name
        # AI: save roll number on the instance
        self.roll_no = roll_no
        # AI: save hostel residency status on the instance
        self.hostel_status = hostel_status
        # AI: convert fee_due to float and store it
        self.fee_due = float(fee_due)

    # AI: Adjust the fee_due by subtracting the given amount (payment)
    def fee_update(self, amount: float) -> float:
        # AI: validate that amount is int or float
        if not isinstance(amount, (int, float)):
            # AI: raise TypeError if invalid
            raise TypeError("amount must be a number")
        # AI: subtract amount from fee_due (payment reduces what is owed)
        self.fee_due -= float(amount)
        # AI: return the updated amount owed
        return self.fee_due

    # AI: Build and return a dict summarizing student information
    def display_details(self) -> dict:
        details = {
            'name': self.name,
            'roll_no': self.roll_no,
            'hostel_status': self.hostel_status,
            'fee_due': self.fee_due,
        }
        # AI: return the constructed dictionary
        return details
'''


def compare_comments(manual_source: str, ai_source: str) -> None:
    """Compare manual comments and AI-style comments and print a short diff.

    The function prints both sources, simple counts, and a unified diff to
    highlight differences in wording and structure between the manual and AI
    inline comments.
    """
    print('--- Manual commented source (excerpt) ---')
    print(manual_source.strip())
    print()
    print('--- AI commented source (excerpt) ---')
    print(ai_source.strip())
    print()

    # Basic metrics
    def metrics(text: str):
        return len(text), len(text.split())

    m_chars, m_words = metrics(manual_source)
    a_chars, a_words = metrics(ai_source)
    print(f'Manual: {m_chars} chars, {m_words} words')
    print(f'AI:     {a_chars} chars, {a_words} words')
    print()

    # Produce a unified diff for visibility
    manual_lines = manual_source.strip().splitlines()
    ai_lines = ai_source.strip().splitlines()
    diff = difflib.unified_diff(manual_lines, ai_lines, fromfile='manual', tofile='ai', lineterm='')
    print('--- Unified diff (manual -> ai) ---')
    for i, line in enumerate(diff):
        if i >= 200:
            print('... (diff truncated)')
            break
        print(line)


if __name__ == '__main__':
    # MANUAL: create a student instance for demonstration
    student = sru_student('Alice', 101, True, fee_due=1500.0)
    # MANUAL: show initial details
    print('Initial details:', student.display_details())
    # MANUAL: apply a payment of 500
    new_due = student.fee_update(500)
    # MANUAL: show updated due and details
    print('After payment, fee_due =', new_due)
    print('Updated details:', student.display_details())
    print('\nNow comparing manual comments with AI-style comments:\n')

    # Build a manual-source excerpt from this file's manual-commented lines
    # For simplicity, we'll assemble the manual version from the class code above
    manual_source = '''
class sru_student:
    # MANUAL: Initialize a student with name, roll number and hostel status
    def __init__(self, name: str, roll_no: int, hostel_status: bool, fee_due: float = 0.0) -> None:
        # MANUAL: store the student's name
        self.name = name
        # MANUAL: store the student's roll number
        self.roll_no = roll_no
        # MANUAL: boolean indicating whether student stays in hostel
        self.hostel_status = hostel_status
        # MANUAL: amount of fee currently due for the student
        self.fee_due = float(fee_due)

    # MANUAL: Update the fee (apply a payment or charge) and return the new due
    def fee_update(self, amount: float) -> float:
        # MANUAL: ensure amount is numeric
        if not isinstance(amount, (int, float)):
            # MANUAL: raise error on invalid input
            raise TypeError("amount must be a number")
        # MANUAL: apply the payment (positive amount reduces due, negative increases)
        self.fee_due -= float(amount)
        # MANUAL: return updated fee due
        return self.fee_due

    # MANUAL: Return a dictionary with student details for display or testing
    def display_details(self) -> dict:
        # MANUAL: prepare a details mapping
        details = {
            'name': self.name,
            'roll_no': self.roll_no,
            'hostel_status': self.hostel_status,
            'fee_due': self.fee_due,
        }
        # MANUAL: return the mapping
        return details
'''

    # Now compare the manual excerpt with the AI-commented version
    compare_comments(manual_source, ai_commented_code)
