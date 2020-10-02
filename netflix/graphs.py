import networkx as nx
import matplotlib.pyplot as plt


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
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            if vertex in graph:
                queue.extend(graph[vertex])
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


def generate_graph(graph_from, graph_to):
    graph = {}
    for g_from, g_to in zip(graph_from, graph_to):
        if g_from not in graph:
            graph[g_from] = [g_to]
        else:
            graph[g_from].append(g_to)

        if g_to not in graph:
            graph[g_to] = [g_from]
        else:
            graph[g_to] = [g_from]
    return graph

def dfs_count(graph, node, visited, ids, val, count):
    count += 1
    visited[node] = 1
    if ids[node - 1] == val:
        return count
    else:
        temp = -1
        for u in graph[node]:
            if visited[u] == 0:
                temp = dfs_count(graph, u, visited, ids, val, count)
        return temp


def find_shortest_based_on_color(graph_nodes, graph_from, graph_to, ids, val):
    # 4,[1, 1, 4], [2, 3, 2], [1, 2, 1, 1], 1

    graph = generate_graph(graph_from, graph_to)

    count = 0
    for i in range(len(ids)):
        if ids[i] == val:
            count = 1
            for node in graph[i+1]:
                if ids[node-1] == val:
                    return count
            else:
                temp_list = []
                visited = [0]*(graph_nodes+1)
                visited[i+1] = 1
                for node in graph[i+1]:
                    variable = 0
                    count = dfs_count(graph, node, visited, ids, val, variable)
                    temp_list.append(count)

                minimum = 999999
                flag = 0
                for i in temp_list:
                    if i != -1 and i < minimum:
                        flag = 1
                        minimum = i

                if flag == 1:
                    return minimum
                else:
                    return -1

    if count == 0:
        return -1



def dfs(graph, start):
    visited = []
    stack = [start]
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                stack.extend(graph[node][::-1])  # reserve list to mimic adding to stack
    return visited


def dfs_recursion(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for next in graph[start]:
        dfs_recursion(graph, next, visited)
    return visited

# Find the minimum spanning tree of a connected, undirected graph with weighted edges.




def visualize_graph(graph):
    edge_list = []
    for x in graph:
        for y in graph[x]:
            edge_list.append([x, y])
    G = nx.Graph()
    G.add_edges_from(edge_list)
    nx.draw_networkx(G)
    plt.show()




if __name__ == '__main__':

    # basic graph
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

    # circle graph
    graph2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['E'],
        'E': ['F'],
        'F': ['G'],
        'G': ['A', 'D', 'B'],
    }

    # tree
    graph3 = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '3': ['7', '8'],
        '4': ['9', '10'],
        '5': ['11', '22'],
        '6': ['33', '44'],
        '10': ['55', '66'],
        '9': ['77', '88'],
        '7': ['99', '111'],
        '8': ['232', '343'],
        '11': ['654', '897'],
        '22': ['668', '454']

    }

    graph4 = {
        '1/1': ['2/2', '3/1'],
        '2/2': ['4/1']
    }

    #r = dfs(graph3, '1')
    #print(r)
    #r1 = dfs_recursion(graph, 'A')
    #print(r1)

    #r2 = list(dfs_paths(graph, 'A', 'F'))
    #print(r2)

    #r3 = list(shortest_path(graph3, '1', '111'))
    #print(r3)

    r4 = find_shortest_based_on_color(5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2)
    print(r4)

    r4 = visualize_graph({1: [2, 3], 2: [4], 3: [5]})
