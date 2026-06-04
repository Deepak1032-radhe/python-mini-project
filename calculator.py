a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operator=input("Enter the operator (+, -, *, /): ")
if operator == "+": 

    result = a + b
elif operator == "-":   
    result = a - b  
elif operator == "*":
    result = a * b
elif operator == "/":
    result = a / b
else:
    print("Invalid operator!")
    result = None

if result is not None:
    print(f"The result of {a} {operator} {b} is {result}.")