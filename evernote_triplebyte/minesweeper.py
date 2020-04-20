"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents
an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left,
right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed
square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

DONE - If a mine ('M') is revealed, then the game is over - change it to 'X'.
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

DONE - If a mine ('M') is revealed, then the game is over - change it to 'X'.

- If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all
of its adjacent unrevealed squares should be revealed recursively.

- If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
representing the number of adjacent mines.


"""
def get_neighbors(board, click):
    click_x, click_y = click[0], click[1]
    n, m = len(board), len(board[0])
    for dx in (-1, 0, +1):
        for dy in (-1, 0, +1):
            nx, ny = click_x + dx, click_y + dy
            if 0 <= nx < n and 0 <= ny < m and not (nx == click_x and ny == click_y):
                yield nx, ny


def update_board(board, click):
    current_cell = board[click[0]][click[1]]
    if current_cell == 'M':
        board[click[0]][click[1]] = 'X'
    elif current_cell == 'E':
        m_ajustments = sum(board[click[0]][click[1]] == 'M' for i, j in get_neighbors(board, click))
        if m_ajustments == 0:
            board[click[0]][click[1]] = 'B'
            for neighbor in get_neighbors(board, click):
                update_board(board, neighbor)
        else:
            board[click[0]][click[1]] = str(m_ajustments)

    return board





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
        print(results)

        counter += 1

