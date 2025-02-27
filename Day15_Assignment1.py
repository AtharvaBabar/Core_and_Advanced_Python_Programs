#Q1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_file_line_by_line(filename):
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            # Read and display each line
            for line in file:
                print(line.strip())  # strip() removes trailing newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Call the function with the filename
read_file_line_by_line("ABC.txt")


'''
OUTPUT:
Hello, World!
Welcome to Python file handling.
This is a sample text file.

Error: The file 'ABC.txt' does not exist.
'''
