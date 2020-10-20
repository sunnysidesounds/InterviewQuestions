


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

import itertools
import random

class Solution:

    def __init__(self, nums):
        self.num_list = nums


    def reset(self):
        return self.num_list


    def shuffle(self):
        copy_of_num_list = self.num_list.copy()
        random.shuffle(copy_of_num_list)
        return copy_of_num_list







if __name__ == '__main__':

    r = Solution([1, 2, 3])
    r.shuffle()
