

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


# Find kth maximum value in Binary Search Tree
def kth_maxiumum_value(node, k):
    current = node
    counter = 0
    k_largest = None
    while current is not None:

        if current.right is None:

            counter += 1
            if counter == k:
                k_largest = current

            current = current.left

        else:
            successor = current.right
            while successor.left is not None and successor.left != current:
                successor = successor.left

            if successor.left is None:
                successor.left = current
                current = current.right
            else:
                successor.left = None
                counter += 1
                if counter == k:
                    k_largest = current

                current = current.left

    return k_largest.data

# Use an inorder traversal, in ascending order of the tree.
# What element are we one
# Return results.
def kth_smallest_value(node, k):
    nums = []
    in_order(root, nums, k)
    return nums[1]


def in_order(root, nums, k):
    if root is None:
        return
    else:
        in_order(root.left, nums, k)
        if nums[0] == k:
            nums[1] = root.data
            return
        in_order(root.right, nums, k)






if __name__ == '__main__':

    root = None
    root = insert(root, 4)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 6)
    insert(root, 5)

    results = minimum_value(root)
    #print(results)
    results1 = maximum_value(root)
    #print(results1)
    result2 = maximum_height(root)
    #print(result2)

    result3 = kth_smallest_value(root, 2)
    print(result3)