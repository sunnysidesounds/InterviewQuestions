"""

You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents land, and each 1 represents part of a river.
A river consists of any number of 1s that are either horizontally or vertically adjacent (but not diagonally adjacent).
The number of adjacent 1s forming a river determine its size. Write a function that returns an array of the sizes of
all rivers represented in the input matrix. Note that these sizes do not need to be in any particular order.

# input
[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

# output

  [1, 2, 2, 2, 5]


- given unequal height and width matrix with 0 and 1.
- 0's = land
- 1's = part of river
- river = 1's connected horizontally or vertically adjacent (not diagonally adjacent)
- return array of sizes

- treat this problem as a graph problem

- keep track of nodes you've visited
- identical matrix to keep track of visited nodes
- bfs / dfs algo
- O(w * h)


"""

def river_sizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverse_node(i, j, matrix, visited, sizes)
    return sizes


    pass

def traverse_node(i, j, matrix, visited, sizes):
    current_river_size = 0
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_river_size += 1
        unvisited_neighbors = get_unnvisited_neighbors(i, j, matrix, visited)
        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)
    if current_river_size > 0:
        sizes.append(current_river_size)


def get_unnvisited_neighbors(i, j, matrix, visited):
    unvisited_neighbors = []
    #behind
    if i > 0 and not visited[i-1][j]:
        unvisited_neighbors.append([i-1, j])
    #front
    if i < len(matrix) - 1 and visited[i+1][j]:
        unvisited_neighbors.append([i+1, j])
    # top
    if j > 0 and not visited[i][j-1]:
        unvisited_neighbors.append([i, j-1])
    # bottom
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisited_neighbors.append([i, j+1])
    return unvisited_neighbors




if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]
    results = river_sizes(matrix)
    print(results)
