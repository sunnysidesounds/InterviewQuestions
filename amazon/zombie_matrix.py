"""
    Given a 2D grid, each cell is either a zombie or a human.
    Zombies can turn adjacent (up/down/left/right) human beings into zombies every day.
    Find out how many days does it take to infect all humans?

    Input:
    matrix, a 2D integer array where a[i][j] = 1 represents a zombie on the cell and a[i][j] = 0 represents a human on the cell.

    Output:
    Return an integer represent how many days does it take to infect all humans.
    Return -1 if no zombie exists.



    Example :
    Input:
    [[0, 1, 1, 0, 1], <-- 0,0 - (0,1) - (0,2) - 0,3 - (0,4)
    [0, 1, 0, 1, 0], <-- 1,0 - (1,1) - 1,2 - (1,3) - 1,4
    [0, 0, 0, 0, 1], <-- 2,0 - 2,1 - 2,2 - 2,3 - (2,4)
    [0, 1, 0, 0, 0]]m<-- 3,0 - (3,1) - 3,2 - 3,3 - 3,4

    directions=[[1,0],[-1,0],[0,1],[0,-1]] bottom, top, right, left

    Output:
    2

    Explanation:
    At the end of the day 1, the status of the grid:
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1]]

    At the end of the day 2, the status of the grid:
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]

"""

def human_days(matrix):
    if len(matrix) == 0:
        return 0

    days = 0
    queue = []
    row_length = len(matrix)
    column_length = len(matrix[0])

    # add zombies to the queue
    for row in range(row_length):
        for column in range(column_length):
            if matrix[row][column] == 1:
                queue.append((row, column))

    direction_shift = [[1,0],[-1,0],[0,1],[0,-1]] # bottom, top, right, left shift

    while True:
        sub_queue = []
        while len(queue) > 0:
            (row, column) = queue.pop()
            print("- row, column: {0}, {1}".format(row, column))
            for d in direction_shift:
                new_row = row + d[0]
                new_column = column + d[1]
                # Make sure the indexes are within the range of the matrix
                # and if the grid item is a human == 0
                if new_row < row_length and new_column < column_length and matrix[new_row][new_column] == 0:
                    matrix[new_row][new_column] = 1
                    sub_queue.append((new_column, new_column))

                print("- ni, nj {0} {1}".format(new_row, new_column))
                print()
        queue = sub_queue
        days += 1

        if not queue:
            break

    return days




if __name__ == '__main__':
    matrix = [[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0]]


    print(human_days(matrix))