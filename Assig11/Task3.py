class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a node at the end of the linked list"""
        new_node = Node(data)

        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        """Display all nodes in the linked list"""
        current = self.head
        if current is None:
            print("Linked List is empty")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ------------------- Test Code (t) ------------------- #
if __name__ == "__main__":
    ll = SinglyLinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_beginning(5)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    print("Linked List elements:")
    ll.display()     # Output: 5 -> 10 -> 20 -> 30 -> None
