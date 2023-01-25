#   Sets

photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1280x1024'}

photo_sizes.add('1024x768')

print(photo_sizes)

union_sizes = photo_sizes.union(other_sizes)

print(union_sizes)

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.union(other_set))
print(my_set.difference(other_set))

copied_set = my_set.copy()
my_set.add('T')
copied_set.add('M')

print(my_set)
print(copied_set)
print(my_set.symmetric_difference(copied_set))


nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

print(nums.issubset(other_nums))
print(other_nums.issuperset(nums))

a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}

print(a | b)                # = a.union(b)
print(a & b)                # = a.intersection(b)

# = a.union(b) - a.intersection(b) = a.symmetric_difference(b)
print((a | b) - (a & b))

# Task
ints = {1, 2, 3, 4, 5, 6}
other_ints = {7, 8, 9}

other_ints.update([5, 6])

print(other_ints)

new_ints = ints & other_ints

print(list(new_ints))
