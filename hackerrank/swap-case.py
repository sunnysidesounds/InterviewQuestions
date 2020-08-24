def swap_case(string):
    swapped_string = ""
    index = 0
    for character in string:
        if character.isupper():
            character = character.lower()
        else:
            character = character.upper()
        swapped_string += character

        index += 1


    return swapped_string


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)