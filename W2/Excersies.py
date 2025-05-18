#Exercise 1
# Define the Cat class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Luna", 3)
cat3 = Cat("Shadow", 7)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest

# Step 3: Print the oldest cat's details
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")



#Exercise 2
# Step 1: Create the Dog Class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Print Dog Details and Call Methods
print(f"David's dog is named {davids_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size.")


#Exercise 3

# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Example usage
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Call the method to sing the song
stairway.sing_me_a_song()


#Exercise 4

# Step 1: Define the Zoo Class
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.groups:
                self.groups[first_letter] = [animal]
            else:
                self.groups[first_letter].append(animal)
        return self.groups

    def get_groups(self):
        if hasattr(self, 'groups'):
            for letter, animals in self.groups.items():
                print(f"{letter}: {animals}")
        else:
            print("Please sort the animals first using sort_animals().")

# Step 2: Create a Zoo instance
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Step 3: Use the Zoo methods
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Cat")

ramat_gan_safari.get_animals()

print()