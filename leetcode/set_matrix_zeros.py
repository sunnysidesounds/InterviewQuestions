


import unittest


def set_matrix_zeros(matrix):
    is_first_row = False
    is_first_column = False

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            is_first_column = True
            break

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            is_first_row = True
            break

    # mark zeros on first row and column
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # use mark to set elements
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][0] or matrix[0][j]:
                matrix[i][j] = 0

    # set first column and row
    if is_first_column:
        for i in range(len(matrix)):
            matrix[i][0] = 0

    if is_first_row:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0

    print(matrix)



class TestSetMatrixZeros(unittest.TestCase):

    def test_1(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        set_matrix_zeros(matrix)
        self.assertEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])


if __name__ == '__main__':
    unittest.main()

