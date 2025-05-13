#Challenge 1

#The goal is to create a dictionary where each letter from a user-input word is a key, and the value is a list of positions (indices) where that letter appears.

word = input("Enter a word: ")
letter_index_dict = {}

for index, letter in enumerate(word):
    if letter in letter_index_dict:
        letter_index_dict[letter].append(index)
    else:
        letter_index_dict[letter] = [index]

print(letter_index_dict)

#Explenations
# input() ask the user for a word.
# enumerate(word) gives both index and letter in the loop.
# if theres a letter in letter_index_dict: checks if the letter is already a key.
# .append(index) adds the new index to the existing list.
# else: letter_index_dict[letter] = [index] creates a new key with a list.

#Results

dodo: {"d": [0, 2], "o": [1, 3]}
froggy: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}
grapes: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}

#Challenge 2

items_purchase = {
    "Water": "$1", 
    "Bread": "$3", 
    "TV": "$1,000", 
    "Fertilizer": "$20"
}
wallet = "$300"

# Convert wallet to int
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# Make result list
affordable_items = []

# Loop through items and clean prices
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_price <= wallet_amount:
        affordable_items.append(item)

# Sort or return "Nothing"
if not affordable_items:
    print("Nothing")
else:
    print(sorted(affordable_items))

#Explenations
# wallet.replace(...) cleans the string to get the number
# int(...) converts string price to number for comparison
# if clean_price <= wallet_amount:check if the user can afford it
# sorted(affordable_items) returns the list in alphabetical order

#Test 1

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

Output: ["Bread", "Fertilizer", "Water"]


#Test 2

items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"

Output: ["Apple", "Bananas", "Fan", "Honey", "Spoon"]


#Test 3

items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"

Output: "Nothing"