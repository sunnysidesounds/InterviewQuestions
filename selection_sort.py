"""

  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Selection Sort algorithm to sort the array.

  If you're unfamiliar with Selection Sort, we recommend watching the Conceptual
  Overview section of this question's video explanation before starting to code.

  Hint:

  Divide the input array into two subarrays in place. The first subarray should
  be sorted at all times and should start with a length of 0, while the second
  subarray should be unsorted.

  Find the smallest (or largest) element in the unsorted subarray and insert it into
  the sorted subarray with a swap.

  Repeat this process of finding the smallest (or largest) element in the unsorted subarray
  and inserting it in its correct position in the sorted subarray with a swap until
  the entire array is sorted.


    Sample Input:  = [8, 5, 2, 9, 5, 6, 3]
    Sample Output: = [2, 3, 5, 5, 6, 8, 9]




"""


def selection_sort(array):

    for i in range(len(array)-1):
        minimum = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]

    return array

    pass



if __name__ == '__main__':

    tests_data_array = [
        {"test": [8, 5, 2, 9, 5, 6, 3], "expected": [2, 3, 5, 5, 6, 8, 9]},
        {"test": [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8],
         "expected": [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10]},
        {"test": [1], "expected": [1]},


    ]

    counter = 1
    for data in tests_data_array:
        results = selection_sort(data['test'])
        print("PASSED Test {counter}: {results}".format(counter=counter, results=results), results == data['expected'])

        counter += 1



