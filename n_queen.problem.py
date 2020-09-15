
all_possible_solutions = []


def is_safe(solutions, row, column, n):
    if solutions[column] != -1:
        return False
    else:
        left_diagonal = row - column
        right_diagonal = row + column
        for i in range(0, n):
            if solutions[i] != -1:
                if (solutions[i] + i == right_diagonal) or (solutions[i] - i == left_diagonal):
                    return False

        return True


def solve(n, solutions, postion):
    if postion == n:
        print(solutions)
    else:
        for i in range(0, n):
            if is_safe(solutions, postion, i, n):
                solutions[i] = postion
                solve(n, solutions, postion + 1)
                solutions[i] = -1


def main(n):
    solve(n, [-1 for y in range(n)], 0)
    return all_possible_solutions


if __name__ == "__main__":
    n = 4
    results = main(n)
    print(results)