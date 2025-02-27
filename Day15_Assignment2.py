#Q2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            # Read the entire content of the file
            content = file.read()
            # Split content into words using whitespace
            words = content.split()
            # Count the number of words
            word_count = len(words)
            # Display the word count
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Call the function with the filename
count_words_in_file("ABC.txt")


'''
OUTPUT:
Total number of words in 'ABC.txt': 12

Error: The file 'ABC.txt' does not exist.
'''
