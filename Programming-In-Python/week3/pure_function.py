my_list = [1, 2, 3]


def add_to_list(item):
    my_list.append(item)
    return my_list


# new_list = add_to_list(4)

# print(my_list)
# print(new_list)

# update function add_to_list function


def add_to_list_modified(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list


print(my_list)
print(add_to_list_modified(my_list, 4))
print(my_list)
