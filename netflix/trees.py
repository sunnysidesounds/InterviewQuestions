

# Find minimum value in Binary Search Tree
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)

    return node


# Left most value in a binary tree
def minimum_value(node):
    current = node
    while current.left is not None:
        current = current.left

    return current.data


def maximum_value(node):
    current = node
    while current.right is not None:
        current = current.right

    return current.data


# Find Height of Binary Tree
def maximum_height(node):

    if node is None:
        return 0
    else:
        return 1 + max(maximum_height(node.left), maximum_height(node.right))


if __name__ == '__main__':

    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)

    results = minimum_value(root)
    print(results)
    results1 = maximum_value(root)
    print(results1)
    result2 = maximum_height(root)
    print(result2)