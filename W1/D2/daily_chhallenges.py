# Challenge 1: Multiples of a Number

# This program asks the user for a number and a length,
# then generates a list of that many multiples of the number.

# Ask the user for a number to multiply
try:
    number_to_multiply = int(input("Enter a number to multiply: "))
    desired_length = int(input("Enter the number of multiples to generate: "))
except ValueError:
    print("Invalid input. Please enter whole numbers only.")
    exit()

# Create an empty list to store the multiples
multiples_list = []

# Generate the multiples using a loop
for i in range(1, desired_length + 1):
    multiples_list.append(number_to_multiply * i)

# Print the list of multiples
print("List of multiples:", multiples_list)


# Challenge 2: Remove Consecutive Duplicate Letters

# This program removes consecutive duplicate characters from a string,
# so "ppoeemm" becomes "poem".

# Ask the user for a string
input_string = input("Enter a word or sentence: ")

# Check if the input string is not empty
if input_string != "":
    # Initialize the result with the first character
    modified_string = input_string[0]

    # Loop through the remaining characters
    for char in input_string[1:]:
        # Add the character only if it's not the same as the last one added
        if char != modified_string[-1]:
            modified_string += char

    # Print the result
    print("Modified string without consecutive duplicates:", modified_string)
else:
    print("You entered an empty string.")

