#Q3.  Write a python program finding the factorial of a given number using a while loop.

# Function to find the factorial of a number using a while loop
def factorial(num):
    # Initialize factorial to 1
    fact = 1
    
    # Loop while num is greater than 0
    while num > 0:
        fact *= num  # Multiply fact by num
        num -= 1  # Decrement num
    
    return fact

# Input from the user
num = int(input("Enter a number: "))

# Call the function and print the factorial
print("Factorial:", factorial(num))


'''
OUTPUT:
Enter a number: 7
Factorial: 5040
'''
