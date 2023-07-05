# algorithm for palindrome

def is_palindrome(str):
    start = 0
    end = len(str) - 1
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True


print(is_palindrome("quinn"))
print(is_palindrome('racecar'))
