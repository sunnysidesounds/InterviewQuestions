



def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    return False






if __name__ == '__main__':

    results = is_palindrome("abcdcbad")
    print(results)





