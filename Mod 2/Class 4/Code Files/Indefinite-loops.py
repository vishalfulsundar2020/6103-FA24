# %%
# Indefinite / Conditional Loops

# Remember the good old friend
def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


# %%
# A user-friendly factorial
def fact1():
    n = eval(input('Enter n: '))

    # Check if an integer indefinitely
    while not isinstance(n, int): # int is a class
        n = eval(input('Please enter an integer: '))
    
    # Factorial computation
    return factorial(n)

# Function call
fact1()

# %%

# A more user-friendly factorial
# Iterate until the input is a positive integer
def fact2():
    n = eval(input('Enter n: '))

    # Check if an integer indefinitely
    while n<-0 and not isinstance(n, int): # int is a class
        n = eval(input('Please enter a positive integer: '))
    
    # Factorial computation
    return factorial(n)

# Function call
fact2(-4)

#Another way to do it - A better way to do it
def fact2():
    # Input validation: Convert input to integer and ensure it's positive
    try:
        n = int(input('Enter n: '))
    except ValueError:
        n = -1  # Assign an invalid value to trigger the while loop

    # Check if input is a positive integer
    while n < 0:
        try:
            n = int(input('Please enter a positive integer: '))
        except ValueError:
            n = -1  # Continue to prompt if input is not a valid integer

    # Factorial computation
    return factorial(n)

# Example call
print(fact2())


# %%
# A more user-friendly and resource-friendly factorial
# Limit the number of attempts
def fact3():
    max_att = 3

    n = eval(input('Enter n: '))
    attempts = 1

    # Check if reached the maximum
    while (attempts < max_att) and (not isinstance(n, int) and n <= 0): # int is a class
        attempts += 1
        if attempts < max_att:
            n = eval(input('Please enter a positive integer: '))
    # Factorial computation
    return factorial(n) if attempts < max_att else -1

# Function call
fact3(4)


# %%
# Sentinel Loop
# averaging positive numbers
def sumOfPositives():
    total = 0.0

    x = float(input('Enter a number (negative to quit) >> '))
    while x >= 0:
        total += x
        x = float(input('Enter a number (negative to quit) >> '))
    return total

print( sumOfPositives() )

# %%