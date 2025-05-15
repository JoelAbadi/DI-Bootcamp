#Challenge #1

#Get input from the user
input_string = input("Enter words separated by commas: ")

#Split the string into a list
word_list = input_string.split(",")

#Sort the list alphabetically
word_list.sort()

#Join the sorted list back into a string
sorted_string = ",".join(word_list)

#Print the result
print(sorted_string)



#Challenge #2

#Define the function
def longest_word(sentence):
    # Step 2: Split the sentence into words
    words = sentence.split()

    # Step 3: Initialize variables
    longest = ""
    max_length = 0

#Iterate through the words
    for word in words:
        # Step 5: Compare word lengths
        if len(word) > max_length:
            longest = word
            max_length = len(word)

#Return the longest word
    return longest

print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))  
