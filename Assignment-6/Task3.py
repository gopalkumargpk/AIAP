"""Task3: Age group classification using different conditional approaches.

This module demonstrates three different approaches to age group classification:
1. Traditional nested if-elif-else conditionals
2. Match-case statement (Python 3.10+)
3. Dictionary-based mapping approach

Each approach is analyzed for readability, maintainability, and performance.
"""

from typing import Literal


AgeGroup = Literal["Infant", "Child", "Teen", "Young Adult", "Adult", "Senior"]


def classify_age_if_elif(age: int) -> AgeGroup:
    """Classify age into groups using nested if-elif-else conditionals.
    
    Args:
        age: The person's age in years (should be non-negative)
        
    Returns:
        The age group classification as a string
        
    Analysis:
    - Complexity: O(1) time as it uses simple comparisons
    - Pros: Explicit logic flow, familiar to most programmers
    - Cons: Can become unwieldy with many conditions
    - Edge cases: Handles negative ages by raising ValueError
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 2:
        return "Infant"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 35:
        return "Young Adult"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


def classify_age_match(age: int) -> AgeGroup:
    """Classify age using match-case statement (Python 3.10+).
    
    This demonstrates a more modern pattern matching approach.
    Note: Requires Python 3.10 or later.
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
        
    match age:
        case _ if age < 2:
            return "Infant"
        case _ if age < 13:
            return "Child"
        case _ if age < 20:
            return "Teen"
        case _ if age < 35:
            return "Young Adult"
        case _ if age < 65:
            return "Adult"
        case _:
            return "Senior"


# Dictionary-based approach using ranges
AGE_GROUPS = [
    (range(0, 2), "Infant"),
    (range(2, 13), "Child"),
    (range(13, 20), "Teen"),
    (range(20, 35), "Young Adult"),
    (range(35, 65), "Adult"),
    (range(65, 150), "Senior")  # Upper bound for practical purposes
]

def classify_age_dict(age: int) -> AgeGroup:
    """Classify age using dictionary/list-based lookup.
    
    This demonstrates a data-driven approach where age ranges
    are defined separately from the logic.
    
    Pros:
    - Separates data (ranges) from logic
    - Easy to modify ranges without changing code
    - More maintainable for many categories
    
    Cons:
    - Slightly more complex implementation
    - May be marginally slower due to iteration
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    for age_range, group in AGE_GROUPS:
        if age in age_range:
            return group
    return "Senior"  # Default for very high ages


def run_tests() -> None:
    """Verify implementations with test cases including edge cases."""
    test_cases = [
        (-1, ValueError),  # Should raise ValueError
        (0, "Infant"),
        (1, "Infant"),
        (2, "Child"),
        (12, "Child"),
        (13, "Teen"),
        (19, "Teen"),
        (20, "Young Adult"),
        (34, "Young Adult"),
        (35, "Adult"),
        (64, "Adult"),
        (65, "Senior"),
        (100, "Senior")
    ]
    
    implementations = [
        ("if-elif", classify_age_if_elif),
        ("match-case", classify_age_match),
        ("dictionary", classify_age_dict)
    ]
    
    for impl_name, func in implementations:
        print(f"\nTesting {impl_name} implementation:")
        for age, expected in test_cases:
            try:
                result = func(age)
                if expected is ValueError:
                    print(f"❌ Failed: age={age}, expected ValueError")
                elif result == expected:
                    print(f"✓ Passed: age={age} -> {result}")
                else:
                    print(f"❌ Failed: age={age}, got {result}, expected {expected}")
            except ValueError as e:
                if expected is ValueError:
                    print(f"✓ Passed: age={age} correctly raised ValueError")
                else:
                    print(f"❌ Failed: age={age} raised unexpected ValueError")


if __name__ == "__main__":
    # Demo with sample ages
    sample_ages = [1, 7, 15, 25, 45, 75]
    
    print("Sample classifications using different implementations:\n")
    for age in sample_ages:
        print(f"Age {age}:")
        print(f"  if-elif  : {classify_age_if_elif(age)}")
        print(f"  match    : {classify_age_match(age)}")
        print(f"  dict     : {classify_age_dict(age)}")
        print()
    
    # Run test suite
    print("\nRunning test suite...")
    run_tests()
