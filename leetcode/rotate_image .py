
import unittest


# brute force
def rotate_image(matrix):

    new_matrix = []

    for column in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix) - 1, -1, -1):
            value = matrix[row][column]
            new_row.append(value)
        new_matrix.append(new_row)

    return new_matrix


def rotate_image_2(matrix):
    n = len(matrix[0])

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            bottom_left = matrix[n - 1 - j][i]
            top_left = matrix[i][j]
            top_right = matrix[j][n - 1 - i]
            bottom_right = matrix[n - 1 - i][n - 1 - j]

            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[j][n - 1 - i] = top_left
            matrix[n - 1 - i][n - 1 - j] = top_right
            matrix[n - 1 - j][i] = bottom_right



    return matrix






class TestRotatingImage(unittest.TestCase):

    def test_1(self):  # brute force
        output = rotate_image([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(output, [[7,4,1],[8,5,2],[9,6,3]], 'Brute force, should be crosswise')

    def test_2(self):  # brute force
        output = rotate_image_2([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(output, [[7,4,1],[8,5,2],[9,6,3]], 'Optimal, should be crosswise')









if __name__ == '__main__':
    unittest.main()
