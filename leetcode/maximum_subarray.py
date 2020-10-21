import unittest

def get_max_subarray(nums):
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(len(nums)):
        extend_subarray = max_ending_here + nums[i]
        new_subarray = nums[i]
        max_ending_here = max(extend_subarray, new_subarray)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def get_max_subarray_2(nums):
    subarray_max = 0
    max_at_point = 0

    for i in range(len(nums)): # iterate over our nums
        max_at_point = max_at_point + nums[i] # adding up our values
        if max_at_point < 0: # set max_at_point to zero if less than zero
            max_at_point = 0
        if subarray_max < max_at_point: # set subarray_max to the max_at_point when the subarray_max is less than max_at_point
            subarray_max = max_at_point

    return subarray_max

def get_max_subarray_3(array):

    max_so_far = 0
    max_ending_here = 0

    for i in range(len(array)):
        max_extend =  max_ending_here + array[i]
        new_subarray = array[i]
        max_ending_here = max(max_extend, new_subarray)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

class TestMaximumSubArray(unittest.TestCase):

    def test_1(self):
        output = get_max_subarray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(output, 6, 'Maximum Subarray should be value of 6')
        pass

    def test_2(self):
        output = get_max_subarray([1])
        self.assertEqual(output, 1, 'Maximum Subarray should be value of 1')
        pass

    def test_3(self):
        output = get_max_subarray([0])
        self.assertEqual(output, 0, 'Maximum Subarray should be value of 0')
        pass

    def test_4(self):
        output = get_max_subarray([-1])
        self.assertEqual(output, -1, 'Maximum Subarray should be value of -1')
        pass

    def test_5(self):
        output = get_max_subarray([-2147483647])
        self.assertEqual(output, -2147483647, 'Maximum Subarray should be value of -2147483647')
        pass

if __name__ == '__main__':
    unittest.main()