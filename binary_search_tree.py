class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = new_node
                        return self
                    current = current.left
                else:
                    if not current.right:
                        current.right = new_node
                        return self
                    current = current.right

    def insert_r(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, current_node, value):
        if value <= current_node.value:
            if current_node.left:
                self.insert_node(current_node.left, value)
            else:
                current_node.left = Node(value)
        elif value > current_node.value:
            if current_node.right:
                self.insert_node(current_node.right, value)
            else:
                current_node.right = Node(value)

    def lookup(self, value):
        if not self.root:
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



    def branchSums(self,  root):
        # Write your code here.
        stack = []
        sums_of_branches = []
        stack.append(root)
        while len(stack) != 0:
            current = stack.pop()


    def flatten_binary_tree(self, root):

        if root is not None:
            arr = []
            self._flatten_binary_tree(root, arr)

            previous = None
            current_node = None
            for i in range(len(arr) - 1):
                current_node = arr[i]
                next_node = arr[i + 1]

                print("NODE:", current_node.value, "NEXT NODE:", next_node.value)

                current_node.left = previous
                current_node.right = next_node
                previous = current_node
                print()

            return current_node
        else:
            return None


    def _flatten_binary_tree(self, node, array):
        if node.left is not None:
            self._flatten_binary_tree(node.left, array)
        array.append(node)
        if node.right is not None:
            self._flatten_binary_tree(node.right, array)


    def findClosestValueInBst(self, tree, target):
        return self.find_closest_value_helper(tree. target, tree.value)
        pass

    def find_closest_value_helper(self, node, target, current_closest):
        if node.left is not None:
            self.find_closest_value_helper(node.left, target, current_closest)

        if node.value == target:
            return target

        if abs(node.value - target) < current_closest:
            current_closest = node.value

        if node.right is not None:
            self.find_closest_value_helper(node.right, target, current_closest)




if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.root = Node(1)
    bst.root.left = Node(2)
    bst.root.left.left = Node(4)
    bst.root.left.right = Node(5)
    bst.root.left.right.left = Node(7)
    bst.root.left.right.right = Node(8)

    bst.root.right = Node(3)
    bst.root.right.left = Node(6)
    results = bst.flatten_binary_tree(bst.root)

    print(results)

    # prints BST
    bst.print_tree(results, 1)

"""
10, 5, 15, 5, 2, 1, 22
"""
