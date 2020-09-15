

# Given a two-dimensional array, if any element within is zero, make its whole row and column zero.
def make_zero(matrix):
    """
    Naive Approach
    :param matrix:
    :return:
    """
    zero_indexes = []
    for x in range(len(matrix)): # O(x * y) or O(n)
        for y in range(len(matrix[0])):
            value = matrix[x][y]
            if value == 0:
                if (x, y) not in zero_indexes:
                    zero_indexes.append((x, y))

    for (row_index, column_index) in zero_indexes:

        # change row: row 1, column 2
        for i in range(len(matrix)):
            matrix[row_index][i] = 0

        for j in range(len(matrix[0])):
            matrix[j][column_index] = 0

    return matrix

def make_zero_2(matrix):
    """
    Naive Approach
    :param matrix:
    :return:
    """
    for x in range(len(matrix)): # O(x * y) or O(n)
        for y in range(len(matrix[0])):
            value = matrix[x][y]
            if value == 0:
                for i in range(len(matrix)):
                    matrix[x][i] = 0

                for j in range(len(matrix[0])):
                    matrix[j][y] = 0

    return matrix



if __name__ == '__main__':


    matrix = [
            [1, 1, 1, 1],
           [1, 1, 0, 1],
           [1, 1, 1, 1],
           [1, 0, 1, 1]
    ]

    results = make_zero(matrix)

    print(results)

   #  [[1], [0], [0], [1],
   #   [0], [0], [0*], [0],
   #   [1], [0], [0], [1],
   #   [0], [0*], [0], [0]]
#
   # [[1, 0, 0, 1], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]
