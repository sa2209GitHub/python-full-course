#   Ranges

my_range = range(7)

for n in my_range:
    print(n)

print(type(my_range))
print(my_range)
print(my_range[0])
print(my_range[1])
print(my_range[2])

print(set(my_range))
print(list(my_range))

other_range = range(0, 98, 4)
print(other_range)
print(set(other_range))

print(set(range(12, 25, 2)))
print(list(range(12, 25, 2)))

new_range = range(2, 13, 2)
print(list(new_range))
print(bool(new_range.count(11)))
print(bool(new_range.count(12)))

# Task:
new_list = []

for i in range(2, 9, 2):
    new_list.append(i)

for i in range(6, 1, -2):
    new_list.append(i)

print(new_list)

floats = []

for i in range(0, 10):
    floats.append(i / 10)

print(floats)
