#   Dictionaries

# my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

# my_disk['brand'] = 'Samsung'
# my_disk['price'] = 80

# print(my_disk)
# print(id(my_disk))

# print(my_disk.__doc__)
# print(my_disk.items())
# print(my_disk.keys())

# print(list(my_disk.keys()))
# print(list(my_disk.values()))

# print(my_disk.get('type', 'hdd'))

# new_disk = my_disk.copy()
# new_disk['type'] = 'ssd'

# print(my_disk, 'id:', id(my_disk))
# print(new_disk, 'id:', id(new_disk))
# print(len(my_disk), len(new_disk))

# Task:
empty_dict = {}

# first_key = input('Enter the first key: ')
# first_value

for i in range(3):
    numbers = ['First', 'Second', 'Third']

    key = input("Enter the " + numbers[i] + " key: ")
    value = input("Enter the " + numbers[i] + " value: ")

    empty_dict[key] = value

print(empty_dict)
