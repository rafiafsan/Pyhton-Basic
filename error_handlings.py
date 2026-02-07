
try:
    result = 1/2
    print(f"{result}")
except ZeroDivisionError:
    print(f"You can not divide by zero.")
except Exception as e:
    print(f"Error is : {e}")
finally:
    print(f"This always run.")