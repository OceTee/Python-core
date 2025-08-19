def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def divide(a,b):
    return a / b
def multiply(a,b):
    return a * b

print("select operation...")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("E to Exit.")

while True:
    choice = input("Enter choice(1/2/3/4/E): ")

    if choice == 'E':
        break

    if choice in ('1','2','3','4','E'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(add(a,b))
        if choice == '2':
            print(subtract(a,b))
        if choice == '3':
            print(multiply(a,b))
        if choice == '4':
            print(divide(a,b))
    else:
        print("Invalid Input")
