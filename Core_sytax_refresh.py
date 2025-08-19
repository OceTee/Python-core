"""
Variables, loops, conditionals, functions, imports, and modules in Python.
"""

# Function that returns fibonacci numbers up to n
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    while a < n: # Loop until a is less than n
        if a % 2 == 0: # Check if the number is even
            print(f"{a} is even") 
        else:         
            print(f"{a} is odd")
        fib_sequence.append(a) # Append current Fibonacci number to the list
        a, b = b, a + b # Update a and b to the next Fibonacci numbers
    return fib_sequence

