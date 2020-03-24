"""
Given a two 2D integer array, find the max score of a path from the upper left cell to bottom right cell.
The score of a path is the minimum value in that path.

Notice: the path can only right and down.

For example:

Input:

[7,5,3]
[2,0,9]
[4,5,9]

Here are some paths from [0,0] to [2,2] and the minimum value on each path:

path: 7->2->4->5->9, minimum value on this path: 2

path: 7->2->0->9->9, minimum value on this path: 0

path: 7->2->0->5->9, minimum value on this path: 0

In the end the max score(the min value) of all the paths is 3.

Output: 3





"""
def max_min_value_path(matrix):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    return calculate_matrix_paths(matrix,
                                  0,  # current_row
                                  0,  # current_column
                                  matrix_rows,  # rows
                                  matrix_columns,  # columns
                                  [0 for _ in range(matrix_rows + matrix_columns)],  # path
                                  [],  # path_list
                                  0  # pointer
                                  )


def calculate_matrix_paths(matrix, current_row, current_column, rows, columns, path, path_list, pointer):
    print()

    # at bottom of matrix, move left to right
    if current_row == (rows - 1):
        for index in range(current_column, columns):
            path[pointer + index - current_column] = matrix[current_row][index]

        sub_path_list = []
        for index in range(pointer + columns - current_column):
            sub_path_list.append(path[index])
        path_list.append(sub_path_list)
        return

    # at right corner, move top to bottom
    if current_column == (columns - 1):
        for index in range(current_row, rows):
            path[pointer + index - current_row] = matrix[index][current_column]

        sub_path_list = []
        for index in range(pointer + rows - current_row):
            sub_path_list.append(path[index])

        path_list.append(sub_path_list)
        return

    path[pointer] = matrix[current_row][current_column]

    calculate_matrix_paths(matrix, current_row + 1, current_column, rows, columns, path, path_list, pointer + 1)
    calculate_matrix_paths(matrix, current_row, current_column + 1, rows, columns, path, path_list, pointer + 1)

    return path_list



if __name__ == '__main__':
    matrix = [[7,5,3],
              [2,0,9],
              [4,5,9]]

    paths = max_min_value_path(matrix)
    print(paths)

    for path in paths:
        min_value = min(path)

        print(min_value)