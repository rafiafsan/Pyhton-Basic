# #Dictonaries : key value pairs.
# #Sets: unique values no duplicate

# person = {
#     "Name" : "Rafi",
#     "Age"  : "25",
#     "Position": "Developer"
#     }
# print(f"Persons name : {person['Name']}")
# print(f"Persons age and position : {person['Age']} and {person['Position']}")

# person["Country"] = "Bangladesh"
# person["Age"] = 30
# print(f"Updated persons information: {person}")

# keys = person.keys()
# values = person.values()
# items = person.items()
# print(f"Persons keys : {keys} and values: {values}")
# print(f"Items: {items}")

# for key , values in person.items():
#     print(f"{key} : {values}")

# del person["Country"]
# print(person)

#Sets:

numbers = {"10","20","30","40","50","60","70"}
colors = {"Red","Green","Blue","Yellow","Orange", "Yellow"}

print(f"Colors : {colors}")
numbers.add("80")
numbers.add("90")
numbers.add("100")
print(f"Numbers: {numbers}")
print(f"Numbers: {numbers}")
numbers.remove("10")
numbers.discard("100")
print(numbers)

numbers1 = {"10","20","30","40"}
numbers2 = {"40","50","60","70"}
merged_numbers = numbers1.union(numbers2)
print(f"Merged numbers : {merged_numbers}")
same_numbers = numbers1.intersection(numbers2)
print(f"Same numbers: {same_numbers}")

subtraction = numbers1.difference(numbers2)

print(f"Difference : {subtraction}")