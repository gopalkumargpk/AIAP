import re
from typing import Tuple

def validate_email(email: str) -> Tuple[bool, str]:
    """
    Validates an email address against standard email format rules.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        Tuple[bool, str]: A tuple of (is_valid, message)
    """
    
    # Check if email is empty or None
    if not email or not isinstance(email, str):
        return False, "Email cannot be empty or None"
    
    # Check if email is a string and strip whitespace
    email = email.strip()
    
    if not email:
        return False, "Email cannot be empty"
    
    # Email should not have spaces
    if ' ' in email:
        return False, "Email cannot contain spaces"
    
    # Check basic structure: must have exactly one @
    if email.count('@') != 1:
        return False, "Email must contain exactly one @ symbol"
    
    # Split into local and domain parts
    local_part, domain_part = email.split('@')
    
    # Validate local part (before @)
    if not local_part:
        return False, "Local part (before @) cannot be empty"
    
    if len(local_part) > 64:
        return False, "Local part cannot exceed 64 characters"
    
    # Local part validation: alphanumeric, dots, hyphens, underscores allowed
    # But cannot start or end with a dot
    if local_part.startswith('.') or local_part.endswith('.'):
        return False, "Local part cannot start or end with a dot"
    
    # Check for consecutive dots
    if '..' in local_part:
        return False, "Local part cannot contain consecutive dots"
    
    # Validate characters in local part
    local_pattern = r'^[a-zA-Z0-9._-]+$'
    if not re.match(local_pattern, local_part):
        return False, "Local part contains invalid characters"
    
    # Validate domain part (after @)
    if not domain_part:
        return False, "Domain part (after @) cannot be empty"
    
    # Domain must have at least one dot
    if '.' not in domain_part:
        return False, "Domain must contain at least one dot"
    
    # Split domain into labels (parts separated by dots)
    domain_labels = domain_part.split('.')
    
    # Each label must be non-empty and valid
    for label in domain_labels:
        if not label:
            return False, "Domain cannot have empty labels (consecutive dots)"
        
        if len(label) > 63:
            return False, "Domain label cannot exceed 63 characters"
        
        # Label cannot start or end with hyphen
        if label.startswith('-') or label.endswith('-'):
            return False, "Domain label cannot start or end with a hyphen"
        
        # Label must contain only alphanumeric and hyphens
        if not re.match(r'^[a-zA-Z0-9-]+$', label):
            return False, "Domain label contains invalid characters"
    
    # TLD (last label) must be at least 2 characters and only letters
    tld = domain_labels[-1]
    if len(tld) < 2:
        return False, "Top-level domain must be at least 2 characters"
    
    if not re.match(r'^[a-zA-Z]+$', tld):
        return False, "Top-level domain must contain only letters"
    
    # Overall domain length check (RFC 5321)
    if len(domain_part) > 255:
        return False, "Domain part cannot exceed 255 characters"
    
    # Overall email length check (RFC 5321)
    if len(email) > 320:
        return False, "Email cannot exceed 320 characters"
    
    return True, "Email is valid"


def is_valid_email(email: str) -> bool:
    """
    Simple boolean wrapper for email validation.
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    is_valid, _ = validate_email(email)
    return is_valid


# Test cases
if __name__ == "__main__":
    test_cases = [
        # Valid emails
        ("user@example.com", True),
        ("john.doe@company.co.uk", True),
        ("test_email@test-domain.com", True),
        ("a@b.co", True),
        ("user123@example.org", True),
        ("first.last@sub.domain.com", True),
        
        # Invalid emails
        ("", False),
        ("notanemail", False),
        ("user@", False),
        ("@example.com", False),
        ("user@@example.com", False),
        ("user@example", False),
        ("user name@example.com", False),
        (".user@example.com", False),
        ("user.@example.com", False),
        ("user..name@example.com", False),
        ("user@.example.com", False),
        ("user@example..com", False),
        ("user@example-.com", False),
        ("user@-example.com", False),
        ("user@123", False),
        (None, False),
        ("user@example.c", False),  # TLD too short
        ("user@example.123", False),  # TLD contains numbers
    ]
    
    print("Running email validation tests...\n")
    passed = 0
    failed = 0
    
    for email, expected in test_cases:
        result, message = validate_email(email)
        status = "✓" if result == expected else "✗"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"{status} Email: {email!r:40} | Expected: {expected!s:5} | Got: {result!s:5} | {message}")
    
    print(f"\n{'='*100}")
    print(f"Tests Passed: {passed}/{len(test_cases)}")
    print(f"Tests Failed: {failed}/{len(test_cases)}")
