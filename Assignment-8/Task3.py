import re
from typing import Tuple

def is_sentence_palindrome(sentence):
    """
    Checks if a sentence is a palindrome, ignoring case, spaces, and punctuation.
    
    A palindrome reads the same forwards and backwards. This function ignores:
    - Case (uppercase/lowercase)
    - Spaces
    - Punctuation marks
    - Special characters
    
    Only alphanumeric characters are considered.
    
    Args:
        sentence: The input sentence to check
        
    Returns:
        bool: True if the sentence is a palindrome, False otherwise
        
    Raises:
        TypeError: If sentence is not a string
    """
    
    # Type validation
    if not isinstance(sentence, str):
        raise TypeError(f"Input must be a string, got {type(sentence).__name__}")
    
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    
    # Handle empty string or string with only non-alphanumeric characters
    if not cleaned:
        return True  # Empty string is considered a palindrome
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]


def check_palindrome_with_details(sentence):
    """
    Checks if a sentence is a palindrome and returns detailed information.
    
    Args:
        sentence: The input sentence to check
        
    Returns:
        dict: Dictionary containing:
            - is_palindrome: bool
            - original: original sentence
            - cleaned: cleaned sentence (alphanumeric only, lowercase)
            - reversed: reversed cleaned sentence
    """
    
    if not isinstance(sentence, str):
        raise TypeError(f"Input must be a string, got {type(sentence).__name__}")
    
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    reversed_text = cleaned[::-1]
    
    return {
        'is_palindrome': cleaned == reversed_text,
        'original': sentence,
        'cleaned': cleaned,
        'reversed': reversed_text
    }


# Comprehensive Test Cases
def run_tests():
    """Run all test cases for the is_sentence_palindrome function"""
    
    test_cases = [
        # CLASSIC PALINDROMES
        {
            "sentence": "A man a plan a canal Panama",
            "expected": True,
            "description": "Classic palindrome with spaces and case"
        },
        {
            "sentence": "race car",
            "expected": True,
            "description": "Simple two-word palindrome"
        },
        {
            "sentence": "racecar",
            "expected": True,
            "description": "Simple palindrome without spaces"
        },
        {
            "sentence": "Was it a car or a cat I saw?",
            "expected": True,
            "description": "Palindrome with punctuation and question mark"
        },
        {
            "sentence": "Madam, I'm Adam",
            "expected": True,
            "description": "Palindrome with punctuation and apostrophe"
        },
        {
            "sentence": "Never odd or even",
            "expected": True,
            "description": "Palindrome with multiple spaces"
        },
        {
            "sentence": "Do geese see God?",
            "expected": True,
            "description": "Palindrome question with punctuation"
        },
        {
            "sentence": "Was it a rat I saw?",
            "expected": True,
            "description": "Palindrome with spaces and punctuation"
        },
        {
            "sentence": "Able was I ere I saw Elba",
            "expected": True,
            "description": "Famous Napoleon palindrome"
        },
        {
            "sentence": "A Santa at NASA",
            "expected": True,
            "description": "Palindrome with proper nouns"
        },
        
        # CASE INSENSITIVITY TESTS
        {
            "sentence": "A",
            "expected": True,
            "description": "Single character"
        },
        {
            "sentence": "AA",
            "expected": True,
            "description": "Two identical letters"
        },
        {
            "sentence": "Aa",
            "expected": True,
            "description": "Two same letters, different case"
        },
        {
            "sentence": "AaBbAa",
            "expected": True,
            "description": "Mixed case palindrome"
        },
        {
            "sentence": "RaceCar",
            "expected": True,
            "description": "Mixed case without spaces"
        },
        
        # PUNCTUATION HANDLING
        {
            "sentence": "a-b-a",
            "expected": True,
            "description": "Palindrome with hyphens"
        },
        {
            "sentence": "a.b.a",
            "expected": True,
            "description": "Palindrome with dots"
        },
        {
            "sentence": "a,b,a",
            "expected": True,
            "description": "Palindrome with commas"
        },
        {
            "sentence": "a!b!a",
            "expected": True,
            "description": "Palindrome with exclamation marks"
        },
        {
            "sentence": "a/b/a",
            "expected": True,
            "description": "Palindrome with slashes"
        },
        {
            "sentence": "a@b@a",
            "expected": True,
            "description": "Palindrome with @ symbols"
        },
        
        # NUMERIC PALINDROMES
        {
            "sentence": "121",
            "expected": True,
            "description": "Numeric palindrome"
        },
        {
            "sentence": "12321",
            "expected": True,
            "description": "Longer numeric palindrome"
        },
        {
            "sentence": "1a2a1",
            "expected": True,
            "description": "Mixed alphanumeric palindrome"
        },
        {
            "sentence": "A1B1A",
            "expected": True,
            "description": "Mixed case alphanumeric palindrome"
        },
        
        # SPACES AND WHITESPACE
        {
            "sentence": "a b a",
            "expected": True,
            "description": "Palindrome with spaces between characters"
        },
        {
            "sentence": "  a b a  ",
            "expected": True,
            "description": "Palindrome with leading/trailing spaces"
        },
        {
            "sentence": "a   b   a",
            "expected": True,
            "description": "Palindrome with multiple spaces"
        },
        {
            "sentence": "a\tb\ta",
            "expected": True,
            "description": "Palindrome with tabs"
        },
        
        # EDGE CASES - EMPTY/MINIMAL
        {
            "sentence": "",
            "expected": True,
            "description": "Empty string"
        },
        {
            "sentence": " ",
            "expected": True,
            "description": "String with only spaces"
        },
        {
            "sentence": "   ",
            "expected": True,
            "description": "String with multiple spaces"
        },
        {
            "sentence": "!!??",
            "expected": True,
            "description": "String with only punctuation"
        },
        {
            "sentence": "!@#$%",
            "expected": True,
            "description": "String with special characters only"
        },
        
        # NON-PALINDROMES - SIMPLE
        {
            "sentence": "hello",
            "expected": False,
            "description": "Simple non-palindrome"
        },
        {
            "sentence": "abc",
            "expected": False,
            "description": "Simple three-letter non-palindrome"
        },
        {
            "sentence": "ab",
            "expected": False,
            "description": "Two-letter non-palindrome"
        },
        {
            "sentence": "world",
            "expected": False,
            "description": "Common word non-palindrome"
        },
        
        # NON-PALINDROMES - WITH SPACES/PUNCTUATION
        {
            "sentence": "hello world",
            "expected": False,
            "description": "Two-word non-palindrome"
        },
        {
            "sentence": "Hello, World!",
            "expected": False,
            "description": "Non-palindrome with punctuation and case"
        },
        {
            "sentence": "Not a palindrome",
            "expected": False,
            "description": "Multi-word non-palindrome"
        },
        {
            "sentence": "A man, a plan, a canal, Panama!",
            "expected": True,
            "description": "Classic palindrome with all punctuation variants"
        },
        {
            "sentence": "Almost",
            "expected": False,
            "description": "Almost palindrome but not quite"
        },
        
        # NUMERIC NON-PALINDROMES
        {
            "sentence": "123",
            "expected": False,
            "description": "Numeric non-palindrome"
        },
        {
            "sentence": "12345",
            "expected": False,
            "description": "Longer numeric non-palindrome"
        },
        
        # COMPLEX REAL-WORLD EXAMPLES
        {
            "sentence": "Desserts I stressed!",
            "expected": True,
            "description": "Complex palindrome with punctuation"
        },
        {
            "sentence": "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!",
            "expected": True,
            "description": "Extended palindrome with multiple elements"
        },
        {
            "sentence": "Was it a car or a cat I saw?",
            "expected": True,
            "description": "Question palindrome"
        },
        {
            "sentence": "Never a foot too far, even.",
            "expected": True,
            "description": "Palindrome with even letters"
        },
    ]
    
    invalid_test_cases = [
        {
            "input": None,
            "error_type": TypeError,
            "description": "None input"
        },
        {
            "input": 123,
            "error_type": TypeError,
            "description": "Integer input"
        },
        {
            "input": 12.34,
            "error_type": TypeError,
            "description": "Float input"
        },
        {
            "input": [],
            "error_type": TypeError,
            "description": "List input"
        },
        {
            "input": {},
            "error_type": TypeError,
            "description": "Dictionary input"
        },
        {
            "input": ('a', 'b', 'a'),
            "error_type": TypeError,
            "description": "Tuple input"
        },
    ]
    
    print("=" * 110)
    print("RUNNING IS_SENTENCE_PALINDROME TEST SUITE")
    print("=" * 110)
    
    valid_passed = 0
    valid_failed = 0
    invalid_passed = 0
    invalid_failed = 0
    
    # Test valid cases
    print("\n" + "=" * 110)
    print("VALID INPUT TESTS")
    print("=" * 110)
    
    for i, test in enumerate(test_cases, 1):
        sentence = test["sentence"]
        expected = test["expected"]
        description = test["description"]
        
        try:
            result = is_sentence_palindrome(sentence)
            details = check_palindrome_with_details(sentence)
            
            if result == expected:
                status = "✓ PASS"
                valid_passed += 1
            else:
                status = "✗ FAIL"
                valid_failed += 1
            
            # Display test result
            print(f"\n{status} | Test {i}")
            print(f"  Input:   {sentence!r}")
            print(f"  Cleaned: {details['cleaned']!r}")
            print(f"  Expected: {expected} | Got: {result} | {description}")
            
        except Exception as e:
            print(f"\n✗ FAIL | Test {i}")
            print(f"  Input: {sentence!r}")
            print(f"  Unexpected error: {type(e).__name__}: {e}")
            valid_failed += 1
    
    # Test invalid cases
    print("\n" + "=" * 110)
    print("INVALID INPUT TESTS (Should raise exceptions)")
    print("=" * 110)
    
    for i, test in enumerate(invalid_test_cases, 1):
        input_val = test["input"]
        expected_error = test["error_type"]
        description = test["description"]
        
        try:
            result = is_sentence_palindrome(input_val)
            print(f"\n✗ FAIL | Invalid Test {i}")
            print(f"  Input: {input_val!r}")
            print(f"  Expected {expected_error.__name__} but got result: {result}")
            print(f"  {description}")
            invalid_failed += 1
        except expected_error as e:
            print(f"\n✓ PASS | Invalid Test {i}")
            print(f"  Input: {input_val!r}")
            print(f"  Raised {expected_error.__name__}: {e}")
            print(f"  {description}")
            invalid_passed += 1
        except Exception as e:
            print(f"\n✗ FAIL | Invalid Test {i}")
            print(f"  Input: {input_val!r}")
            print(f"  Expected {expected_error.__name__} but got {type(e).__name__}: {e}")
            print(f"  {description}")
            invalid_failed += 1
    
    # Summary
    print("\n" + "=" * 110)
    print("TEST SUMMARY")
    print("=" * 110)
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
    
    print("=" * 110)


if __name__ == "__main__":
    run_tests()
