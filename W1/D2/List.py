#A list is a sequence of elements
# names = []
# name_1 =  'john'
# name_2 = 'beth'
# name_3 = 'rip'
# name_4 = 'stacey'


# names.extend([name_1 , name_2 ,name_3 , name_4])

# print (names)

list1 = [5, 10, 15, 20, 25, 50, 20]

x = list1 ('20')
print ('x')

print('x'[4])

j= list1.replace('20', '200')

list1.index(20)

if list1.index(20):
    index_found = list1.index(20)
    list1.insert(index_found, 200)
    list1. remove (20)
    print(list1)
else:
    print ('element not found')