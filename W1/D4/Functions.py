# # def func_name():
# #     '''prints a phrase on the console''' #doc strings
# # print('i am a function')


# def greetings(language):
#     '''print a hello in spanish on the console'''
#     if language == 'PT':
#         print('Ola')
        
#     elif language == 'ES':
#         print('hola')

# greetings("ES")

# def greeting (language, user_name):
#     '''print hello in other languages'''
#     if language== 'RU':
#         print('Priviet')

#     elif language== 'HE':
#         print('Shalom',user_name)

#     else:
#         print('undefined language')

# #keyword argument
# greeting(language="HE", user_name="Juliana")


#create a function called country_info that recieves a country name as an argument and 
#prints the capital of that country .make the country name argument default
#Nabu

def country_info (country_name='Nabu'):

    if country_name =="Panama":
        print (f'the capital of {country_name} is Panama_City')

    elif country_name == 'Israel':
        print (f'the capital of {country_name} is Jerusalem')

    elif country_name == 'Nabu':
        print (f'the capital of {country_name} is Thead')

    else:
        print(f'country not found')

country_info("USA")
######


def calculation (num1,num2):
    result = num1 +num2
    return result
#print (calculation(5,4))
calculation_result = calculation(5,4)
print(calculation_result)



####

def calculation (a,b):
    addition = a+b
    substraction = a-b
    return addition,substraction