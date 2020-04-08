"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


"""

def search_matrix_1(matrix, target):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False


def search_matrix_2(matrix, target):
    m = len(matrix) - 1
    n = len(matrix[0]) - 1

    i = m
    j = 0

    while i >= 0 and j <= n:
        print(matrix[i][j])
        if target < matrix[i][j]:
            i -= 1
        elif target > matrix[i][j]:
            j += 1
        else:
            return True

    return False





if __name__ == '__main__':
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    results1 = search_matrix_1(matrix, 54)
    print("Results1 ", results1)

    results2 = search_matrix_2(matrix, 9)
    print("Results2 ", results2)
