# In-order traversal of a binary tree is a depth-first traversal method where the nodes are recursively visited in this order: left subtree, root node, right subtree. This traversal method is commonly used to retrieve the values of a binary search tree in sorted order.
from node import Node

def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)  # Visit left subtree
        print(root.value, end=' ')     # Visit root node
        in_order_traversal(root.right)  # Visit right subtree

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(6)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print("In-order traversal of the binary tree:")
    in_order_traversal(root)
