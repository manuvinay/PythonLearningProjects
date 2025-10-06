a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")

if b != 0:
    print(f"Division: {a/b}")
else:
    print("Division: Cannot divide by zero.")