# #if else statements are used to make decisions in our code based on certain conditioans.

# age = int(input(f"Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")
    
    
    
# #we can also use elif to check for multiple conditions.

# marks = int(input(f"Enter your marks: "))
# if marks >= 90:
#     grade = 'A'
#     message =  'Excellent'
#     print(f"You got an {grade} grade with a message: {message}")
# elif marks >= 80:
#     grade = 'B'
#     message = 'Good'
# elif marks >= 70:
#     garde = 'C'
#     message = 'Average'
# elif marks >= 60:
#     grade = 'D'
#     message = 'Below Average'
# else:
#     grade = 'F'
#     message = 'Fail'

# print(f"You got an {grade} grade with a message: {message}")



    
# #we can also use nested if statements to check for multiple conditions.

# number = int(input(f"Enter a nmber:"))
# if number > 0 :
#     print(f"{number} is a positive number.")
#     if number % 2 == 0:
#         print(f"numbe is even.")
#     else:
#         print(f"number is odd.")
# else:
#     print(f"number is zero or negative.")
        
        
age : int = 25
has_lisence : bool =True
has_inssurance : bool = False

if age >=18 and has_lisence :
    print("You have both the age and lisence to drive.")
else:
    print("You do not have both the age and lisence to drive.")

if age >= 18 and has_inssurance:
    print("You have both the age and insurance to drive.")
else:
    print("You do not have both the age and insurance to drive.")
    



# if age >= 18 or has_inssurance:
#     print("You have either the age or lisence to drive.")