import re
from datetime import datetime


def convert_date_format(date_str):
    """
    Converts a date string from "YYYY-MM-DD" format to "DD-MM-YYYY" format.
    
    This function validates the input date format and ensures the date is valid
    before converting it.
    
    Args:
        date_str (str): The date string in "YYYY-MM-DD" format
        
    Returns:
        str: The date string in "DD-MM-YYYY" format
        
    Raises:
        TypeError: If date_str is not a string
        ValueError: If date_str is not in correct format or is an invalid date
    """
    
    # Type validation
    if not isinstance(date_str, str):
        raise TypeError(f"Date must be a string, got {type(date_str).__name__}")
    
    # Check if string is empty
    if not date_str or not date_str.strip():
        raise ValueError("Date string cannot be empty")
    
    date_str = date_str.strip()
    
    # Check format with regex: YYYY-MM-DD
    format_pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
    match = re.match(format_pattern, date_str)
    
    if not match:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD', got '{date_str}'")
    
    year, month, day = match.groups()
    
    # Convert to integers for validation
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    
    # Validate month
    if month_int < 1 or month_int > 12:
        raise ValueError(f"Invalid month: {month_int}. Month must be between 01 and 12")
    
    # Validate year (basic check - should be reasonable year range)
    if year_int < 1 or year_int > 9999:
        raise ValueError(f"Invalid year: {year_int}. Year must be between 1 and 9999")
    
    # Validate day based on month
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if leap year
    is_leap = (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0)
    if is_leap:
        days_in_month[1] = 29  # February has 29 days in leap year
    
    max_day = days_in_month[month_int - 1]
    
    if day_int < 1 or day_int > max_day:
        raise ValueError(f"Invalid day: {day_int}. Day must be between 01 and {max_day} for month {month_int}")
    
    # Valid date - convert format
    return f"{day}-{month}-{year}"


def validate_and_convert(date_str):
    """
    Validates and converts date format, returning detailed information.
    
    Args:
        date_str (str): The date string in "YYYY-MM-DD" format
        
    Returns:
        dict: Dictionary containing:
            - original: original input
            - converted: converted date string
            - is_valid: boolean validation result
            - error: error message if any
    """
    try:
        converted = convert_date_format(date_str)
        return {
            'original': date_str,
            'converted': converted,
            'is_valid': True,
            'error': None
        }
    except (TypeError, ValueError) as e:
        return {
            'original': date_str,
            'converted': None,
            'is_valid': False,
            'error': str(e)
        }


# Comprehensive Test Cases
def run_tests():
    """Run all test cases for the convert_date_format function"""
    
    print("=" * 120)
    print("RUNNING CONVERT_DATE_FORMAT TEST SUITE")
    print("=" * 120)
    
    test_cases = [
        # VALID DATES - BASIC CONVERSIONS
        {
            "input": "2023-10-15",
            "expected": "15-10-2023",
            "description": "Example from requirements"
        },
        {
            "input": "2024-01-01",
            "expected": "01-01-2024",
            "description": "New Year's Day 2024"
        },
        {
            "input": "2000-12-31",
            "expected": "31-12-2000",
            "description": "Last day of year 2000"
        },
        {
            "input": "1999-01-01",
            "expected": "01-01-1999",
            "description": "Year 1999"
        },
        
        # VALID DATES - LEAP YEAR TESTING
        {
            "input": "2024-02-29",
            "expected": "29-02-2024",
            "description": "Leap day in leap year 2024"
        },
        {
            "input": "2000-02-29",
            "expected": "29-02-2000",
            "description": "Leap day in year 2000 (divisible by 400)"
        },
        {
            "input": "2020-02-29",
            "expected": "29-02-2020",
            "description": "Leap day in year 2020"
        },
        
        # VALID DATES - NON-LEAP YEAR
        {
            "input": "2023-02-28",
            "expected": "28-02-2023",
            "description": "Last day of February in non-leap year"
        },
        {
            "input": "2100-02-28",
            "expected": "28-02-2100",
            "description": "Year 2100 (not leap, divisible by 100 but not 400)"
        },
        
        # VALID DATES - VARIOUS MONTHS
        {
            "input": "2023-01-31",
            "expected": "31-01-2023",
            "description": "January (31 days)"
        },
        {
            "input": "2023-04-30",
            "expected": "30-04-2023",
            "description": "April (30 days)"
        },
        {
            "input": "2023-06-30",
            "expected": "30-06-2023",
            "description": "June (30 days)"
        },
        {
            "input": "2023-09-30",
            "expected": "30-09-2023",
            "description": "September (30 days)"
        },
        {
            "input": "2023-11-30",
            "expected": "30-11-2023",
            "description": "November (30 days)"
        },
        
        # VALID DATES - EDGE CASES FOR DAYS
        {
            "input": "2023-03-01",
            "expected": "01-03-2023",
            "description": "First day of month"
        },
        {
            "input": "2023-12-01",
            "expected": "01-12-2023",
            "description": "December first"
        },
        {
            "input": "2023-07-15",
            "expected": "15-07-2023",
            "description": "Mid-month date"
        },
        
        # VALID DATES - HISTORICAL DATES
        {
            "input": "1900-01-01",
            "expected": "01-01-1900",
            "description": "Year 1900"
        },
        {
            "input": "1970-01-01",
            "expected": "01-01-1970",
            "description": "Unix epoch date"
        },
        {
            "input": "2001-09-11",
            "expected": "11-09-2001",
            "description": "Historical date"
        },
        
        # VALID DATES - FUTURE DATES
        {
            "input": "2099-12-31",
            "expected": "31-12-2099",
            "description": "Far future date"
        },
        {
            "input": "2050-06-15",
            "expected": "15-06-2050",
            "description": "Mid-century future date"
        },
        
        # VALID DATES - SINGLE DIGIT MONTH/DAY WITH LEADING ZERO
        {
            "input": "2023-01-05",
            "expected": "05-01-2023",
            "description": "Single digit month and day"
        },
        {
            "input": "2023-09-09",
            "expected": "09-09-2023",
            "description": "Double digit single values"
        },
    ]
    
    invalid_test_cases = [
        # TYPE ERRORS
        {
            "input": None,
            "error_type": TypeError,
            "description": "None input"
        },
        {
            "input": 20231015,
            "error_type": TypeError,
            "description": "Integer input"
        },
        {
            "input": 2023.10,
            "error_type": TypeError,
            "description": "Float input"
        },
        {
            "input": ['2023', '10', '15'],
            "error_type": TypeError,
            "description": "List input"
        },
        {
            "input": {'year': 2023, 'month': 10, 'day': 15},
            "error_type": TypeError,
            "description": "Dictionary input"
        },
        {
            "input": ('2023', '10', '15'),
            "error_type": TypeError,
            "description": "Tuple input"
        },
        
        # EMPTY/WHITESPACE ERRORS
        {
            "input": "",
            "error_type": ValueError,
            "description": "Empty string"
        },
        {
            "input": "   ",
            "error_type": ValueError,
            "description": "Whitespace only"
        },
        
        # FORMAT ERRORS - WRONG SEPARATORS
        {
            "input": "2023/10/15",
            "error_type": ValueError,
            "description": "Wrong separator (/) instead of (-)"
        },
        {
            "input": "2023.10.15",
            "error_type": ValueError,
            "description": "Wrong separator (.) instead of (-)"
        },
        {
            "input": "2023 10 15",
            "error_type": ValueError,
            "description": "Spaces instead of dashes"
        },
        {
            "input": "20231015",
            "error_type": ValueError,
            "description": "No separators"
        },
        
        # FORMAT ERRORS - WRONG ORDER
        {
            "input": "15-10-2023",
            "error_type": ValueError,
            "description": "Already in DD-MM-YYYY format (wrong direction)"
        },
        {
            "input": "10-15-2023",
            "error_type": ValueError,
            "description": "MM-DD-YYYY format"
        },
        {
            "input": "2023-15-10",
            "error_type": ValueError,
            "description": "YYYY-DD-MM format"
        },
        
        # FORMAT ERRORS - WRONG NUMBER OF PARTS
        {
            "input": "2023-10",
            "error_type": ValueError,
            "description": "Missing day"
        },
        {
            "input": "2023-10-15-05",
            "error_type": ValueError,
            "description": "Extra part"
        },
        {
            "input": "2023-10-15-05-30",
            "error_type": ValueError,
            "description": "Extra parts with time"
        },
        
        # FORMAT ERRORS - WRONG NUMBER OF DIGITS
        {
            "input": "23-10-15",
            "error_type": ValueError,
            "description": "2-digit year"
        },
        {
            "input": "2023-1-15",
            "error_type": ValueError,
            "description": "1-digit month"
        },
        {
            "input": "2023-10-5",
            "error_type": ValueError,
            "description": "1-digit day"
        },
        {
            "input": "20231-10-15",
            "error_type": ValueError,
            "description": "5-digit year"
        },
        
        # FORMAT ERRORS - NON-NUMERIC
        {
            "input": "YYYY-MM-DD",
            "error_type": ValueError,
            "description": "Text format string"
        },
        {
            "input": "202a-10-15",
            "error_type": ValueError,
            "description": "Letter in year"
        },
        {
            "input": "2023-1a-15",
            "error_type": ValueError,
            "description": "Letter in month"
        },
        {
            "input": "2023-10-1b",
            "error_type": ValueError,
            "description": "Letter in day"
        },
        
        # INVALID MONTH
        {
            "input": "2023-00-15",
            "error_type": ValueError,
            "description": "Month 00"
        },
        {
            "input": "2023-13-15",
            "error_type": ValueError,
            "description": "Month 13"
        },
        {
            "input": "2023-99-15",
            "error_type": ValueError,
            "description": "Month 99"
        },
        
        # INVALID DAY
        {
            "input": "2023-01-00",
            "error_type": ValueError,
            "description": "Day 00"
        },
        {
            "input": "2023-01-32",
            "error_type": ValueError,
            "description": "Day 32 in January"
        },
        {
            "input": "2023-02-29",
            "error_type": ValueError,
            "description": "February 29 in non-leap year"
        },
        {
            "input": "2023-04-31",
            "error_type": ValueError,
            "description": "Day 31 in April (30 days)"
        },
        {
            "input": "2023-06-31",
            "error_type": ValueError,
            "description": "Day 31 in June (30 days)"
        },
        {
            "input": "2023-09-31",
            "error_type": ValueError,
            "description": "Day 31 in September (30 days)"
        },
        {
            "input": "2023-11-31",
            "error_type": ValueError,
            "description": "Day 31 in November (30 days)"
        },
        {
            "input": "2023-12-32",
            "error_type": ValueError,
            "description": "Day 32"
        },
        {
            "input": "2023-03-99",
            "error_type": ValueError,
            "description": "Day 99"
        },
        
        # INVALID YEAR
        {
            "input": "0000-01-01",
            "error_type": ValueError,
            "description": "Year 0000"
        },
        {
            "input": "-001-01-01",
            "error_type": ValueError,
            "description": "Negative year"
        },
    ]
    
    passed_count = 0
    failed_count = 0
    
    # Test valid cases
    print("\n" + "=" * 120)
    print("VALID DATE CONVERSION TESTS")
    print("=" * 120)
    
    for i, test in enumerate(test_cases, 1):
        input_val = test["input"]
        expected = test["expected"]
        description = test["description"]
        
        try:
            result = convert_date_format(input_val)
            if result == expected:
                status = "✓ PASS"
                passed_count += 1
            else:
                status = "✗ FAIL"
                failed_count += 1
            
            print(f"\n{status} | Test {i}")
            print(f"  Input:    '{input_val}'")
            print(f"  Expected: '{expected}'")
            print(f"  Got:      '{result}'")
            print(f"  Description: {description}")
            
        except Exception as e:
            print(f"\n✗ FAIL | Test {i}")
            print(f"  Input: '{input_val}'")
            print(f"  Unexpected error: {type(e).__name__}: {e}")
            print(f"  Description: {description}")
            failed_count += 1
    
    # Test invalid cases
    print("\n" + "=" * 120)
    print("INVALID DATE TESTS (Should raise exceptions)")
    print("=" * 120)
    
    for i, test in enumerate(invalid_test_cases, 1):
        input_val = test["input"]
        expected_error = test["error_type"]
        description = test["description"]
        
        try:
            result = convert_date_format(input_val)
            print(f"\n✗ FAIL | Invalid Test {i}")
            print(f"  Input: {input_val!r}")
            print(f"  Expected {expected_error.__name__} but got result: '{result}'")
            print(f"  Description: {description}")
            failed_count += 1
        except expected_error as e:
            print(f"\n✓ PASS | Invalid Test {i}")
            print(f"  Input: {input_val!r}")
            print(f"  Raised {expected_error.__name__}: {e}")
            print(f"  Description: {description}")
            passed_count += 1
        except Exception as e:
            print(f"\n✗ FAIL | Invalid Test {i}")
            print(f"  Input: {input_val!r}")
            print(f"  Expected {expected_error.__name__} but got {type(e).__name__}: {e}")
            print(f"  Description: {description}")
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 120)
    print("TEST SUMMARY")
    print("=" * 120)
    total_tests = len(test_cases) + len(invalid_test_cases)
    
    print(f"\nValid Conversion Tests: {len(test_cases)}")
    print(f"Invalid Input Tests:   {len(invalid_test_cases)}")
    print(f"Total Tests:           {total_tests}")
    print(f"\nTests Passed: {passed_count}/{total_tests}")
    print(f"Tests Failed: {failed_count}/{total_tests}")
    
    if failed_count == 0:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\n❌ {failed_count} test(s) failed")
    
    print("=" * 120)


# Demonstration function
def demonstrate_function():
    """Demonstrate the function with various examples"""
    
    print("\n" + "=" * 120)
    print("FUNCTION DEMONSTRATION")
    print("=" * 120)
    
    examples = [
        "2023-10-15",
        "2024-02-29",
        "2000-12-31",
        "1999-01-01",
    ]
    
    for example in examples:
        result = convert_date_format(example)
        print(f"\nInput:  {example} → Output: {result}")


if __name__ == "__main__":
    run_tests()
    demonstrate_function()
