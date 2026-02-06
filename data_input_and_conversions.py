#input functions always returns a string, so we neet to convert it to the desired data type if we want to perform any operations.

name =  input(f"Enter your name: ")
# age = input(f"Enter your age: ")
age = int(input(f"Enter your age:"))
print(f"Your name is {name} and you are {age} years old.")

x : int = 10
new_age = age + x
print(f"Your age after {x} years will be {new_age}")

price = float(input(f"Enter the price of an item: "))
sold : bool = input(f"Is the item sold? (yes/no) : ")

print(f"price : {price} and has been sold : {sold}")