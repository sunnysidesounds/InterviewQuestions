"""
  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.

  A peak is defined as three or more adjacent integers in the array that are
  strictly increasing until they reach a tip (the highest value in the peak), at
  which point they become strictly decreasing.

  For example, the integers <span>1, 4, 10, 2</span> form a peak, but the
  integers <span>4, 0, 10</span> don't and neither do the integers
  <span>1, 2, 2, 0</span>. Similarly, the integers <span>1, 2, 3</span> don't
  form a peak because there aren't any strictly decreasing integers after the

Sample Input
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

Sample Output
6 // 0, 10, 6, 5, -1, -3

"""

def longest_peak(array):
    longest_peak_value = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i] > array[i + 1]:
            left = i - 2
            while left >= 0 and array[left] < array[left + 1]:
                left -= 1

            right = i + 2
            while right < len(array) and array[right] < array[right - 1]:
                right += 1

            current_peak_value = abs(right - left - 1)

            if current_peak_value > longest_peak_value:
                longest_peak_value = current_peak_value
        i += 1

    return longest_peak_value



    pass


if __name__ == '__main__':

    test_data = [
        {"input": [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3], "expected": 6},
        {"input": [1, 3, 2], "expected": 3},
        {"input": [1, 2, 3, 4, 5, 1], "expected": 6},
        {"input": [1, 2, 3, 4, 5, 6, 10, 100, 1000], "expected": 0},


    ]
    count = 1
    for data in test_data:
        result = longest_peak(data['input'])
        print("PASSED TEST {count}".format(count=count), result == data['expected'])

        count += 1