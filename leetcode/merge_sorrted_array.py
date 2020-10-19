from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    copy_of_nums1 = nums1[:m]
    nums1[:] = []

    index1 = 0
    index2 = 0

    while index1 < m and index2 < n:
        if copy_of_nums1[index1] < nums2[index2]:
            nums1.append(copy_of_nums1[index1])
            index1 += 1
        else:
            nums1.append(nums2[index2])
            index2 += 1

    if index1 < m:
        nums1[index1 + index2:] = copy_of_nums1[index1:]
    if index2 < n:
        nums1[index1 + index2:] = nums2[index2:]


    print(nums1)









if __name__ == '__main__':

    num1 = [1,2,3,0,0,0]
    m = 3
    num2 =  [2,5,6]
    n = 3

    merge(num1, m, num2, n)

    print(num1)

