"""
Python Queue Class Implementation with Error Handling
This module implements a Queue data structure with enqueue, dequeue, and peek operations.
"""


class Queue:
    """
    A simple Queue implementation using a Python list.
    Follows FIFO (First In, First Out) principle.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, data):
        """
        Add an item to the back of the queue.
        
        Args:
            data: The data to add to the queue
        
        Returns:
            bool: True if enqueue was successful
        """
        self.items.append(data)
        return True
    
    def dequeue(self):
        """
        Remove and return the item from the front of the queue.
        
        Returns:
            The data from the front of the queue
        
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self.items.pop(0)
    
    def peek(self):
        """
        View the item at the front of the queue without removing it.
        
        Returns:
            The data from the front of the queue
        
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue")
        return self.items[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: The number of items in the queue
        """
        return len(self.items)
    
    def __str__(self):
        """Return a string representation of the queue."""
        return f"Queue({self.items})"


# ============================================================================
# TESTING SECTION
# ============================================================================

def test_queue():
    """Comprehensive test suite for the Queue class."""
    
    print("=" * 70)
    print("QUEUE CLASS TESTING")
    print("=" * 70)
    
    # Test 1: Create an empty queue
    print("\n[TEST 1] Creating an empty queue")
    q = Queue()
    print(f"  Queue created: {q}")
    print(f"  Is empty? {q.is_empty()}")
    print(f"  Size: {q.size()}")
    assert q.is_empty() == True, "Queue should be empty"
    assert q.size() == 0, "Queue size should be 0"
    print("  ✓ PASSED")
    
    # Test 2: Enqueue items
    print("\n[TEST 2] Enqueuing items (adding to queue)")
    q.enqueue(10)
    print(f"  After enqueue(10): {q}, Size: {q.size()}")
    q.enqueue(20)
    print(f"  After enqueue(20): {q}, Size: {q.size()}")
    q.enqueue(30)
    print(f"  After enqueue(30): {q}, Size: {q.size()}")
    q.enqueue("Hello")
    print(f"  After enqueue('Hello'): {q}, Size: {q.size()}")
    q.enqueue([1, 2, 3])
    print(f"  After enqueue([1, 2, 3]): {q}, Size: {q.size()}")
    assert q.size() == 5, "Queue should have 5 items"
    assert not q.is_empty(), "Queue should not be empty"
    print("  ✓ PASSED")
    
    # Test 3: Peek at the front item (without removing)
    print("\n[TEST 3] Peeking at the front item (without removing)")
    front_item = q.peek()
    print(f"  Front item (peek): {front_item}")
    print(f"  Queue after peek: {q}, Size: {q.size()}")
    assert front_item == 10, "Front item should be 10"
    assert q.size() == 5, "Size should remain 5 after peek"
    print("  ✓ PASSED - Peek doesn't remove the item")
    
    # Test 4: Dequeue items (FIFO order)
    print("\n[TEST 4] Dequeuing items (FIFO - First In First Out)")
    dequeued1 = q.dequeue()
    print(f"  Dequeue 1: {dequeued1}, Remaining queue: {q}, Size: {q.size()}")
    assert dequeued1 == 10, "First dequeue should be 10"
    
    dequeued2 = q.dequeue()
    print(f"  Dequeue 2: {dequeued2}, Remaining queue: {q}, Size: {q.size()}")
    assert dequeued2 == 20, "Second dequeue should be 20"
    
    dequeued3 = q.dequeue()
    print(f"  Dequeue 3: {dequeued3}, Remaining queue: {q}, Size: {q.size()}")
    assert dequeued3 == 30, "Third dequeue should be 30"
    
    dequeued4 = q.dequeue()
    print(f"  Dequeue 4: {dequeued4}, Remaining queue: {q}, Size: {q.size()}")
    assert dequeued4 == "Hello", "Fourth dequeue should be 'Hello'"
    
    dequeued5 = q.dequeue()
    print(f"  Dequeue 5: {dequeued5}, Remaining queue: {q}, Size: {q.size()}")
    assert dequeued5 == [1, 2, 3], "Fifth dequeue should be [1, 2, 3]"
    print("  ✓ PASSED - Items removed in FIFO order")
    
    # Test 5: Verify queue is now empty
    print("\n[TEST 5] Verifying queue is empty after dequeuing all items")
    print(f"  Queue: {q}")
    print(f"  Is empty? {q.is_empty()}")
    print(f"  Size: {q.size()}")
    assert q.is_empty() == True, "Queue should be empty"
    assert q.size() == 0, "Queue size should be 0"
    print("  ✓ PASSED")
    
    # Test 6: Error handling - Dequeue from empty queue
    print("\n[TEST 6] Error handling - Dequeue from empty queue")
    try:
        q.dequeue()
        print("  ✗ FAILED - Should have raised IndexError")
        assert False, "Should have raised IndexError"
    except IndexError as e:
        print(f"  Exception caught: {e}")
        print("  ✓ PASSED - IndexError raised as expected")
    
    # Test 7: Error handling - Peek at empty queue
    print("\n[TEST 7] Error handling - Peek at empty queue")
    try:
        q.peek()
        print("  ✗ FAILED - Should have raised IndexError")
        assert False, "Should have raised IndexError"
    except IndexError as e:
        print(f"  Exception caught: {e}")
        print("  ✓ PASSED - IndexError raised as expected")
    
    # Test 8: Mixed operations with error handling
    print("\n[TEST 8] Mixed operations with error handling")
    q2 = Queue()
    q2.enqueue("A")
    print(f"  After enqueue('A'): {q2}")
    q2.enqueue("B")
    print(f"  After enqueue('B'): {q2}")
    print(f"  Peek: {q2.peek()}")
    print(f"  Dequeue: {q2.dequeue()}")
    print(f"  After first dequeue: {q2}")
    q2.enqueue("C")
    print(f"  After enqueue('C'): {q2}")
    print(f"  Dequeue: {q2.dequeue()}")
    print(f"  After second dequeue: {q2}")
    print(f"  Dequeue: {q2.dequeue()}")
    print(f"  After third dequeue: {q2}")
    print("  ✓ PASSED")
    
    # Test 9: Large number of items
    print("\n[TEST 9] Testing with large number of items (1000 items)")
    q3 = Queue()
    for i in range(1000):
        q3.enqueue(i)
    print(f"  Added 1000 items, Size: {q3.size()}")
    assert q3.size() == 1000, "Queue should have 1000 items"
    assert q3.peek() == 0, "First item should be 0"
    
    # Remove some items
    for _ in range(500):
        q3.dequeue()
    print(f"  After removing 500 items, Size: {q3.size()}")
    assert q3.size() == 500, "Queue should have 500 items"
    assert q3.peek() == 500, "First item should now be 500"
    print("  ✓ PASSED")
    
    # Test 10: Mixed data types
    print("\n[TEST 10] Testing with mixed data types")
    q4 = Queue()
    mixed_data = [42, 3.14, "string", True, None, {"key": "value"}, [1, 2, 3]]
    for data in mixed_data:
        q4.enqueue(data)
    print(f"  Added 7 items of mixed types: {q4}")
    
    for expected in mixed_data:
        dequeued = q4.dequeue()
        print(f"  Dequeued: {dequeued} (type: {type(dequeued).__name__})")
        assert dequeued == expected, f"Dequeued item should be {expected}"
    print("  ✓ PASSED - All mixed data types handled correctly")
    
    print("\n" + "=" * 70)
    print("ALL TESTS PASSED! ✓")
    print("=" * 70)


if __name__ == "__main__":
    test_queue()
