# import random
# import os
import random
import os


print("Looking for words.txt in:", os.getcwd())


def get_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


def get_random_sentence(length):
    words = get_words_from_file("words.txt")
    if len(words) < length:
        print("Error: Not enough words in the file to generate the sentence.")
        return ""

    sentence = ' '.join(random.choice(words) for _ in range(length)).lower()
    return sentence


def main():
    print("\nWelcome to the Random Sentence Generator!")
    print("This program generates a random sentence using words from a word list.")

    user_input = input("Enter a sentence length between 2 and 20: ")

    try:
        length = int(user_input)
        if length < 2 or length > 20:
            print("Please enter a number between 2 and 20.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    sentence = get_random_sentence(length)
    if sentence:
        print("\nGenerated sentence:")
        print(sentence)


if __name__ == "__main__":
    main()


#  Exercise 2

import json

# Step 1: Load the JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Parse the string into a Python dictionary
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print("Employee salary:", salary)

# Step 3: Add the “birth_date” key
data["company"]["employee"]["birth_date"] = "1995-06-15"

# Step 4: Save the modified JSON to a file
with open("modified_employee.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nModified JSON saved to 'modified_employee.json'")

