# Given a binary tree, populate an array to represent its zigzag level order traversal.
# You should populate the values of all nodes of the first level from left to right,
# then right to left for the next level and keep alternating in the same manner for
# the following levels.

# Can be solved using two stacks.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def zigzag_level_order(root):
    if root is None:
        return

    # Create two stacks to store current
    # and next level
    currentLevel = []
    nextLevel = []

    # if ltr is true push nodes from
    # left to right otherwise from
    # right to left
    ltr = True

    # append root to currentlevel stack
    currentLevel.append(root)

    # Check if stack is empty
    while len(currentLevel) > 0:
        # pop from stack
        temp = currentLevel.pop(-1)
        # print the data
        print(temp.data, " ", end="")

        if ltr:
            # if ltr is true push left
            # before right
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            # else push right before left
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            # reverse ltr to push node in
            # opposite order
            ltr = not ltr
            # swapping of stacks
            currentLevel, nextLevel = nextLevel, currentLevel




if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

    zigzag_level_order(root)