"""
Given an undirected graph, find out all the vertices when removed will make the graph disconnected.
Initially the graph is connected.

For example given the graph below:


Return [3, 6]. Because we can make the graph disconnected by removing either vertex 3 or vertex 6.

Input:

nodeNum, the total count of vertices in the graph. Each vertex has an unique id in the range from 0 to nodeNum - 1 inclusive.

edges, a list of integer pairs representing all the edges on the graph.

output:

A list of integers representing the ids of the articulation points.

example:

Input:

nodeNum = 7

edges = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]

0 = 2
1 = 2
2 = 3
3 = 3
4 = 1
5 = 2
6 = 1

1
2
2
1
3
1

Output:

[2,3,5]


"""

from collections import defaultdict


def find_critical_nodes(nodeNum, edges):
    graph = defaultdict(list)
    for vertex in edges:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])

    print(graph)


if __name__ == '__main__':
    results = find_critical_nodes(7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]])
    print(results)