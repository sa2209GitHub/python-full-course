#   Object Behavior

from copy import deepcopy

# Immutable objects behavior
print("Immutable object behavior:")
my_number = 10
other_number = my_number
print(id(10), id(my_number), id(other_number), "<<< all ids are the same")

other_number += 5  # this will create a new object
print(id(10), id(my_number), id(other_number), "<<< new object")

# Mutable object behavior
print("\nMutable object behavior:")
my_list = [1, 2, 3]
other_list = [1, 2, 3]

print(id(my_list), id(other_list), id([1, 2, 3]), "<<< all ids are different")

# Deep copy
print("\nObject deep copy:")

info = {
    'name': 'Alex',
    'country': 'Unknown',
    'contacts': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['contacts'].extend(('alex@mail.com', '+7-919-772-23-99'))

print(info)
print(info_deepcopy)
