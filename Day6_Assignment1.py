#Q1. Write a python program to reverse a number using a while loop.

# Function to reverse a number
def reverse_number(num):
    # Initialize reversed number to 0
    reversed_num = 0
    
    # Loop until the number becomes 0
    while num > 0:
        # Extract the last digit
        digit = num % 10
        
        # Append the digit to the reversed number
        reversed_num = (reversed_num * 10) + digit
        
        # Remove the last digit from the original number
        num = num // 10
    
    return reversed_num

# Input from the user
num = int(input("Enter a number: "))

# Call the function and print the reversed number
print("Reversed number:", reverse_number(num))


'''
OUTPUT:
Enter a number: 12345
Reversed number: 54321
'''
