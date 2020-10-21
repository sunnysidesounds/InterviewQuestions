import unittest


def distinct_stairs_climbed_3(n):
    if n <= 1:
        return 1
    d_ways = [0 for _ in range(n + 1)]  # + 1 to include zero as distinct step
    d_ways[0] = 1  # zero steps, one distinct step
    d_ways[1] = 1  # one step, one distinct step
    for i in range(2, n + 1):
        d_ways[i] = d_ways[i - 2] + d_ways[i - 1]

    return d_ways[n]


def distinct_stairs_climbed_2(num, measurement):

    num = num + 1
    results = [0 for x in range(num)]
    results[0] = 1
    results[1] = 1
    dict = []

    for i in range(2, num):
        j = 1
        while j <= measurement and j <= i:
            results[i] = results[i] + results[i - j]
            dict.append(results[i])
            j += 1
    return results[num - 1]





# O(2^n)
def distinct_stairs_climbed_1(num):
    return distinct_stairs_climbed_helper(num + 1)


def distinct_stairs_climbed_helper(num):
    if num <= 1:
        return num
    return distinct_stairs_climbed_helper(num - 1) + distinct_stairs_climbed_helper(num - 2)


class TestClimbingStairs(unittest.TestCase):

    def test_1(self):
        output = distinct_stairs_climbed_1(2)
        self.assertEqual(output, 2, "This should equal 2")

    def test_2(self):
        output = distinct_stairs_climbed_1(3)
        self.assertEqual(output, 3, "This should equal 3")

    def test_4(self):
        output = distinct_stairs_climbed_1(4)
        self.assertEqual(output, 5, "This should equal 5")

    def test_5(self):
        output = distinct_stairs_climbed_2(4, 2)
        self.assertEqual(output, 5, "This should equal 5")

    def test_6(self):
        output = distinct_stairs_climbed_3(4)
        self.assertEqual(output, 5, "This should equal 5")

    def test_7(self):
        output = distinct_stairs_climbed_3(3)
        self.assertEqual(output, 3, "This should equal 3")


if __name__ == '__main__':
    unittest.main()



