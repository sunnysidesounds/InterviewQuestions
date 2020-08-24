


"""

Write a function that takes in a string made up of brackets ("(", "[", "{", ")", "]", and "}") and other
optional characters. The function should return a boolean representing whether or not the string is balanced
in regards to brackets.

A string is said to be balanced if it has as many opening brackets of a given type
as it has closing brackets of that type and if no bracket is unmatched. Note that a closing bracket cannot
match a corresponding opening bracket that comes after it. Similarly, brackets cannot overlap each
other as in "[(])".

"""


def is_balanced_brackets(string):
    # example: ("(", "[", "{", ")", "]", and "}")
    # is balanced is has same opening brackets as closing brackets of that character type.
    # closing bracket ) cannot match a corresponding opening bracket ( that comes after it, )(
    # no bracket overlaps, [(]).

    # assumptions:
    # if we run into a closing bracket first, with no prior opening brakcet it isn't balanced, return false, ]()
    stack = []
    for char in string:
        # check if the character is an open bracket { [ ( and append to the stack (list)
        if is_opening_bracket(char):
            stack.append(char)
        # else if must be a closing bracket
        else:
            # if stack is empty return false because this would be an unbalanced string.
            if len(stack) == 0:
                return False
            # otherwise, pop the item from the top of the stack
            opening_bracket = stack.pop()
            # combine the popped item and concatinate it with the current iterated character
            string_to_match = opening_bracket + char
            # The check if this newly constructed string has a matching bracket {}, [], ()
            if not has_matching_brackets(string_to_match):
                return False

    if len(stack) > 0:
        return False

    return True


def is_opening_bracket(b):
    return b in ['(', '{', '[']


def has_matching_brackets(string):
    return True if string == "[]" or string == "{}" or string == "()" else False






if __name__ == '__main__':

    true_str = "([])(){}(())()()"
    false_str = "()()[{()})]"
    results = is_balanced_brackets(true_str)
    print(results)



