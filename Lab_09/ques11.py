# Implement binary tree in python using classes and methods

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.value:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.value, end=" ")
            self._inorder(root.right)

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root:
            print(root.value, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.value, end=" ")

binary_tree = BinaryTree()

binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(70)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(60)
binary_tree.insert(80)

print("In-order traversal:")
binary_tree.inorder()

print("\nPre-order traversal:")
binary_tree.preorder()

print("\nPost-order traversal:")
binary_tree.postorder()
