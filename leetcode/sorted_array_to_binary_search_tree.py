


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





def sorted_array_to_bst(nums):
    if not nums or len(nums) == 0:
        return None
    return construct_bst(nums, 0, len(nums) - 1)


def construct_bst(nums, left, right):
    if left > right:
        return None
    middle = left + (right - left) // 2
    current = TreeNode(nums[middle])

    current.left = construct_bst(nums, left, middle - 1)
    current.right = construct_bst(nums, middle + 1, right)
    return current






