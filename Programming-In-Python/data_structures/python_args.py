def sum(a, b):
    return a + b


print(sum(1, 2))


def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_of(1, 2, 3, 4, 5))
