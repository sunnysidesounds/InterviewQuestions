class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root

            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break

    def lookup(self, value):
        if self.root == None:
            return None
        node = self.root
        while (node != None):
            if value <= node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            elif node.value == value:
                return node
        return None

    def remove(self, value):
        # Code here
        print()

    def traverse(self, node):
        tree = {}
        print("node: ", node.value)
        if node.left:
            print("node-left: ", node.left.value)
            self.traverse(node.left)
        if node.right:
            print("node-right: ", node.right.value)
            self.traverse(node.left)

    def print_tree(self, root, space):
        COUNT = [10]

        # Base case
        if (root == None):
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        self.print_tree(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end=" ")
        print(root.value)

        # Process left child
        self.print_tree(root.left, space)

    def breath_first_search(self):
        current_node = self.root
        output = []
        queue = []
        queue.append(current_node)
        while (len(queue) > 0):
            current_node = queue.pop()
            output.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return output

    def validate_a_bst(self, node):
        if not node:
            return True
        stack =[{"node": node, "min": float("-inf"), "max": float("inf")}]
        while stack:
            current_node = stack.pop()
            if not current_node['node']:
                continue
            if current_node['node'].value <= current_node['min'] or current_node['node'].value >= current_node['max']:
                return False
            stack.append({"node": current_node['node'].right, "min": current_node['node'].value, "max": current_node['max']})
            stack.append({"node": current_node['node'].left, "min": current_node['min'], "max": current_node['node'].value})
        return True



    # def validate_a_bst_2(self):


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(5)
    bst.insert(2)
    bst.insert(1)
    bst.insert(22)
    # bst.insert(11)

    bst.root.left.right = Node(11)

    is_bst = bst.validate_a_bst(bst.root)
    print(is_bst)

    bst.print_tree(bst.root, 10)

"""
10, 5, 15, 5, 2, 1, 22
"""
