
# For Loops
print(f"Counting numbers 1 to 5 using a for loop:")

for i in range(1,6):
    print(f"Number: {i}", end = " ")
    #used end=" " to print numbers in the same line with a space between them.


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(f"-{i}")

#Enumerate funtion is used to get the index value of the current item in the loop.
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}", end= " ")
    print(f"\n") #used to print a new line after each iteration of the outer loop.

# while loops

print(f"Counting number 1 to 5 using a while loop:")
i= 5
while i > 0:
    print(f"Number: {i}")
    i -= 1

lottery_number = 7
guess  = int(input(f"Enter first guess: "))
attempts  = 0

while guess!=lottery_number and attempts < 7:
    attempts += 1
    print(f"Attempts: {attempts} and Guess: {guess}")
    if guess < lottery_number:
        print(f"Too low")
    else:
        print(f"Too High")
    guess = int(input(f"Enter No.{attempts} guess:"))
if guess == lottery_number:
    print(f"Guessed Right!")
else:
    print(f"Attempts exceeed.")

for i in range(1,11):
    if i == 5:
        continue
    if i == 8:
        break
    print(f"Number: {i}")