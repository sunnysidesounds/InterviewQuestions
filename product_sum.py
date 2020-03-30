"""

Write a function that takes in a "special" array and returns its product sum.
A "special" array is a non-empty array that contains either integers or other "special" arrays.
The product sum of a "special" array is the sum of its elements, where "special" arrays inside
it should be summed themselves and then multiplied by their level of depth. For example,
the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

Sample input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample output: 12 (calculated as: (5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)))

Initialize the product sum of the "special" array to 0. Then, iterate through all of the array's elements;
if you come across a number, add it to the product sum; if you come across another "special" array, recursively
call the productSum function on it and add the returned value to the product sum. How will you handle multiplying
the product sums at a given level of depth?

"""
def product_sum(array):
    return calulate_product_sum(array, 1)


def calulate_product_sum(source_array, multiplier):
    psum = 0
    for item in source_array:
        if isinstance(item, list):
            psum += calulate_product_sum(item, multiplier + 1)
        else:
            psum += item
    return psum * multiplier
    pass


if __name__ == '__main__':
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    results = product_sum(array)
    print(results)