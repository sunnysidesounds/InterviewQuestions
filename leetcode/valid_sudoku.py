
def is_valid_sudoku(board):
    valid_row = False
    valid_column = False
    valid_subbox = False

    for row in range(0, len(board)):
        for column in range(0, len(board[0])):

            valid_row = is_valid_row(board, row)
            if not valid_row:
                return False

            valid_column = is_valid_column(board, column)
            if not valid_column:
                return False

            valid_subbox = is_valid_subbox(board, row - row % 3, column - column % 3)
            if not valid_subbox:
                return False

    return valid_row and valid_column and valid_subbox


def is_valid_row(board, row):

    row_map = {}
    for i in range(0, len(board)):
        value = board[row][i]
        if value != '.' and value in row_map:
            return False
        row_map[value] = 1

    return True


def is_valid_column(board, column):
    column_map = {}
    for i in range(0, len(board)):
        value = board[i][column]
        if value != '.' and value in column_map:
            return False
        column_map[value] = 1

    return True


def is_valid_subbox(board, start_row, start_column):
    subbox_map = {}
    for row in range(0, 3):
        for column in range(0, 3):
            value = board[row + start_row][column + start_column]
            if value != '.' and value in subbox_map:
                return False
            subbox_map[value] = 1

    return True


if __name__ == '__main__':

    true_board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

    false_board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]


    test_board = [[ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],
      [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],
      [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],
      [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],
      [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],
      [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],
      [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],
      [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],
      [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ]]

    r = is_valid_sudoku(test_board)
    print(r)
