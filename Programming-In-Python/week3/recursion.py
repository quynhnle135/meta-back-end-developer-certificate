def find_factorial(n):
    if n <= 1:
        return n
    return n * find_factorial(n - 1)


print(find_factorial(5))


def sum(n):
    if n == 1:
        return 0
    return n + sum(n - 1)


print(sum(5))
