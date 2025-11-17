class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node into the BST"""
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._insert_recursive(root.left, data)
        else:
            root.right = self._insert_recursive(root.right, data)

        return root

    def inorder_traversal(self):
        """Perform inorder traversal and print nodes"""
        print("Inorder Traversal:", end=" ")
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.data, end=" ")
            self._inorder_recursive(root.right)


# ------------------- Test Code (t) ------------------- #
if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    bst.inorder_traversal()   # Expected Output: 20 30 40 50 60 70 80
