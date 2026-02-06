# #listes = ordered, mutable, allows duplicate elements
# #tuples = ordered, immutable, allows duplicate elements
# #immutable = cannot be changed after creation
# #mutable = can be changed after creation

# #LISTS
languages = ["Python", "Java", "C++", "JavaScript", "Ruby", "Python"]
ages = [25, 30, 35, 40, 45]
mixed = ["Hello", 123, 3.14, True, None]

print(f"programming languages: {languages}")
print(f"ages: {ages}")
print(f"Mixed: {mixed}")

print(f"First two languages: {languages[0:2]}")
print(f"Last two ages: {ages[-2:]}")
print(f"Every other element in mixed: {mixed[::2]}")
print(f"Reversed languages: {languages[::-1]}")
print(f"Inner ages: {ages[1:4]}")


#modify list

languages[3] = "TypeScript"
print(F"Modified languages: {languages}")
languages.append("Go")
languages.insert(2, "C#")
print(f"Modified languages: {languages}")

ages.remove(35)
print(f"Modified ages: {ages}")
x = ages.pop()
print(f"Modified ages: {ages}")
print(f"Popped value: {x}")

print(f"length of languages: {len(languages)}")
print(f"length of ages: {len(ages)}")
print(f"count of 'Python' in languages= {languages.count('Python')}")
print(f"index of 'Java' in languages: {languages.index('Java')}")

#Checking for membership
print(f"'Python' in languages: {'Dart' in languages}")
print(f"'C++' in languages: {'C++' in languages}")
print(100 in ages)

#TUPLES
coordinates = (10,20)
red  = (255,0,0)

print(f"Coordinates: {coordinates}")
print(f"Number of 255 in red: {red.count(255)}")
print(f"Index of 0in red: {red.index(0)}")

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(f"matrix: {matrix}")
print(f"Five in matrix: {matrix[1][1]}")


students = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
print(f"Students: {students}")
print(f"First student name: {students[0][0]}")
print(f"Second student age: {students[1][1]}")

