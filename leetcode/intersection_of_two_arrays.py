


def intersect(num1, num2):
    num1.sort()
    num2.sort()
    results = []

    idx1 = 0
    idx2 = 0

    while idx1 < len(num1) and idx2 < len(num2):
        if num1[idx1] == num2[idx2]:
            results.append(num1[idx1])
            idx1 += 1
            idx2 += 1
        elif num1[idx1] < num2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return results


def intersect_2(num1, num2):

    num1_map = {}
    results = []

    for num in num1:
        if num not in num1_map:
            num1_map[num] = 1
        else:
            num1_map[num] += 1

    for num in num2:

        if num in num1_map and num1_map[num] > 0:
            results.append(num)
            num1_map[num] = num1_map[num] - 1

    return results










if __name__ == '__main__':


    r1 = intersect_2([4,9,5], [9,4,9,8,4])
    print(r1)
