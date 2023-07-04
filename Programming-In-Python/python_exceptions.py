def divide_by(a, b):
    return a / b


# zero division error
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")

# index error
items = [1, 2, 3, 4, 5]
try:
    item = items[6]
    print(item)
except:
    print("The index does not exist in the list")
