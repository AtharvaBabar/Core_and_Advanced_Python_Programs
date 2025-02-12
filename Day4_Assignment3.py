#Q3. Python Program to Check if a Number is Positive, Negative or zero.

# Function to check if the number is positive, negative, or zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Taking input from the user
num = float(input("Enter a number: "))

# Checking and displaying the result
result = check_number(num)
print(f"The number is {result}.")


'''
OUTPUT:
Enter a number: 8
The number is Positive.

Enter a number: 0
The number is Zero.

Enter a number: -3.5
The number is Negative.
'''
