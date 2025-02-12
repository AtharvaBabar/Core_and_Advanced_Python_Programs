#Q2. Python Program to Find the Largest Among Three Numbers.

# Function to find the largest among three numbers
def find_largest(a, b, c):
    # Using max() function to find the largest number
    return max(a, b, c)

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Finding the largest number
largest = find_largest(num1, num2, num3)

# Displaying the result
print(f"The largest number is {largest}")


'''
OUTPUT:
Enter first number: 5
Enter second number: 80
Enter third number: 10000
The largest number is 10000.0
'''
