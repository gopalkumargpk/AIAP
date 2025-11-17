class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def peek(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]


# ---------------- Test Code (t) ---------------- #
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue size:", q.size())      # Output: 3
    print("Front element:", q.peek())   # Output: 10

    print("Dequeued:", q.dequeue())     # Output: 10
    print("Front after dequeue:", q.peek())  # Output: 20
    print("Is queue empty?:", q.is_empty())  # Output: False
