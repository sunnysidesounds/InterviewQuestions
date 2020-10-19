from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:

    current_count = 0
    max_count = 0
    for i in range(len(nums)):
        val = nums[i]
        if val == 1:
            current_count = current_count + 1
            if current_count > max_count:
                max_count = current_count
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 0

    return max_count






if __name__ == '__main__':

    results = findMaxConsecutiveOnes([1])
    print(results)
