set_a = {1, 2, 3, 4, 5}
print(set_a)

set_a.add(6)
print(set_a)

set_b = {4, 5, 6, 7, 8}
print(set_a.union(set_b))

set_c = {4, 4, 4, 4, 4}
print(set_c)

print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a - set_b)
print(set_a.symmetric_difference(set_b))
