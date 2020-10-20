# Different way to traversal a matrix with equal


# LEFT TO RIGHT --->
# Left to Right equals row, than column
def matrix_traversals_left_to_right(matrix):
    arr = []
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            value = matrix[row][column]
            arr.append(value)
    return arr

# RIGHT TO LEFT <--
# Right to Left equals, column, than backwards row
def matrix_traversals_right_to_left(matrix):
    arr = []
    for column in range(len(matrix[0])):
        for row in range(len(matrix) - 1, -1, -1):
            value = matrix[column][row]
            arr.append(value)
    return arr

# TOP TO BOTTOM
# Top to Bottom equals, column, than row
def matrix_traversals_top_to_bottom(matrix):
    arr = []
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):
            value = matrix[row][column]
            arr.append(value)
    return arr

# BOTTOM TO TOP
# Bottom to Top equals, column, than backwards row
def matrix_traversals_bottom_to_top(matrix):
    arr = []
    for column in range(len(matrix[0])):
        for row in range(len(matrix) - 1, -1, -1):
            value = matrix[row][column]
            arr.append(value)
    return arr

# DIAGONAL TOP TO BOTTOM
def matrix_traversals_diagonal_top_bottom(matrix):
    arr = []
    row = 0
    column = 0
    while row < len(matrix):
        value = matrix[row][column]
        arr.append(value)

        row += 1
        column += 1

    return arr

# DIAGONAL BOTTOM TO TOP
def matrix_traversals_diagonal_bottom_top(matrix):
    arr = []
    row = len(matrix) - 1
    column = len(matrix[0]) - 1
    while row >= 0:
        value = matrix[row][column]
        arr.append(value)

        row -= 1
        column -= 1

    return arr

# SPIRAL TOP TO BOTTOM
def matrix_traversals_spiral_top_bottom(matrix):
    """
        k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator
    """
    output_arr = []
    start_row_idx = 0
    end_row_idx = len(matrix)

    start_column_idx = 0
    end_column_idx = len(matrix[0])

    while start_row_idx < end_row_idx:
        while start_column_idx < end_column_idx:
            value = matrix[start_row_idx][start_column_idx]
            output_arr.append(value)
            print("value: ", value)
            start_column_idx += 1

        start_row_idx += 1
    start_row_idx = 1
    while start_row_idx < end_row_idx:
        value = matrix[start_row_idx][start_column_idx - 1]
        output_arr.append(value)
        print("value: ", value)
        start_row_idx += 1



    #print("start_row_idx ", start_row_idx)
    #print("end_row_idx ", end_row_idx)
    #print("start_column_idx ", start_column_idx)
    #print("end_column_idx ", end_column_idx)


    return output_arr

# SPIRAL BOTTOM TO TOP
def matrix_traversals_spiral_bottom_to_top(matrix):

    return None


# Matrix Indexes
# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44


if __name__ == "__main__":

    tests = dict()
    tests['left_to_right'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [1, 4, 7, 11, 15, 2, 5, 8, 12, 19, 3, 6, 9, 16, 22, 10, 13, 14, 17, 24, 18, 21, 23, 26, 30]}

    tests['right_to_left'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [15, 11, 7, 4, 1, 19, 12, 8, 5, 2, 22, 16, 9, 6, 3, 24, 17, 14, 13, 10, 30, 26, 23, 21, 18]}

    tests['top_to_bottom'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [1, 2, 3, 10, 18, 4, 5, 6, 13, 21, 7, 8, 9, 14, 23, 11, 12, 16, 17, 26, 15, 19, 22, 24, 30]}

    tests['bottom_to_top'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [18, 10, 3, 2, 1, 21, 13, 6, 5, 4, 23, 14, 9, 8, 7, 26, 17, 16, 12, 11, 30, 24, 22, 19, 15]}

    tests['diagonal_top_bottom'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [1, 5, 9, 17, 30]}

    tests['diagonal_bottom_top'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [30, 17, 9, 5, 1]}

    tests['sprial_top_bottom'] = {"paramters": [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], "expected": [1, 4, 7, 11, 15, 19, 22, 24, 30, 26, 23, 21, 18, 10, 3, 2, 5, 8, 12, 16, 17, 14, 13, 6, 9]}

    # Left to Right
#   results1 = matrix_traversals_left_to_right(tests['left_to_right']['paramters'])
#   print("Test {0}".format("left_to_right ", tests['left_to_right']['paramters']), tests['left_to_right']['expected'] == results1, results1)

#   # Right to Left
#   results2 = matrix_traversals_right_to_left(tests['right_to_left']['paramters'])
#   print("Test {0}".format("right_to_left ", tests['right_to_left']['paramters']), tests['right_to_left']['expected'] == results2, results2)

#   # Top to Bottom
#   results3 = matrix_traversals_top_to_bottom(tests['top_to_bottom']['paramters'])
#   print("Test {0}".format("top_to_bottom ", tests['top_to_bottom']['paramters']), tests['top_to_bottom']['expected'] == results3, results3)

#   # Bottom to Top
#   results4 = matrix_traversals_bottom_to_top(tests['bottom_to_top']['paramters'])
#   print("Test {0}".format("bottom_to_top ", tests['bottom_to_top']['paramters']), tests['bottom_to_top']['expected'] == results4, results4)

#   # Diagonal Top to Bottom
#   results5 = matrix_traversals_diagonal_top_bottom(tests['diagonal_top_bottom']['paramters'])
#   print("Test {0}".format("diagonal_top_bottom ", tests['diagonal_top_bottom']['paramters']), tests['diagonal_top_bottom']['expected'] == results5, results5)

#   # Diagonal Bottom to Top
#   results6 = matrix_traversals_diagonal_bottom_top(tests['diagonal_bottom_top']['paramters'])
#   print("Test {0}".format("diagonal_bottom_top ", tests['diagonal_bottom_top']['paramters']), tests['diagonal_bottom_top']['expected'] == results6, results6)

    results7 = matrix_traversals_spiral_top_bottom(tests['sprial_top_bottom']['paramters'])
    print("Test {0}".format("sprial_top_bottom ", tests['sprial_top_bottom']['paramters']), tests['sprial_top_bottom']['expected'] == results7, results7)
