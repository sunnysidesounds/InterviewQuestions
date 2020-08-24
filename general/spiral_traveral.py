def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row-1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dir = 0

    while (top <= bottom and left <=right):
        if dir ==0:
            for i in range(left,right+1): # moving left->right
                print (arr[top][i], end=" ")

            # Since we have traversed the whole first
            # row, move down to the next row.
            top +=1
            dir = 1

        elif dir ==1:
            for i in range(top,bottom+1): # moving top->bottom
                print (arr[i][right], end=" ")

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -=1
            dir = 2

        elif dir ==2:
            for i in range(right,left-1,-1): # moving right->left
                print (arr[bottom][i], end=" ")

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -=1
            dir = 3

        elif dir ==3:
            for i in range(bottom,top-1,-1): # moving bottom->top
                print (arr[i][left], end=" ")
            # Since we have traversed the whole first
            # column, move down to the next column.
            left +=1
            dir = 0















def spiralTraverse(array):
    # Write your code here.
    top = 0
    bottom = len(array) - 1
    left = 0
    right = len(array[0]) - 1

    traverse_direction = 0
    output_array = []

    while top <= bottom and left <= right:
        if traverse_direction == 0: # left to right
            for i in range(left, right + 1, 1):
                value = array[top][i]
                output_array.append(value)

            top += 1
            traverse_direction += 1

        elif traverse_direction == 1: # top to bottom
            for i in range(top, bottom+1, 1):
                value = array[i][right]
                output_array.append(value)

            right -= 1
            traverse_direction += 1

        elif traverse_direction == 2: # right to left
            for i in range(right, left - 1, -1):
                value = array[bottom][i]
                output_array.append(value)

            bottom -= 1
            traverse_direction += 1

        elif traverse_direction == 3: # bottom to top
            for i in range(bottom, top - 1, -1):
                value = array[i][left]
                output_array.append(value)

            left += 1
            traverse_direction = 0



    return output_array



# Driver code
# Change the following array and the corresponding row and
# column arguments to test on some other input
if __name__ == '__main__':

    array = [[1,2,3,4],
             [12,13,14,5],
             [11,16,15,6],
             [10,9,8,7]]

    spiralMatrixPrint(4, 4, array)
    print("\n")
    v = spiralTraverse(array)
    print(v)