# #Exercise 1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s" if self.amount != 1 else f"{self.amount} {self.currency}"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, int):
            return self.amount + other
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Currency' and '{type(other).__name__}'")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError(f"Unsupported operand type(s) for +=: 'Currency' and '{type(other).__name__}'")
        return self
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))       # '5 dollars'
print(int(c1))       # 5
print(repr(c1))      # '5 dollars'
print(c1 + 5)        # 10
print(c1 + c2)       # 15
print(c1)            # 5 dollars

c1 += 5
print(c1)            # 10 dollars

c1 += c2
print(c1)            # 20 dollars

# This should raise a TypeError
try:
    print(c1 + c3)
except TypeError as e:
    print(e)  # Cannot add between Currency type <dollar> and <shekel>


#Exercise 2

#View func file:

from func import add_numbers

add_numbers(10, 15)



#Exercise 3

import string
import random

# Step 2: Create a string with all uppercase and lowercase letters
all_letters = string.ascii_letters  # Includes both lowercase and uppercase

# Step 3: Generate a random string of length 5
random_string = ''

for _ in range(5):
    random_char = random.choice(all_letters)
    random_string += random_char  # Concatenate character to the result

print("Random string:", random_string)


#Exercise 4

import datetime 

def show_current_date():
    current_date = datetime.date.today()  
    print("Today's date is:", current_date)  

show_current_date()



#Exercise 5

import datetime  # Step 1: Import the datetime module

def time_until_new_year():
    # Step 2: Get current date and time
    now = datetime.datetime.now()
    
    # Step 3: Create a datetime object for Jan 1st of the next year
    next_year = now.year + 1
    jan_first = datetime.datetime(year=next_year, month=1, day=1)
    
    # Step 4: Calculate the time difference
    time_left = jan_first - now
    
    # Step 5: Display the time difference
    print("Time left until January 1st:")
    print(time_left)

# Call the function
time_until_new_year()



#Exercise 6
import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")  # You can change format if needed
    now = datetime.datetime.now()
    time_lived = now - birthdate
    minutes = int(time_lived.total_seconds() / 60)
    print(f"You have lived for approximately {minutes:,} minutes.")

# Example usage:
minutes_lived("1990-01-01")


# Exercise 7

#go to CMD nad download "faker"

from faker import Faker 

users = []

def generate_fake_users(n):
    fake = Faker()
    
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)


generate_fake_users(5)

for user in users:
    print(user)
    print("-" * 40)
