#CALCULATOR
def calculator(a:int , b:int, operation =str) -> int:
    if operation == "addition":
        result = a+b
        print(f"{operation} is : {result}")
    elif operation == "subtraction":
        result = a-b
        print(f"{operation} is : {result}")
    elif operation == "multiply":
        result = a*b
        print(f"{operation} is : {result}")
    elif operation == "divide":
        try:
           result = a/b
           print(f"{operation} is : {result}")
        except ZeroDivisionError:
            print(f"You can not divide something by zero.")
    else:
        print(f"Invalid Operation.")
    return result
        
divide = calculator(10,10,"divide")
add = calculator(10,10,"addition")
print(f"Addition is : {add}")
print(f"Divide is : {divide}")

num1 = int(input(f"Enter your first number:"))
num2 = int(input(f"Enter your second number:"))
operation = input(f"Enter operation: ").lower()

calc = calculator(num1,num2,operation)

