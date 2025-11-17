def grade(score):
    """
    Returns letter grade based on numeric score.
    
    Args:
        score: Numeric score value
        
    Returns:
        Letter grade (A, B, C, D, or F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Alternative approach using dictionary mapping with ranges
def grade_dict(score):
    """
    Returns letter grade using dictionary-based approach.
    
    Args:
        score: Numeric score value
        
    Returns:
        Letter grade (A, B, C, D, or F)
    """
    grade_ranges = [
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (0, "F")
    ]
    
    for threshold, letter in grade_ranges:
        if score >= threshold:
            return letter
    
    return "F"


# Example usage
if __name__ == "__main__":
    test_scores = [95, 85, 75, 65, 55]
    
    print("Using elif approach:")
    for score in test_scores:
        print(f"Score: {score} -> Grade: {grade(score)}")
    
    print("\nUsing dictionary approach:")
    for score in test_scores:
        print(f"Score: {score} -> Grade: {grade_dict(score)}")