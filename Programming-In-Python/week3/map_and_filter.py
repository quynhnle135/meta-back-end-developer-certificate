menu = ['espresso', 'mocha', 'latte', 'cappuchino', 'cortado', 'americano']


def drink_starts_with_c(drinks):
    for drink in drinks:
        if drink[0] == 'c' or drink[0] == "C":
            print(drink)


def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)

print("----")
a = [[96], [69]]
print("".join(list(map(str, a))))

z = ['alpha', 'bravo', 'charlie']
new_z = [i[0] * 2 for i in z]
print(new_z)

print("----")
