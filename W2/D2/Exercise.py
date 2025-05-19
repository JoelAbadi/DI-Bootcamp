#Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def __init__(self, name, age, eye_color):
        super().__init__(name, age)
        self.eye_color = eye_color

    def purr(self):
        return f"{self.name} is purring with its {self.eye_color} eyes."

# Create cat objects
bengal_cat = Bengal("Leo", 3)
chartreux_cat = Chartreux("Misty", 5)
siamese_cat = Siamese("Nina", 2, "blue")

# List of all cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create Pets instance and walk the cats
sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} wins the fight against {self.name}!"
        else:
            return f"{self.name} and {other_dog.name} are equally matched!"

# Create dogs
dog1 = Dog("Bolt", 5, 20)
dog2 = Dog("Rocky", 4, 25)
dog3 = Dog("Bella", 3, 15)

# Test methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog3.fight(dog1))


#Exercise 3

import random

# Assuming Dog class is already defined and imported
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        all_dogs = ', '.join(args)
        print(f"{self.name}, {all_dogs} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")

# Example usage (test code):
dog1 = PetDog("Fido", 2, 10)
dog2 = PetDog("Buddy", 3, 15)
dog3 = PetDog("Max", 4, 20)

dog1.train()                     # Fido is barking
dog1.play("Buddy", "Max")       # Fido, Buddy, Max all play together
dog1.do_a_trick()               # Fido does a random trick
dog2.do_a_trick()               # Nothing happens because not trained


#Exercise 4

# Step 1: Define the Person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


# Step 2: Define the Family class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("This person is not in the family.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"- {member.first_name}, {member.age} years old")

