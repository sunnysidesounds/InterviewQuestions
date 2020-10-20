






def is_valid_bst(root):
    return compute_valid_bst(root, float("-inf"), float("inf"))




def compute_valid_bst(node, minv, maxv):
    if node is None:
        return True
    if node.val < minv or node.val >= maxv:
        return False

    left_is_valid = compute_valid_bst(node.left, minv, node.value)
    right_is_valid = compute_valid_bst(node.right, node.value, maxv)
    return left_is_valid and right_is_valid



if __name__ == '__main__':
    pass