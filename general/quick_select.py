"""
Write a function that takes in an array of distinct integers as well as an integer k and returns
the kth smallest number in that array in linear time, on average. The array could be sorted,
but isn't necessarily so.


"""

def quickselect(array, k):
    # Write your code here.
    pass


def quickselect_cheat(array, k):
    array.sort()
    if len(array) >= k:
        return array[k-1]
    else:
        return array[0]






if __name__ == '__main__':
     #arr = [8, 5, 2, 9, 7, 6, 3]
     arr = [43, 24, 37]
     #arr = [1]
     k = 4
     results = quickselect(arr, k)
     results = quickselect_cheat(arr, k)
     print(results)