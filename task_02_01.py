def is_palindrome(s):
    s = str(s).replace(' ', '').lower()
    i = 0
    j = len(s) - 1
    is_palindrom = True
    while i < j:
        if s[i] != s[j]:
            is_palindrom = False
        i += 1
        j -= 1


