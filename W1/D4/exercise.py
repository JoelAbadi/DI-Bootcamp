
#Exercise 1


def display_message():
    print ("I am learning about funtions in Python")


display_message()


#Exercise 2

def favorite_book(title):
    print(f"One of my favorites books is {title}")

favorite_book('Lord of the Rings')


#Exercise 3
def describe_city(city ,country= "Unknown"):
    print(f'{city} is in {country}.')


describe_city("Reykjavik", "Iceland")


def describe_city(city ,country= "Unknown"):
    print(f'{city} is in {country}.')


describe_city("Paris")


#Exercise 4
import random 

def guess_number (user_number):
    random_number= random.randint(1,100)
    if user_number == random_number:
        print('Success!')
    else:
        print(f'Fail!, your number: {user_number}, Random number: {random_number}')

guess_number(52)


#Exercise 5

def make_shirt (size = "Large", text= 'I love Python'):
    print(f"The size of the shirt is {size} and the text says '{text}'.")

make_shirt()

make_shirt("Medium")

make_shirt("Small", "I love coding")

make_shirt(size= 'small', text="Hello!")

#Exercise 6

magician_names = ['Harry Houdini','David Blaine','Criss Angel']

def show_magicians(names):
    for names in names:
        print(names)

def make_great(names):
    for i in range(len(names)):
        names[i] =names[i]+ " The Great"

make_great(magician_names)
show_magicians(magician_names)

#Exercise 7

import random

def get_renaodm_temp():
    return random.randint(-10,40)

def main():
    temp = get_renaodm_temp()
    print(f' The temperature right now is {temp} degrees Celsius.')

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 24:
        print("Nice weather.")
    elif temp < 33:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")

def get_random_temp():
    return round(random.uniform(-10, 40), 1)

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(10, 22), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(10, 25), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def main():
    month = int(input("Enter the month as a number (1–12): "))
    
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    elif month in [9, 10, 11]:
        season = "autumn"
    else:
        season = "unknown"
    
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp < 24:
        print("Nice weather.")
    elif temp < 33:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
