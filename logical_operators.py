#   Logical Operators

# not
print('not:')
print(not 10)           # False
print(not 0)            # True
print(not 'abc')        # False
print(not (''))         # True
print(not True)         # False
print(not None)         # True

# not not
print('\nnot not:')
print(not not 10)       # True
print(not not 0)        # False
print(not not 'abc')    # True
print(not not (''))     # False
print(not not True)     # True
print(not not None)     # False

# and, or (short-circurt operators)
print('\nand:')
print(1 and 2)                  # 2
print(1 and 0)                  # 0
print(0 and 1)                  # 0

print('\nor:')
print(1 or 2)                   # 1
print(1 or 0)                   # 1
print(0 or 1)                   # 1

print('\nand or:')
print((0 and 2) or (2 and 1))   # 1

# Examples:

my_list = [1, 2]
other_list = ['a', 'b']
my_dict = {'A': 1}

print('\nexamples:')
print(len(my_list) < 0 or other_list[0])    # a
print(len(my_list) > 0 or other_list)       # True
print(my_list or my_dict)                   # [1, 2]

print(my_list and my_dict)                  # {}


my_list and print("List is not empty")
my_dict and print('Dictionary is not empty')

print("List is not empty" if my_list else "List is empty")
print("Dictionary is not empty" if my_dict else "Dictionary is empty")

# Task
dict_one = {
    'key_one': 1,
    'key_two': 2,
    'key_three': 'XYZ',
}

dict_two = {
    'key_one': 1,
    'key_two': 2,
    'key_three': 'XYZ',
}

dict_one == dict_two and print('Dictionaries are equal')
