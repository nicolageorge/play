def palindrome(n, c):
    a=''.join(set(c))
    return "{}{}".format(a, a[::-1])
