
"""
Given an expression string exp, write a program to examine whether the pairs and the
orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.

Example:

Input: exp = “[()]{}{[()()]()}”
Output: Balanced

Input: exp = “[(])”
Output: Not Balanced


"""


stack = []


def is_balanced_expression(string):
    stack = []
    for expression in string:
        if is_open_expression(expression):
            stack.append(expression)
        else:
            if len(stack) == 0:
                return False

            current_expression = stack.pop()
            matching_expression = current_expression + expression
            if not has_matching_expression(matching_expression):
                return False
    if len(stack) > 0:
        return False
    else:
        return True


def has_matching_expression(expression):
    return True if expression == '[]' or expression == '{}' or expression == '()' else False


def is_open_expression(expression):
    return True if expression == '[' or expression == '{' or expression == '(' else None







if __name__ == '__main__':
    results = is_balanced_expression("[")
    print(results)


