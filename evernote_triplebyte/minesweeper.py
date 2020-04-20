"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents
an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left,
right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed
square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

- If a mine ('M') is revealed, then the game is over - change it to 'X'.
- If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all
of its adjacent unrevealed squares should be revealed recursively.
- If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
representing the number of adjacent mines.
- Return the board when no more squares will be revealed.


- 'M' represents an unrevealed mine
- 'E' represents an unrevealed empty square
- 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines
- digits ('1' to '8') represents how many mines are adjacent to this revealed square
- 'X' represents a revealed mine


Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:



Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the
unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
Accepted

- Assume a click is always within bounds of the bpard



- If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all
of its adjacent unrevealed squares should be revealed recursively.

- If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
representing the number of adjacent mines.


"""
def update_board(board, click):
    visited = [[False for value in row] for row in board]
    return update_board_helper(board, click, visited)


def update_board_helper(board, click, visited):
    row_length = len(board)
    columm_length = len(board[0])

    if all_is_visited(visited):
        return board
    else:
        for row in range(row_length):
            for column in range(columm_length):
                click_on_board = board[click[0]][click[1]]
                if click_on_board == 'M':
                    board[click[0]][click[1]] = 'X'
                    return board
                if click_on_board == 'E':
                    neigbors = get_neigboring_nodes(row, column, board, visited)



def all_is_visited(visited):
    has_all = True
    for visit in visited:
        if not all(visit):
            return False
    return has_all


def get_neigboring_nodes(row, column, board, visited):
    neigbors = []
    # left:
    if row > 0 and not visited[row - 1][column]:
        neigbors.append([row - 1, column])
    # right:
    if row < len(board) - 1 and not visited[row + 1][ column]:
        neigbors.append([row + 1, column])
    # top:
    if column > 0 and not visited[row][column - 1]:
        neigbors.append([row, column - 1])
    # bottom
    if column < len(board) - 1 and not visited[row][column + 1]:
        neigbors.append([row, column + 1])
    return neigbors

if __name__ == '__main__':

    tests = [
        # Test 1
        {"board": [['E', 'E', 'E', 'E', 'E'],
                    ['E', 'E', 'M', 'E', 'E'],
                    ['E', 'E', 'E', 'E', 'E'],
                    ['E', 'E', 'E', 'E', 'E']],
         "click": [3, 0],
         "expected": [['B', '1', 'E', '1', 'B'],
                      ['B', '1', 'M', '1', 'B'],
                      ['B', '1', '1', '1', 'B'],
                      ['B', 'B', 'B', 'B', 'B']]
         },
        # Test 2
        {"board": [['B', '1', 'E', '1', 'B'],
                   ['B', '1', 'M', '1', 'B'],
                   ['B', '1', '1', '1', 'B'],
                   ['B', 'B', 'B', 'B', 'B']],
         "click": [1, 2],
         "expected": [['B', '1', 'E', '1', 'B'],
                      ['B', '1', 'X', '1', 'B'],
                      ['B', '1', '1', '1', 'B'],
                      ['B', 'B', 'B', 'B', 'B']]
         }

    ]

    counter = 1
    for test in tests:
        results = update_board(test['board'], test['click'])
        print("{0} test ".format(counter), results == test['expected'])

        counter += 1

