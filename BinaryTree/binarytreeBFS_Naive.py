class Node():
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def print_current_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_current_level(root.left, level - 1)
        print_current_level(root.right, level - 1)


def print_level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print_current_level(root, i)
        print()


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("BFS Naive:")
    print_level_order(root)
