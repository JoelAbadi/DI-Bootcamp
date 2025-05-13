# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# physics_class = sample_dict['class']['student']['marks']['physics']

# print(physics_class)


# shirts = [
#      {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'S',
#     'price': 20
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'M',
#     'price': 25
#   },
#   {
#     'name': 'Awesome T-shirt 3000',
#     'size': 'L',
#     'price': 30
#   }
# ]

# for shirts in shirts:
#     if shirts ['size'] == "M":
#         print(shirts['price'])


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["age", "salary"]

for key in keys_to_remove:
    sample_dict.pop(key)

print(sample_dict)