# Python3 program to Print all possible paths from
# top left to bottom right of a mXn matrix

'''
/* mat: Pointer to the starting of mXn matrix
i, j: Current position of the robot
     (For the first call use 0, 0)
m, n: Dimentions of given the matrix
pi: Next index to be filed in path array
*path[0..pi-1]: The path traversed by robot till now
                (Array to hold the path need to have
                 space for at least m+n elements) */
'''
def printAllPathsUtil(matrix, current_position_i, current_position_j, rows, columns, path, pi):

    # Reached the bottom of the matrix
    # so we are left with only option to move right
    if (current_position_i == rows - 1):
        for k in range(current_position_j, columns):
            path[pi + k - current_position_j] = matrix[current_position_i][k]

        for l in range(pi + columns - current_position_j):
            print(path[l], end = " ")
        print()
        return

    # Reached the right corner of the matrix
    # we are left with only the downward movement.
    if (current_position_j == columns - 1):

        for k in range(current_position_i, rows):
            path[pi + k - current_position_i] = matrix[k][current_position_j]

        for l in range(pi + rows - current_position_i):
            print(path[l], end = " ")
        print()
        return

    # Add the current cell
    # to the path being generated
    path[pi] = matrix[current_position_i][current_position_j]

    # Print all the paths
    # that are possible after moving down
    printAllPathsUtil(matrix, current_position_i + 1, current_position_j, rows, columns, path, pi + 1)

    # Print all the paths
    # that are possible after moving right
    printAllPathsUtil(matrix, current_position_i, current_position_j + 1, rows, columns, path, pi + 1)

    # Print all the paths
    # that are possible after moving diagonal
    # printAllPathsUtil(mat, i+1, j+1, m, n, path, pi + 1);

# The main function that prints all paths
# from top left to bottom right
# in a matrix 'mat' of size mXn
def printAllPaths(matrix, rows, columns):

    path = [0 for i in range(rows + columns)]
    printAllPathsUtil(matrix, 0, 0, rows, columns, path, 0)

# Driver Code
mat = [[1, 2, 3],
       [4, 5, 6]]

if __name__ == '__main__':

    printAllPaths(mat, 2, 3)

# This code is contributed by Mohit Kumar