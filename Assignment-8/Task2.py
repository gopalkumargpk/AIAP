def assign_grade(score):
    """
    Assigns a letter grade based on a numeric score.
    
    Grading Scale:
        90-100: A
        80-89:  B
        70-79:  C
        60-69:  D
        < 60:   F
    
    Args:
        score: The numeric score to be graded
        
    Returns:
        str: The letter grade (A, B, C, D, or F)
        
    Raises:
        TypeError: If score is not a valid numeric type
        ValueError: If score is outside the valid range (0-100)
    """
    
    # Type validation
    if not isinstance(score, (int, float)):
        raise TypeError(f"Score must be a number, got {type(score).__name__}")
    
    # Check for NaN or infinity
    if isinstance(score, float):
        if score != score:  # NaN check
            raise ValueError("Score cannot be NaN")
        if score == float('inf') or score == float('-inf'):
            raise ValueError("Score cannot be infinity")
    
    # Range validation
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    
    # Assign grade based on score ranges
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:  # score < 60
        return 'F'


# Comprehensive Test Cases
def run_tests():
    """Run all test cases for the assign_grade function"""
    
    test_cases = [
        # VALID CASES - Normal Range Tests
        {"score": 95, "expected": 'A', "description": "Score in middle of A range"},
        {"score": 85, "expected": 'B', "description": "Score in middle of B range"},
        {"score": 75, "expected": 'C', "description": "Score in middle of C range"},
        {"score": 65, "expected": 'D', "description": "Score in middle of D range"},
        {"score": 45, "expected": 'F', "description": "Score in middle of F range"},
        
        # BOUNDARY CASES - Lower Boundaries
        {"score": 90, "expected": 'A', "description": "Lower boundary of A (90)"},
        {"score": 80, "expected": 'B', "description": "Lower boundary of B (80)"},
        {"score": 70, "expected": 'C', "description": "Lower boundary of C (70)"},
        {"score": 60, "expected": 'D', "description": "Lower boundary of D (60)"},
        {"score": 0, "expected": 'F', "description": "Lower boundary of F (0)"},
        
        # BOUNDARY CASES - Upper Boundaries
        {"score": 100, "expected": 'A', "description": "Upper boundary of A (100)"},
        {"score": 89, "expected": 'B', "description": "Upper boundary of B (89)"},
        {"score": 79, "expected": 'C', "description": "Upper boundary of C (79)"},
        {"score": 69, "expected": 'D', "description": "Upper boundary of D (69)"},
        {"score": 59, "expected": 'F', "description": "Upper boundary of F (59)"},
        
        # BOUNDARY CASES - Just Outside Valid Range
        {"score": 89.9, "expected": 'B', "description": "Just below A boundary (89.9)"},
        {"score": 79.9, "expected": 'C', "description": "Just below B boundary (79.9)"},
        {"score": 69.9, "expected": 'D', "description": "Just below C boundary (69.9)"},
        {"score": 59.9, "expected": 'F', "description": "Just below D boundary (59.9)"},
        
        # FLOATING POINT SCORES
        {"score": 92.5, "expected": 'A', "description": "Float score in A range"},
        {"score": 85.7, "expected": 'B', "description": "Float score in B range"},
        {"score": 73.2, "expected": 'C', "description": "Float score in C range"},
        {"score": 64.5, "expected": 'D', "description": "Float score in D range"},
        {"score": 55.3, "expected": 'F', "description": "Float score in F range"},
    ]
    
    invalid_test_cases = [
        # INVALID INPUTS - Type Errors
        {"score": "eighty", "error_type": TypeError, "description": "String input"},
        {"score": "95", "error_type": TypeError, "description": "Numeric string"},
        {"score": None, "error_type": TypeError, "description": "None input"},
        {"score": [], "error_type": TypeError, "description": "List input"},
        {"score": {}, "error_type": TypeError, "description": "Dict input"},
        {"score": (85,), "error_type": TypeError, "description": "Tuple input"},
        
        # INVALID INPUTS - Value Errors (Out of Range)
        {"score": -5, "error_type": ValueError, "description": "Negative score"},
        {"score": -100, "error_type": ValueError, "description": "Large negative score"},
        {"score": 105, "error_type": ValueError, "description": "Score above 100"},
        {"score": 150, "error_type": ValueError, "description": "Score way above 100"},
        {"score": -0.5, "error_type": ValueError, "description": "Negative float"},
        {"score": 100.1, "error_type": ValueError, "description": "Just above 100"},
        
        # SPECIAL FLOAT VALUES
        {"score": float('inf'), "error_type": ValueError, "description": "Infinity"},
        {"score": float('-inf'), "error_type": ValueError, "description": "Negative infinity"},
        {"score": float('nan'), "error_type": ValueError, "description": "NaN (Not a Number)"},
    ]
    
    print("=" * 100)
    print("RUNNING ASSIGN_GRADE TEST SUITE")
    print("=" * 100)
    
    valid_passed = 0
    valid_failed = 0
    invalid_passed = 0
    invalid_failed = 0
    
    # Test valid cases
    print("\n" + "=" * 100)
    print("VALID INPUT TESTS")
    print("=" * 100)
    
    for test in test_cases:
        score = test["score"]
        expected = test["expected"]
        description = test["description"]
        
        try:
            result = assign_grade(score)
            if result == expected:
                print(f"✓ PASS | Score: {score:6} | Expected: {expected} | Got: {result} | {description}")
                valid_passed += 1
            else:
                print(f"✗ FAIL | Score: {score:6} | Expected: {expected} | Got: {result} | {description}")
                valid_failed += 1
        except Exception as e:
            print(f"✗ FAIL | Score: {score:6} | Unexpected error: {type(e).__name__}: {e}")
            valid_failed += 1
    
    # Test invalid cases
    print("\n" + "=" * 100)
    print("INVALID INPUT TESTS (Should raise exceptions)")
    print("=" * 100)
    
    for test in invalid_test_cases:
        score = test["score"]
        expected_error = test["error_type"]
        description = test["description"]
        
        try:
            result = assign_grade(score)
            print(f"✗ FAIL | Input: {score!r:20} | Expected {expected_error.__name__} but got result: {result} | {description}")
            invalid_failed += 1
        except expected_error as e:
            print(f"✓ PASS | Input: {score!r:20} | Raised {expected_error.__name__}: {e} | {description}")
            invalid_passed += 1
        except Exception as e:
            print(f"✗ FAIL | Input: {score!r:20} | Expected {expected_error.__name__} but got {type(e).__name__}: {e} | {description}")
            invalid_failed += 1
    
    # Summary
    print("\n" + "=" * 100)
    print("TEST SUMMARY")
    print("=" * 100)
    total_valid = valid_passed + valid_failed
    total_invalid = invalid_passed + invalid_failed
    total_all = total_valid + total_invalid
    total_passed = valid_passed + invalid_passed
    total_failed = valid_failed + invalid_failed
    
    print(f"\nValid Input Tests:   {valid_passed}/{total_valid} passed")
    print(f"Invalid Input Tests: {invalid_passed}/{total_invalid} passed")
    print(f"\nTotal Tests:         {total_passed}/{total_all} passed")
    
    if total_failed == 0:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\n❌ {total_failed} test(s) failed")
    
    print("=" * 100)


if __name__ == "__main__":
    run_tests()
