

class AIBoard:

    def __init__(self, board):
        self.board = board

    def make_move(self):
        # assuming this is legal move
        if not self.board.is_board_full():

            # get all value with dashes.
            print()

        else:
            raise Exception('Can not make move')







        # find all tashes

        # what is legal move






class Board:

    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def add_token_to_board(self, rows, columns, token):
        if (rows >= 0 and rows <= len(self.board)) and (columns >= 0 and columns <= len(self.board[0]) -1):
            self.board[rows][columns] = token
        else:
            print("token is out of bounds")
        return self.board

    def print_board(self):
        for row in self.board:
            print('|'.join(row))

    def is_board_full(self):
        for row in self.board:
            if "-" in row:
                return False
        return True
















if __name__ == '__main__':

    board = Board()

    board.add_token_to_board(0, 0, 'X')
    board.add_token_to_board(1, 1, '0')
    board.add_token_to_board(1, 2, 'X')
    board.print_board()

    print(board.is_board_full())




    #print(results)
    #print()





















if __name__ == '__main__':
    pass