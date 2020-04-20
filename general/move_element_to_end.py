"""

  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.

  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.

    Sample Input
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2

Sample Output
[1, 3, 4, 2, 2, 2, 2, 2] // the numbers 1, 3, and 4 could be ordered differently

Following Hint #2, set two pointers at the start and end of the array, respectively.
Move the right pointer inwards so long as it points to the integer to move, and move
the left pointer inwards so long as it doesn't point to the integer to move. When both
pointers aren't moving, swap their values in place. Repeat this process until the pointers
pass each other.


"""


def move_element_to_end(array, toMove):
    left = 0
    right = len(array) - 1

    while left < right:

        while left < right and array[right] == toMove:
            right -= 1

        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1

    return array



    pass



if __name__ == '__main__':
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2

    results = move_element_to_end(array, toMove)
    print(results)