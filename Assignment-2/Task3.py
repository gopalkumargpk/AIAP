def calculate_area(shape_type, *dimensions):
    """
    Calculate the area of different geometric shapes.
    
    Parameters:
    shape_type (str): The type of shape ('circle', 'rectangle', 'triangle', 'square')
    *dimensions: The dimensions of the shape (radius, length, width, base, height, or side)
    
    Returns:
    float: The area of the shape
    """
    # Line 1: Import math module for pi constant
    import math
    
    # Line 2: Convert shape type to lowercase to make it case-insensitive
    shape_type = shape_type.lower()
    
    # Line 3-7: Calculate circle area
    if shape_type == 'circle':
        # Check if exactly one dimension (radius) is provided
        if len(dimensions) != 1:
            return "Error: Circle needs exactly one dimension (radius)"
        return math.pi * dimensions[0] ** 2
    
    # Line 8-12: Calculate rectangle area
    elif shape_type == 'rectangle':
        # Check if exactly two dimensions (length and width) are provided
        if len(dimensions) != 2:
            return "Error: Rectangle needs exactly two dimensions (length and width)"
        return dimensions[0] * dimensions[1]
    
    # Line 13-17: Calculate triangle area
    elif shape_type == 'triangle':
        # Check if exactly two dimensions (base and height) are provided
        if len(dimensions) != 2:
            return "Error: Triangle needs exactly two dimensions (base and height)"
        return 0.5 * dimensions[0] * dimensions[1]
    
    # Line 18-22: Calculate square area
    elif shape_type == 'square':
        # Check if exactly one dimension (side) is provided
        if len(dimensions) != 1:
            return "Error: Square needs exactly one dimension (side)"
        return dimensions[0] ** 2
    
    # Line 23: Handle invalid shape types
    else:
        return "Error: Invalid shape type"

# Example usage
def main():
    # Test the function with different shapes
    print("1. Circle Area (radius = 5):", calculate_area('circle', 5))
    print("2. Rectangle Area (length = 4, width = 6):", calculate_area('rectangle', 4, 6))
    print("3. Triangle Area (base = 3, height = 8):", calculate_area('triangle', 3, 8))
    print("4. Square Area (side = 4):", calculate_area('square', 4))
    # Test error cases
    print("5. Error Case (invalid shape):", calculate_area('pentagon', 5))
    print("6. Error Case (wrong dimensions):", calculate_area('rectangle', 4))

if __name__ == "__main__":
    main()