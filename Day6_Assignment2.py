#Q2. Write a python program to check whether a number is palindrome or not?

# Function to check if a number is a palindrome
def is_palindrome(num):
    # Store the original number
    original_num = num
    
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
    
    # Check if the original number is equal to the reversed number
    return original_num == reversed_num

# Input from the user
num = int(input("Enter a number: "))

# Check and print whether the number is a palindrome or not
if is_palindrome(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")


'''
OUTPUT:
Enter a number: 12345
The number is not a palindrome.

Enter a number: 767
The number is a palindrome.
'''
