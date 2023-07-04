my_str = "Looping"

for c in my_str:
    print(c, end=" ")

favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramissu', 'Chocolate Cake']
print()
for item in favorites:
    print(item, end=', ')

print()
for i in range(10):
    print("Looping...", i)


print()
count = 0
while count < 11:
    print(count)
    count += 1

count = 0
while count < len(favorites):
    print("I like this dessert: ", favorites[count])
    count += 1
