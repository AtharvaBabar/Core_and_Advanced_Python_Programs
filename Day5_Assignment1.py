#Q1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

# Function to divide two numbers
def div(a, b):
    # Check if denominator is not zero to avoid division error
    if b == 0:
        return "Division by zero is not allowed"
    return a / b  # Perform division and return result

# Calling the function with two numbers
result = div(10, 2)

# Displaying the result
print("Division result:", result)


'''
OUTPUT:
Division result: 5.0
'''
