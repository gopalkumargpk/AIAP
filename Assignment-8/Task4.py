from typing import Dict, List, Tuple
from decimal import Decimal, ROUND_HALF_UP


class ShoppingCart:
    """
    A shopping cart implementation for managing items and calculating costs.
    
    Attributes:
        items (dict): Dictionary storing items with name as key and (price, quantity) as value
    """
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.
        
        If the item already exists, the quantity is incremented.
        
        Args:
            name (str): The name of the item
            price (float): The price of the item (must be non-negative)
            quantity (int): The quantity to add (default: 1, must be positive)
            
        Raises:
            TypeError: If name is not a string, or price/quantity are not valid numbers
            ValueError: If price is negative or quantity is not positive
        """
        
        # Validate inputs
        if not isinstance(name, str):
            raise TypeError(f"Item name must be a string, got {type(name).__name__}")
        
        if not name.strip():
            raise ValueError("Item name cannot be empty or whitespace only")
        
        if not isinstance(price, (int, float)):
            raise TypeError(f"Price must be a number, got {type(price).__name__}")
        
        if not isinstance(quantity, int):
            raise TypeError(f"Quantity must be an integer, got {type(quantity).__name__}")
        
        if price < 0:
            raise ValueError(f"Price cannot be negative, got {price}")
        
        if quantity <= 0:
            raise ValueError(f"Quantity must be positive, got {quantity}")
        
        # Convert price to Decimal for precision
        price = Decimal(str(price))
        
        # Add or update item
        name = name.strip()
        if name in self.items:
            existing_price, existing_qty = self.items[name]
            self.items[name] = (price, existing_qty + quantity)
        else:
            self.items[name] = (price, quantity)
    
    def remove_item(self, name: str, quantity: int = None) -> bool:
        """
        Remove an item from the shopping cart.
        
        If quantity is specified, only that quantity is removed.
        If quantity is not specified or exceeds item quantity, the entire item is removed.
        
        Args:
            name (str): The name of the item to remove
            quantity (int): The quantity to remove (optional)
            
        Returns:
            bool: True if item was found and removed, False if item not found
            
        Raises:
            TypeError: If name is not a string or quantity is not an integer
            ValueError: If quantity is negative or zero
        """
        
        # Validate inputs
        if not isinstance(name, str):
            raise TypeError(f"Item name must be a string, got {type(name).__name__}")
        
        if quantity is not None:
            if not isinstance(quantity, int):
                raise TypeError(f"Quantity must be an integer, got {type(quantity).__name__}")
            
            if quantity <= 0:
                raise ValueError(f"Quantity must be positive, got {quantity}")
        
        name = name.strip()
        
        # Check if item exists
        if name not in self.items:
            return False
        
        # Remove item or reduce quantity
        if quantity is None:
            # Remove entire item
            del self.items[name]
        else:
            price, current_qty = self.items[name]
            if quantity >= current_qty:
                # Remove entire item if quantity exceeds or equals current
                del self.items[name]
            else:
                # Reduce quantity
                self.items[name] = (price, current_qty - quantity)
        
        return True
    
    def total_cost(self) -> Decimal:
        """
        Calculate the total cost of all items in the cart.
        
        Returns:
            Decimal: The total cost with proper precision
        """
        total = Decimal('0')
        for price, quantity in self.items.values():
            total += price * quantity
        
        return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def get_item_count(self) -> int:
        """Get the total number of items in the cart."""
        return sum(qty for _, qty in self.items.values())
    
    def get_unique_items_count(self) -> int:
        """Get the number of unique items in the cart."""
        return len(self.items)
    
    def get_items(self) -> Dict[str, Tuple[Decimal, int]]:
        """Get a copy of all items in the cart."""
        return dict(self.items)
    
    def clear(self) -> None:
        """Clear all items from the cart."""
        self.items.clear()
    
    def is_empty(self) -> bool:
        """Check if the cart is empty."""
        return len(self.items) == 0
    
    def __str__(self) -> str:
        """String representation of the cart."""
        if not self.items:
            return "Shopping Cart is empty"
        
        items_str = "\n".join(
            f"  - {name}: ${price} x {qty} = ${price * qty}"
            for name, (price, qty) in self.items.items()
        )
        return f"Shopping Cart:\n{items_str}\nTotal: ${self.total_cost()}"
    
    def __repr__(self) -> str:
        """Representation of the cart."""
        return f"ShoppingCart(items={len(self.items)}, total=${self.total_cost()})"


# Comprehensive Test Cases
def run_tests():
    """Run all test cases for the ShoppingCart class"""
    
    print("=" * 110)
    print("RUNNING SHOPPINGCART CLASS TEST SUITE")
    print("=" * 110)
    
    test_count = 0
    passed_count = 0
    failed_count = 0
    
    def test_case(test_name: str, test_func):
        """Helper function to run a test case"""
        nonlocal test_count, passed_count, failed_count
        test_count += 1
        
        try:
            test_func()
            print(f"✓ PASS | {test_name}")
            passed_count += 1
        except AssertionError as e:
            print(f"✗ FAIL | {test_name}: {e}")
            failed_count += 1
        except Exception as e:
            print(f"✗ ERROR | {test_name}: {type(e).__name__}: {e}")
            failed_count += 1
    
    # ==================== INITIALIZATION TESTS ====================
    print("\n" + "=" * 110)
    print("1. INITIALIZATION TESTS")
    print("=" * 110)
    
    def test_init_empty_cart():
        cart = ShoppingCart()
        assert cart.is_empty(), "Cart should be empty after initialization"
        assert cart.get_item_count() == 0, "Item count should be 0"
        assert cart.get_unique_items_count() == 0, "Unique items count should be 0"
        assert cart.total_cost() == Decimal('0'), "Total cost should be 0"
    
    test_case("Create empty shopping cart", test_init_empty_cart)
    
    # ==================== ADD_ITEM TESTS ====================
    print("\n" + "=" * 110)
    print("2. ADD_ITEM TESTS - VALID INPUTS")
    print("=" * 110)
    
    def test_add_single_item():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        assert not cart.is_empty(), "Cart should not be empty"
        assert cart.get_item_count() == 1, "Item count should be 1"
        assert cart.total_cost() == Decimal('1.50'), "Total cost should be 1.50"
    
    test_case("Add single item to cart", test_add_single_item)
    
    def test_add_multiple_items():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.add_item("Orange", 2.00)
        assert cart.get_unique_items_count() == 3, "Should have 3 unique items"
        assert cart.get_item_count() == 3, "Should have 3 total items"
        assert cart.total_cost() == Decimal('4.25'), f"Total should be 4.25, got {cart.total_cost()}"
    
    test_case("Add multiple different items", test_add_multiple_items)
    
    def test_add_item_with_quantity():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=5)
        assert cart.get_item_count() == 5, "Should have 5 apples"
        assert cart.get_unique_items_count() == 1, "Should have 1 unique item"
        assert cart.total_cost() == Decimal('7.50'), "Total should be 7.50"
    
    test_case("Add item with quantity greater than 1", test_add_item_with_quantity)
    
    def test_add_same_item_multiple_times():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Apple", 1.50, quantity=2)
        assert cart.get_item_count() == 3, "Should have 3 apples total"
        assert cart.get_unique_items_count() == 1, "Should have 1 unique item"
        assert cart.total_cost() == Decimal('4.50'), "Total should be 4.50"
    
    test_case("Add same item multiple times (cumulative)", test_add_same_item_multiple_times)
    
    def test_add_item_with_whitespace_in_name():
        cart = ShoppingCart()
        cart.add_item("  Apple  ", 1.50)
        cart.add_item("Apple", 1.50)
        assert cart.get_unique_items_count() == 1, "Whitespace should be stripped from names"
        assert cart.get_item_count() == 2, "Should have 2 apples"
    
    test_case("Add items with whitespace in names", test_add_item_with_whitespace_in_name)
    
    def test_add_item_with_zero_price():
        cart = ShoppingCart()
        cart.add_item("Free Item", 0.00)
        assert cart.total_cost() == Decimal('0'), "Total should be 0 for free item"
    
    test_case("Add item with zero price", test_add_item_with_zero_price)
    
    def test_add_item_with_decimal_price():
        cart = ShoppingCart()
        cart.add_item("Item", 9.99)
        assert cart.total_cost() == Decimal('9.99'), "Should handle decimal prices"
    
    test_case("Add item with decimal price", test_add_item_with_decimal_price)
    
    def test_add_item_with_integer_price():
        cart = ShoppingCart()
        cart.add_item("Item", 5)
        assert cart.total_cost() == Decimal('5.00'), "Should handle integer prices"
    
    test_case("Add item with integer price", test_add_item_with_integer_price)
    
    def test_add_multiple_items_with_quantities():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        cart.add_item("Banana", 0.75, 2)
        cart.add_item("Orange", 2.00, 1)
        assert cart.get_item_count() == 6, "Should have 6 total items"
        assert cart.total_cost() == Decimal('7.00'), f"Total should be 7.00, got {cart.total_cost()}"
    
    test_case("Add multiple items with different quantities", test_add_multiple_items_with_quantities)
    
    # ==================== ADD_ITEM INVALID INPUT TESTS ====================
    print("\n" + "=" * 110)
    print("3. ADD_ITEM TESTS - INVALID INPUTS")
    print("=" * 110)
    
    def test_add_item_invalid_name_type():
        cart = ShoppingCart()
        try:
            cart.add_item(123, 1.50)
            raise AssertionError("Should raise TypeError for non-string name")
        except TypeError:
            pass
    
    test_case("Add item with non-string name", test_add_item_invalid_name_type)
    
    def test_add_item_empty_name():
        cart = ShoppingCart()
        try:
            cart.add_item("", 1.50)
            raise AssertionError("Should raise ValueError for empty name")
        except ValueError:
            pass
    
    test_case("Add item with empty name", test_add_item_empty_name)
    
    def test_add_item_whitespace_only_name():
        cart = ShoppingCart()
        try:
            cart.add_item("   ", 1.50)
            raise AssertionError("Should raise ValueError for whitespace-only name")
        except ValueError:
            pass
    
    test_case("Add item with whitespace-only name", test_add_item_whitespace_only_name)
    
    def test_add_item_invalid_price_type():
        cart = ShoppingCart()
        try:
            cart.add_item("Apple", "1.50")
            raise AssertionError("Should raise TypeError for non-numeric price")
        except TypeError:
            pass
    
    test_case("Add item with non-numeric price", test_add_item_invalid_price_type)
    
    def test_add_item_negative_price():
        cart = ShoppingCart()
        try:
            cart.add_item("Apple", -1.50)
            raise AssertionError("Should raise ValueError for negative price")
        except ValueError:
            pass
    
    test_case("Add item with negative price", test_add_item_negative_price)
    
    def test_add_item_invalid_quantity_type():
        cart = ShoppingCart()
        try:
            cart.add_item("Apple", 1.50, quantity="5")
            raise AssertionError("Should raise TypeError for non-integer quantity")
        except TypeError:
            pass
    
    test_case("Add item with non-integer quantity", test_add_item_invalid_quantity_type)
    
    def test_add_item_zero_quantity():
        cart = ShoppingCart()
        try:
            cart.add_item("Apple", 1.50, quantity=0)
            raise AssertionError("Should raise ValueError for zero quantity")
        except ValueError:
            pass
    
    test_case("Add item with zero quantity", test_add_item_zero_quantity)
    
    def test_add_item_negative_quantity():
        cart = ShoppingCart()
        try:
            cart.add_item("Apple", 1.50, quantity=-5)
            raise AssertionError("Should raise ValueError for negative quantity")
        except ValueError:
            pass
    
    test_case("Add item with negative quantity", test_add_item_negative_quantity)
    
    # ==================== REMOVE_ITEM TESTS ====================
    print("\n" + "=" * 110)
    print("4. REMOVE_ITEM TESTS - VALID INPUTS")
    print("=" * 110)
    
    def test_remove_single_item():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        result = cart.remove_item("Apple")
        assert result is True, "Should return True when item is removed"
        assert cart.is_empty(), "Cart should be empty after removal"
    
    test_case("Remove single item from cart", test_remove_single_item)
    
    def test_remove_nonexistent_item():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        result = cart.remove_item("Banana")
        assert result is False, "Should return False when item not found"
        assert not cart.is_empty(), "Cart should still have apple"
    
    test_case("Remove nonexistent item", test_remove_nonexistent_item)
    
    def test_remove_item_from_empty_cart():
        cart = ShoppingCart()
        result = cart.remove_item("Apple")
        assert result is False, "Should return False when removing from empty cart"
    
    test_case("Remove item from empty cart", test_remove_item_from_empty_cart)
    
    def test_remove_specific_quantity():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=5)
        cart.remove_item("Apple", quantity=2)
        assert cart.get_item_count() == 3, "Should have 3 apples left"
        assert cart.total_cost() == Decimal('4.50'), "Total should be 4.50"
    
    test_case("Remove specific quantity of item", test_remove_specific_quantity)
    
    def test_remove_entire_quantity():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=3)
        cart.remove_item("Apple", quantity=3)
        assert cart.is_empty(), "Cart should be empty after removing all"
    
    test_case("Remove entire quantity", test_remove_entire_quantity)
    
    def test_remove_more_than_available():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=2)
        cart.remove_item("Apple", quantity=5)
        assert cart.is_empty(), "Cart should be empty when removing more than available"
    
    test_case("Remove more quantity than available", test_remove_more_than_available)
    
    def test_remove_with_whitespace_in_name():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        result = cart.remove_item("  Apple  ")
        assert result is True, "Should remove item with whitespace in name"
        assert cart.is_empty(), "Cart should be empty"
    
    test_case("Remove item with whitespace in name", test_remove_with_whitespace_in_name)
    
    def test_remove_multiple_items():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.add_item("Orange", 2.00)
        cart.remove_item("Banana")
        assert cart.get_unique_items_count() == 2, "Should have 2 items left"
        assert cart.total_cost() == Decimal('3.50'), "Total should be 3.50"
    
    test_case("Remove one item from multiple", test_remove_multiple_items)
    
    # ==================== REMOVE_ITEM INVALID INPUT TESTS ====================
    print("\n" + "=" * 110)
    print("5. REMOVE_ITEM TESTS - INVALID INPUTS")
    print("=" * 110)
    
    def test_remove_item_invalid_name_type():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        try:
            cart.remove_item(123)
            raise AssertionError("Should raise TypeError for non-string name")
        except TypeError:
            pass
    
    test_case("Remove item with non-string name", test_remove_item_invalid_name_type)
    
    def test_remove_item_invalid_quantity_type():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=5)
        try:
            cart.remove_item("Apple", quantity="2")
            raise AssertionError("Should raise TypeError for non-integer quantity")
        except TypeError:
            pass
    
    test_case("Remove item with non-integer quantity", test_remove_item_invalid_quantity_type)
    
    def test_remove_item_zero_quantity():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=5)
        try:
            cart.remove_item("Apple", quantity=0)
            raise AssertionError("Should raise ValueError for zero quantity")
        except ValueError:
            pass
    
    test_case("Remove item with zero quantity", test_remove_item_zero_quantity)
    
    def test_remove_item_negative_quantity():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, quantity=5)
        try:
            cart.remove_item("Apple", quantity=-2)
            raise AssertionError("Should raise ValueError for negative quantity")
        except ValueError:
            pass
    
    test_case("Remove item with negative quantity", test_remove_item_negative_quantity)
    
    # ==================== TOTAL_COST TESTS ====================
    print("\n" + "=" * 110)
    print("6. TOTAL_COST TESTS")
    print("=" * 110)
    
    def test_total_cost_empty_cart():
        cart = ShoppingCart()
        assert cart.total_cost() == Decimal('0'), "Empty cart should have total 0"
    
    test_case("Total cost of empty cart", test_total_cost_empty_cart)
    
    def test_total_cost_single_item():
        cart = ShoppingCart()
        cart.add_item("Apple", 5.99)
        assert cart.total_cost() == Decimal('5.99'), "Total should match single item price"
    
    test_case("Total cost with single item", test_total_cost_single_item)
    
    def test_total_cost_multiple_items():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.add_item("Orange", 2.00)
        expected = Decimal('4.25')
        assert cart.total_cost() == expected, f"Total should be {expected}, got {cart.total_cost()}"
    
    test_case("Total cost with multiple different items", test_total_cost_multiple_items)
    
    def test_total_cost_with_quantities():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        cart.add_item("Banana", 0.75, 2)
        expected = Decimal('6.00')
        assert cart.total_cost() == expected, f"Total should be {expected}, got {cart.total_cost()}"
    
    test_case("Total cost with quantities", test_total_cost_with_quantities)
    
    def test_total_cost_precision():
        cart = ShoppingCart()
        cart.add_item("Item1", 0.10)
        cart.add_item("Item2", 0.20)
        cart.add_item("Item3", 0.30)
        assert cart.total_cost() == Decimal('0.60'), "Should handle decimal precision"
    
    test_case("Total cost with decimal precision", test_total_cost_precision)
    
    def test_total_cost_rounding():
        cart = ShoppingCart()
        cart.add_item("Item", 0.01, 3)  # 0.03
        assert cart.total_cost() == Decimal('0.03'), "Should handle rounding correctly"
    
    test_case("Total cost with rounding", test_total_cost_rounding)
    
    def test_total_cost_after_removal():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 5)
        cart.remove_item("Apple", 2)
        expected = Decimal('4.50')
        assert cart.total_cost() == expected, f"Total should be {expected}, got {cart.total_cost()}"
    
    test_case("Total cost after partial removal", test_total_cost_after_removal)
    
    def test_total_cost_large_amounts():
        cart = ShoppingCart()
        cart.add_item("Item1", 999.99, 10)
        cart.add_item("Item2", 500.00, 5)
        expected = Decimal('12499.90')
        assert cart.total_cost() == expected, f"Total should be {expected}, got {cart.total_cost()}"
    
    test_case("Total cost with large amounts", test_total_cost_large_amounts)
    
    # ==================== COMPLEX SCENARIO TESTS ====================
    print("\n" + "=" * 110)
    print("7. COMPLEX SCENARIO TESTS")
    print("=" * 110)
    
    def test_complete_shopping_scenario():
        cart = ShoppingCart()
        # Add items
        cart.add_item("Milk", 3.50, 2)
        cart.add_item("Bread", 2.00, 1)
        cart.add_item("Eggs", 4.50, 1)
        assert cart.total_cost() == Decimal('13.50'), "After adding 3 items"
        
        # Remove some items
        cart.remove_item("Milk", 1)
        assert cart.total_cost() == Decimal('10.00'), "After removing 1 milk"
        
        # Add more items
        cart.add_item("Butter", 5.00, 1)
        assert cart.total_cost() == Decimal('15.00'), "After adding butter"
        
        # Remove entire item
        cart.remove_item("Bread")
        assert cart.total_cost() == Decimal('13.00'), "After removing bread"
    
    test_case("Complete shopping scenario", test_complete_shopping_scenario)
    
    def test_cart_with_duplicate_items():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Apple", 1.50)
        cart.add_item("Apple", 1.50)
        assert cart.get_item_count() == 3, "Should accumulate quantities"
        assert cart.get_unique_items_count() == 1, "Should be only 1 unique item"
        assert cart.total_cost() == Decimal('4.50'), "Total should be 4.50"
    
    test_case("Cart with duplicate items added separately", test_cart_with_duplicate_items)
    
    def test_clear_cart():
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75, 3)
        cart.clear()
        assert cart.is_empty(), "Cart should be empty after clear"
        assert cart.total_cost() == Decimal('0'), "Total should be 0"
    
    test_case("Clear entire cart", test_clear_cart)
    
    def test_alternating_add_remove():
        cart = ShoppingCart()
        cart.add_item("Item1", 10.00)
        cart.add_item("Item2", 20.00)
        cart.remove_item("Item1")
        cart.add_item("Item3", 30.00)
        cart.remove_item("Item2")
        cart.add_item("Item4", 40.00)
        assert cart.get_unique_items_count() == 2, "Should have 2 items"
        assert cart.total_cost() == Decimal('70.00'), "Total should be 70.00"
    
    test_case("Alternating add and remove operations", test_alternating_add_remove)
    
    # ==================== SUMMARY ====================
    print("\n" + "=" * 110)
    print("TEST SUMMARY")
    print("=" * 110)
    print(f"\nTotal Tests: {test_count}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    
    if failed_count == 0:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\n❌ {failed_count} test(s) failed")
    
    print("=" * 110)


if __name__ == "__main__":
    run_tests()
