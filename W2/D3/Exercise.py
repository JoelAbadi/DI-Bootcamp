#Exercise 1

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if not isinstance(other, (Currency, int)):
            raise TypeError(f"Unsupported type for addition: {type(other)}")

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        
        return Currency(self.currency, self.amount + other)

    def __iadd__(self, other):
        if not isinstance(other, (Currency, int)):
            raise TypeError(f"Unsupported type for addition: {type(other)}")

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
         self.amount += other
        return self
    

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))     # Expected: "5 dollars"
print(int(c1))     # Expected: 5
print(repr(c1))    # Expected: "5 dollars"

print(c1 + 5)      # Expected: "10 dollars" as a new Currency object
print(c1 + c2)     # Expected: "15 dollars" as a new Currency object

print(c1)          # Still 5 dollars (unchanged)
c1 += 5
print(c1)          # Now 10 dollars
c1 += c2
print(c1)          # Now 20 dollars

# Now trigger the TypeError
try:
    print(c1 + c3)  # Should raise TypeError
except TypeError as e:
    print(e)        # Expected error message

# Exercise 2

# View func file:

try:
    from func import add_numbers
    add_numbers(3, 4)
except ImportError as e:
    print("Import failed:", e)


#Exercise 3

import string
import random

def generate_random_string():
    return ''.join(random.choices(string.ascii_letters, k=5))

print("Random string:", generate_random_string())

#Exercise 4

from datetime import date

def show_current_date():
    print("Today's date is:", date.today())

show_current_date()

#Exercise 5

from datetime import datetime

def time_until_jan_first():
    now = datetime.now()
    jan_first = datetime(year=now.year + 1, month=1, day=1)
    print("Time left until January 1st:", jan_first - now)

time_until_jan_first()


#Exercise 6
from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.now()
    minutes = int((now - birthdate).total_seconds() / 60)
    print(f"You have lived approximately {minutes} minutes.")

minutes_lived("1995-01-01")  

#Exercise 7
from faker import Faker
def generate_fake_users(n):
    fake = Faker()
    users = []
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)
    return users

for user in generate_fake_users(5):
    print(user)

