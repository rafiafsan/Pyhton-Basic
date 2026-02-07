def greetings(name):
    return f"Hello {name}, welcome!"

print(greetings("John"))

def triangle_area(base, height):
    return (base * height) / 2

def square_area(side):
    return side ** 2

# Height = int(input(f"Enter height of a triangle: "))
# Base = int(input(f"Enter Base of a triangle: "))

# print(triangle_area(Height, Base))

s_area = square_area(10)
print(f"Squae are is : {s_area}")
print(square_area(4))

#args and kwargs(keyword arguments and positional arguments)

def variable_arguments(*args, **kwargs):
    print(f"Positional : {args}")
    print(f"Keywords: {kwargs}")
    
variable_arguments(1,2,3, Name="Rafi", age=20)


value1 = 0
def increment(value):
    value+=1
    global value1
    value1+=1
    print(f"value: {value} and value1 is : {value1}")

increment(10)