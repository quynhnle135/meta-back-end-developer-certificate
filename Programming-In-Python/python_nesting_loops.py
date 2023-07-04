import time

start_time = time.time()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0

# outer loop
for x in list1:
    count += 1
    # inner loop
    for y in list2:
        count += 1

print(count)

# outer loop
for i in range(10):
    # inner loop
    for j in range(10):
        print(j, end=" ")
    print()

print(round(time.time() - start_time, 2))

# Exercise: Use Control flow and loops to solve a problem
num_list = [33, 42, 5, 66, 77, 22, 16, 79,
            36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

for num in num_list:
    if num > 45:
        print("Over 45: ", num)
    else:
        print("Under 45: ", num)

for i in range(len(num_list)):
    if num_list[i] == 36:
        print("Number 36 found at index: ", i)

count = 0
for num in num_list:
    count += 1
    print(count)
    if num == 36:
        print("Found it")
        break
