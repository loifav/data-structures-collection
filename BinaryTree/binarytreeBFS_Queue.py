class Node():
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None


def level_order_traversal(root):
    if not root:
        return

    queue = []
    queue.append(root)

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)  

        if current.right:
            queue.append(current.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print("BFS Queue:")
    level_order_traversal(root)
