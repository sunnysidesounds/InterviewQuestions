
# Given two strings s and t , write a function to determine if t is an anagram of s.



def is_valid_anagram(s, t):

    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        char = s[i]
        if char not in s_dict:
            s_dict[char] = 1
        else:
            s_dict[char] += 1

    for i in range(len(t)):
        char = t[i]
        if char not in t_dict:
            t_dict[char] = 1
        else:
            t_dict[char] += 1

    return s_dict == t_dict













if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"

    s1 = 'car'
    t1 = 'rat'

    r = is_valid_anagram(s1, t1)
    print(r)
