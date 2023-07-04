sample_dict = {1: "coffee", 2: "Tea", 3: "Juice"}

print(sample_dict[1])

# update value in dictionary
sample_dict[2] = 'Smoothie'
print(sample_dict)

# print out the keys in dictionary
for item in sample_dict:
    print(item)

# print out the item in dictionary
for values in sample_dict.values():
    print(values)

# add new key-value pair to dictionary
sample_dict[4] = 'Coconut water'
print(sample_dict)

# length of dictionary
print(len(sample_dict))

for item in sample_dict.items():
    print(item)

for key, value in sample_dict.items():
    print(str(key) + " : " + value)

print()
