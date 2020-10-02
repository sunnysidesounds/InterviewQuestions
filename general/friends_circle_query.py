
def initialize_union(my_dict, x, y):
    if x not in my_dict:
        my_dict[x] = x
    if y not in my_dict:
        my_dict[y] = y

def initialize_size(my_dict, x, y):
    if x not in my_dict:
        my_dict[x] = 1
    if y not in my_dict:
        my_dict[y] = 1

def get_root(arr, i):
    while arr[i] != i:
        i = arr[i]
    return i



def find(arr, a, b):
    if get_root(arr, a) == get_root(arr, b):
        return True
    else:
        return False


if __name__ == '__main__':
    queries = [
        [1, 2],
        [3, 4],
        [1, 3],
        [5, 7],
        [5, 6],
        [7, 4]
    ]

    queries_2 = [
        [0, 1],
        [1, 2],
        [3, 2]
    ]

    queries_3 = [
        [1, 2],
        [1, 3]
    ]

    queries_4 = [
        [1000000000, 23],
        [11, 3778],
        [7, 47],
        [11, 1000000000]

    ]


    queries_5 = [
        [6, 4],
        [5, 9],
        [8, 5],
        [4, 1],
        [1, 5],
        [7, 2],
        [4, 2],
        [7, 6]
    ]

    """
    2
    2
    3
    3
    6
    6
    8
    8
    """




    my_queries = queries_5

    union_find_dict = {}
    size_dict = {}
    results = []
    my_union = []
    largest_group = 0

    # report the size of the largest friend circle (the largest group of friends)
    for query in my_queries:
        initialize_union(union_find_dict, query[0], query[1])
        initialize_size(size_dict, query[0], query[1])
        root_a = get_root(union_find_dict, query[0])
        root_b = get_root(union_find_dict, query[1])

        if root_a != root_b:
            if size_dict[root_a] > size_dict[root_b]:
                union_find_dict[root_b] = root_a
                size_dict[root_a] = size_dict[root_a] + size_dict[root_b]
            else:
                union_find_dict[root_a] = root_b
                size_dict[root_b] = size_dict[root_a] + size_dict[root_b]
            largest_group = max(largest_group, max(size_dict[root_a], size_dict[root_b]))

        results.append(largest_group)

    print(results)





