
number = int(input('Choose a number between 1 and 100')) 

if number == secret_number:
    print('Yes, perfect')

if number % 5 == 0:
    print('Buzz')


elif number % 3 == 0:
    print ('Fizz')

elif number % 3 == 0 and number % 5 == 0:
    print('fizzbuzz')

