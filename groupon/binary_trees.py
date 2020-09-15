


def level_order_bfs(root):
    output = []
    queue = []
    if not root:
        return output
    queue.append(root)
    while len(queue) > 0:
        level = len(queue)
        sub_output = []
        while level > 0:
            node = queue.pop()
            sub_output.append(node)
            if not node.left:
                queue.append(node.left)
            if not node.right:
                queue.append(node.right)
            level -=1
        output.append(sub_output)

    return output
