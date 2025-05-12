#Exercise 1

# my_fav_numbers = [1,5,9,18]
# print(my_fav_numbers)

# my_fav_numbers.append('23')

# print(my_fav_numbers)

# my_fav_numbers .append ('27')

# print(my_fav_numbers)

# my_fav_numbers.remove('27')

# print(my_fav_numbers)

# friend_fav_numbers= [1,4,8,9,12,15]

# print(friend_fav_numbers)

# my_fav_numbers + friend_fav_numbers

# print (my_fav_numbers + friend_fav_numbers)

# my_fav_numbers.pop (0)

# print(my_fav_numbers + friend_fav_numbers)

# our_fav_numbers= my_fav_numbers + friend_fav_numbers 

# print(our_fav_numbers)

#Excerise 2

# my_tuple=(5,10,20,40,80)

# a,b,c,d,e = my_tuple

# print (a)
# print (b)
# print (c)
# print (d)
# print (e)

# f= 160
# g= 320

# new_tuple = (a,b,c,d,e,f,g)

# print(new_tuple)


#Excersie 3

# basket = ['banana', 'apples', 'oranges','blueberries']

# print(basket)

# basket.pop (0)

# print(basket)

# basket.pop (-1)

# print(basket)

# basket.append('Kiwi')

# print(basket)

# basket.insert(0,'apples')

# print(basket)

# apple_count = basket.count('apples')

# print(apple_count)

# basket.clear()

# print(basket)


#Excersie 4

# list = [1.5,2,2.5,3,3.5,4,4.5,5]
# [1,2,3,4,5]
# list1 = []
# print(list)

# for number in range(5):
#     list1.append(number)

# print(list1)

# list2 =[]

# number = 1.5
# while number<= 5:
#     list2.append(number)
#     number +=0.5
# print(list2)

# new_list =(list2+list1)

# print (new_list)

# new_list = sorted

# print(new_list)

# #Excersie 5

# for number in range(1,21):
#     print(number)

# [1,2,3,4,5]

# numbers= list(range (1,21))

# for index in range(len(numbers)):
#     if index % 2 ==0:
#         print(numbers[index])

#Exercise 6

# while True:
#     name= input("Enter your name:")
#     if name == "Joel":
#         break
#     else:
#         print("keep trying")


#Exercise 7
# favorite_fruit = input("Enter your favorite fruit (separaeted by a comma):")
# list_fruits = favorite_fruit.split(',')
# print(list_fruits)
# new_fruit = input('enter a new fruit')
# if new_fruit in list_fruits:
#     print('you chose one of your favorite fruits! Enjoy!')
# else: 
#     print('you chose a new fruit. I hope you enjoy it!')


#Exercise 8
# toppings = []

# while True:
#     topping = input('enter a pizza topping(or type "quit" to finish):' )
#     if topping.lower() == 'quit':
#         break
#     toppings.append(topping)
#     print(f'adding{toppings} to your pizza.')

#     total_price = base_price + price_per_topping * len(toppings)
#     print('\nYour pizza has these toppings:')
#     for t in toppings:
#         print(f'-{t}')

#         print(f'total cost: ${total_price:.2f}')



# Excercise 9

# total_cost = 0

# while True:
#     age_input =input ('enter the person age(or type 'done' to finish)')
#     if age_input.lower()=='done':
#         break

# age= int(age_input)

# if age <3:
#     cost = 0
# elif 3 <= age <= 12:
#     cost = 10
# else:
#     cost=15

# total_cost += cost

# print(f'total ticket cost:${total_cost}')



#Excersie 10

# sandwich_orders = ['Tuna', 'Pastrami','avocado','Pastrami','egg','chicken','Pastrami']
# finished_sandwiches =[]

# print('sorry we are out of Pastrami today')
# while 'Pastrami' in sandwich_orders:sandwich_orders. remove('pastarmi')

# while sandwich_orders:
#     current_sandwich=
#     sandwich_orders.pop(0)
#     print (f'I made your {current_sandwich}')

# finished_sandwiches.append(current_sandwich)

# print('\nAll sandwiches made:')
# for sandwich in finished_sandwiches:
#     print(f'-{sandwich}')







