from math import pi
menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


for item in menu.values():
    print(item['price'])


print(pi)

names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names)


sample_dict = {1: 'c', 2: 'T', 3: 'J'}

for x in sample_dict:
    print(x)

for x in range(1, 4):
    print(int(str(float(x))))
