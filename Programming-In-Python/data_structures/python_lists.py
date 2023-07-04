list1 = [1, 2, 3, 4, 5]
# lists are based on index
print(list1[2])  # 3

list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 40.22]

list4 = [list1, list2, list3]

# print(len(list4))
# for item in list4:
#     print(item)

# insert function in list
list1.insert(5, "Quinn")
print(list1)

list1.append("Johnathan")
print(list1)

# remove item at index 4
list1.pop(4)
print(list1)

# remove item at the last index
list1.pop()
print(list1)
