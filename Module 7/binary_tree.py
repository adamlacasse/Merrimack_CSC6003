from node import Node

def height(node):
    if node is None:
        return 0
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1
    
def is_balanced(node):
    if node is None:
        return True
    
    left_height = height(node.left)
    right_height = height(node.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
# root.left.left.left = Node(5)

if __name__ == "__main__":
    print("Height of the binary tree is:", height(root))
    print("Is the binary tree balanced?", is_balanced(root))
