#   Lists


list_from_str = list('list')

print(list_from_str)

my_list = ['foo', 'bar', 'baz', 4, 5, True]

print(my_list)

my_list.append('string')

print(my_list)

my_list.extend([1, 2, 3, 'A', 'B', 'C'])

print(my_list)

for i in range(len(my_list)):
    print('index', i, ':', my_list[i])

my_list.reverse()

print(my_list)
