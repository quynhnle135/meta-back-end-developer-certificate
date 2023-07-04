my_tuple = (1, 2, 'string', 4.5, True, 'string')
print(len(my_tuple))
print(type(my_tuple[2]))
print(my_tuple.count('string'))

print(my_tuple[1])
print("---")
for item in my_tuple:
    print(item, end=" ")
