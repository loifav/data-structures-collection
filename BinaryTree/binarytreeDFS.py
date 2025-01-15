class Node():
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

    def preOrder(node):
        if node is None:
            return
        print(node.data)
        Node.preOrder(node.left)
        Node.preOrder(node.right)
    
    def inOrder(node):
        if node is None:
            return
        Node.inOrder(node.left)
        print(node.data)
        Node.inOrder(node.right)

    def postOrder(node):
        if node is None:
            return
        Node.postOrder(node.left)
        Node.postOrder(node.right)
        print(node.data)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    print("-----PREORDER------")
    Node.preOrder(root)
    print("-------INORDER-------")
    Node.inOrder(root)
    print("-------POSTORDER-------")
    Node.postOrder(root)