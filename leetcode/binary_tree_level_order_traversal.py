


def level_order(root):
    results = []
    queue = []
    if not root:
        return results
    queue.append(root)
    while len(queue) > 0:
        level = len(queue)
        sub_queue = []
        while level > 0:
            node = queue.pop()
            sub_queue.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level -= 1
        results.append(sub_queue)
    return results







if __name__ == '__main__':

    r1 = level_order()
    print(r1)
