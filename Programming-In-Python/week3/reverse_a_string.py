# reverse a string with list comprehension str[start:stop:step]

my_string = "hello world"
print(my_string[::-1])

# recursion


def reverse_string_recursion(string):
    if len(string) == 0:
        return string
    else:
        return string[1:] + string[0]


print(reverse_string_recursion(my_string))
