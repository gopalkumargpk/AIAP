class Employee:
    """
    A class to represent an employee with name and salary information.
    
    Attributes:
        name (str): The name of the employee
        salary (float): The current salary of the employee
    """
    
    def __init__(self, name, salary):
        """
        Initialize an Employee object.
        
        Args:
            name (str): The name of the employee
            salary (float): The initial salary of the employee
        """
        self._name = name
        self._salary = salary
    
    def increase_salary(self, percentage):
        """
        Increase the employee's salary by a given percentage.
        
        Args:
            percentage (float): The percentage increase to apply to the salary
        """
        if percentage < 0:
            raise ValueError("Percentage cannot be negative")
        self._salary = self._salary + (self._salary * percentage / 100)
    
    def display_info(self):
        """
        Display the employee's information in a formatted manner.
        """
        print(f"Employee: {self._name}, Salary: ${self._salary:.2f}")
    
    @property
    def name(self):
        """Get the employee's name."""
        return self._name
    
    @property
    def salary(self):
        """Get the employee's salary."""
        return self._salary


# Example usage:
if __name__ == "__main__":
    # Create an employee instance
    emp1 = Employee("John Doe", 50000)
    
    # Display initial information
    emp1.display_info()
    
    # Increase salary by 10%
    emp1.increase_salary(10)
    
    # Display updated information
    emp1.display_info()