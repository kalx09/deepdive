class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)


root = Node("A")
root.left = Node("B")
root.left.left = Node("C")
root.left.right = Node("D")
root.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

inorder(root)
