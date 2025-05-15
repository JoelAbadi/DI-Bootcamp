# #create a funtion calles task_manager that accepts and prints " today I need to do: {task} "

# def task_manager(*args):
#     if args:
#         for arg in args:
#             print (f"Today i need to do: {arg}")
#     else:
#         print("Please pass a task as argument")

# task_manager('finish Daily Challenge', 'buy bread', 'to call my mom')


def party_planner(*args, **kwargs):
    if args:
        print('you need to buy')
        for arg in args:
           print(arg) 
    else:
        print('there is no food to buy')

    if kwargs:
        print('party details:')

        for key, values in kwargs.items():
            print(f'{key} : \n {values}')
    else:
        print('theres is not details for this party')

    party_planner('pizza','chips','drinks', address = 'Allenby 20 - TLV', time =  '7PM', ticket_price = '80')



    # Call this function and pass the food and the party details
    # call it with only food inof
    #call it with only  the details
