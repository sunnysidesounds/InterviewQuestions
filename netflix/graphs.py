def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]:
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex]:
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return bfs_paths(graph, start, goal)
    except StopIteration:
        return None


def dfs(graph, start):
    visited = []
    stack = [start]
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node][::-1])  # reserve list to mimic adding to stack
    return visited


def dfs_recursion(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        dfs_recursion(graph, next, visited)
    return visited


if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'],
             'B': ['E', 'F'],
             'C': ['H'],
             'D': ['I', 'J'],
             'E': ['K'],
             'J': ['L'],
             'H': ['G'],
             'L': [],
             'I': [],
             'G': [],
             'F': [],
             'K': []}

    r = dfs(graph, 'A')
    print(r)
    r1 = dfs_recursion(graph, 'A')
    print(r1)

    r2 = list(dfs_paths(graph, 'A', 'F'))
    print(r2)

    r3 = list(shortest_path(graph, 'A', 'K'))
    print(r3)