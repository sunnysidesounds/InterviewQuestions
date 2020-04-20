def twoNumberSum(array, targetSum):
    lookup_map = {}
    if len(array) <= 0:
        return []

    index = 0
    for item in array:
        lookup_map[item] = index
        index += 1

    for item in array:
        offset = targetSum - item
        if offset in lookup_map and item in lookup_map:
            offset_index = lookup_map[offset]
            item_index = lookup_map[item]
            if offset_index != item_index:
                return [offset, item]

    return []


if __name__ == '__main__':
    re = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(re)