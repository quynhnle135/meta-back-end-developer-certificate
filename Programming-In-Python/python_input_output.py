# Python's format function
print("My favorite fruits are {0} and {1}".format("Lychee", "Banana"))

first_fav_fruit = "Lychee"
second_fav_fruit = "Banana"
print(f"My favorite fruits are {first_fav_fruit} and {second_fav_fruit}")

user_name = input("Please enter your name: ")
user_year = input("Please enter your birth year: ")

print(f"Hi, {user_name}! You are {str(2023 - int(user_year))} years old")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))

print(f"Sum of {num_1} and {num_2}: {str(num_1 + num_2)}")
