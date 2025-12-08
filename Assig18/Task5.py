class Car:
    """A class to represent a car."""
    
    def __init__(self, brand, model, year):
        """Initialize car attributes."""
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_details(self):
        """Display car details."""
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


# Create an object and call the method
car = Car("Toyota", "Corolla", 2020)
car.display_details()
