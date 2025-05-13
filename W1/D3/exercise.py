#Exercise 1

#The goal is to take this two list and turn them into a dictorinary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

results=dict(zip(keys,values))
print(results)

#zip(keys, values) combines the two lists into pairs:
('Ten', 10), ('Twenty', 20), ('Thirty', 30)

#dict() turns those pairs into a dictionary.


#Exercise 2

# The goal is to Loop through this dictionary and calculate ticket prices based on age:

# Ticket Pricing Rules:
# Age under 3 = Free
# Age 3 to 12 = $10
# Age over 12 = $15

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0

for member, age in family.items():
    if age < 3:
        print(f"{member.title()} is {age} years old: Ticket is free.")
        price = 0
    elif 3 <= age <= 12:
        print(f"{member.title()} is {age} years old: Ticket costs $10.")
        price = 10
    else:
        print(f"{member.title()} is {age} years old: Ticket costs $15.")
        price = 15

    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")

#I use for loop to go through each person and their age. then used if, elif, else to decide the prices:babies are free,kids pay $10 and adults pay $15

# Rick is 43 years old: Ticket costs $15
# Beth is 13 years old: Ticket costs $15
# Morty is 5 years old: Ticket costs $10
# Summer is 8 years old: Ticket costs $10
# Total cost for the family: $50

#Bonus
family = {}
while True:
    name = input("Enter family member's name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age

total_cost = 0

for member, age in family.items():
    if age < 3:
        print(f"{member.title()} is {age} years old: Ticket is free.")
        price = 0
    elif 3 <= age <= 12:
        print(f"{member.title()} is {age} years old: Ticket costs $10.")
        price = 10
    else:
        print(f"{member.title()} is {age} years old: Ticket costs $15.")
        price = 15

    total_cost += price

print(f"\nTotal cost for the family: ${total_cost}")


#Exercise 3

# The goal is to create a dictionary with Zara brand data and practice modifying, accessing, and managing its contents using dictionary methods.

# the dictionary:

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Then we will change number_stores to 2

brand["number_stores"] = 2

#We can also review is clients with type_of_clothes

print("Zara's clients are:", ", ".join(brand["type_of_clothes"]))

#.join() combines the list into a easier to read sentence.

#I added a new key and value,with a key of country_creation and value "Spain"

brand["country_creation"] = "Spain"

#I add the international_competitors and also “Desigual”

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#I deleted the creation_date key

brand.pop("creation_date")

#I print the last item in international_competitors

print("Last international competitor:", brand["international_competitors"][-1])

#Also the colors of the US

print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))

#Now we check the number of keys in the dictionary

print("Number of keys in the dictionary:", len(brand))

#Print all the brands keys

print("All keys:", list(brand.keys()))

#Bonus

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)
print("\nUpdated brand dictionary:")
print(brand)


#Exercise 4

#The goal is to create 3 different dictionaries from a list using indexing, sorting, and dictionary creation techniques.

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#Merging the charchter to their indices

char_to_index = {user: index for index, user in enumerate(users)}
print("Characters to indices:", char_to_index)

#I used enumerate to get both the index and the character

index_to_char = {index: user for index, user in enumerate(users)}
print("Indices to characters:", index_to_char)

#I sorted the characters

sorted_users = sorted(users)
sorted_char_to_index = {user: index for index, user in enumerate(sorted_users)}
print("Alphabetical characters to indices:", sorted_char_to_index)

Characters_to_indices: {'Mickey': 0, 'Minnie': 1, 'Donald': 2, 'Ariel': 3, 'Pluto': 4}
Indices_to_characters: {0: 'Mickey', 1: 'Minnie', 2: 'Donald', 3: 'Ariel', 4: 'Pluto'}
Alphabetical_characters_to_indices: {'Ariel': 0, 'Donald': 1, 'Mickey': 2, 'Minnie': 3, 'Pluto': 4}