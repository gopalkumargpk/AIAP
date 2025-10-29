class Student:
    """
    A class to represent a student in a school management system.
    
    Attributes:
        name (str): The student's full name
        roll_number (str): Unique student ID
        grades (dict): Dictionary containing subject:grade pairs
        attendance (float): Attendance percentage
    """
    
    def __init__(self, name, roll_number):
        """
        Initialize a new student.
        
        Args:
            name (str): Student's full name
            roll_number (str): Unique student ID
        """
        self.name = name
        self.roll_number = roll_number
        self.grades = {}
        self.attendance = 0.0
    
    def add_grade(self, subject, grade):
        """
        Add or update a grade for a subject.
        
        Args:
            subject (str): Name of the subject
            grade (float): Grade received (0-100)
        """
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def calculate_average(self):
        """
        Calculate the average grade across all subjects.
        
        Returns:
            float: Average grade, or 0 if no grades exist
        """
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def update_attendance(self, days_present, total_days):
        """
        Update student's attendance percentage.
        
        Args:
            days_present (int): Number of days student was present
            total_days (int): Total number of school days
        """
        if total_days > 0 and days_present <= total_days:
            self.attendance = (days_present / total_days) * 100
        else:
            raise ValueError("Invalid attendance values")
    
    def get_status(self):
        """
        Get the student's academic status based on grades and attendance.
        
        Returns:
            str: Status message indicating academic standing
        """
        average = self.calculate_average()
        if self.attendance < 75:
            return "Warning: Low attendance"
        elif average >= 90:
            return "Excellent"
        elif average >= 75:
            return "Good"
        elif average >= 60:
            return "Pass"
        else:
            return "Needs Improvement"
    
    def __str__(self):
        """
        String representation of the student.
        
        Returns:
            str: Formatted string with student details
        """
        return (f"Student: {self.name}\n"
                f"Roll Number: {self.roll_number}\n"
                f"Average Grade: {self.calculate_average():.2f}\n"
                f"Attendance: {self.attendance:.2f}%\n"
                f"Status: {self.get_status()}")

# Example usage
def main():
    try:
        # Create a new student
        student = Student("John Doe", "A123")
        
        # Add grades for different subjects
        student.add_grade("Math", 95)
        student.add_grade("Science", 88)
        student.add_grade("English", 92)
        
        # Update attendance
        student.update_attendance(85, 100)  # 85 days present out of 100
        
        # Print student information
        print(student)
        
        # Demonstrate error handling
        try:
            student.add_grade("History", 150)  # Invalid grade
        except ValueError as e:
            print(f"\nError: {e}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()