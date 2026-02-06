a : int = 3
b : int = 2
print(f"Addition of a and b: {a + b}")
print(f"Subtraction of a and b: {a - b}")
print(f"Multiplication of a and b: {a * b}")
print(f"Division of a and b: {a / b}")
print(f"floor division of a and b {a//b}")
print(f"Ceiling division of a and b {a//b + (a%b > 0)}")
print(f"Modulus of a and b: {a % b}")
print(f"Exponentiation of a and b: {a ** b}")

# logical and comparison operations
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a > 0 and b > 0)
print(a > 0 or b > 0)
print(not (a > 0 and b > 0))

print({a and b})
print({a or b})
print(not a)
print(a and b)
