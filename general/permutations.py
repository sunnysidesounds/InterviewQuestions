"""

  Write a function that takes in an array of unique integers and returns an
  array of all permutations of those integers in no particular order.
    If the input array is empty, the function should return an empty array.

Sample Input
array = [1, 2, 3]
Sample Output<
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]



"""


def get_permutations(array):
    all_perms = []
    permutate(0, array, all_perms)
    return all_perms


def permutate(i, arr, perms):
    if i == len(arr) - 1:
        copy_of_array = list(arr) # take copy of array
        perms.append(copy_of_array)
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]  # swap
            permutate(i + 1, arr, perms)
            arr[j], arr[i] = arr[i], arr[j]  # swap back



if __name__ == '__main__':

    tests =[
        {"array": [1, 2, 3], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}
    ]
    counter = 1
    for test in tests:
        results = get_permutations(test['array'])
        print("Test {0}".format(counter), results == test['expected'])
        print(results)

        counter += 1