#   Tuples

internal_ids = (151, 245)
external_ids = (624, 451, 941)

all_ids = internal_ids + external_ids

print(all_ids)
print(all_ids.count(151), all_ids.count(9))
print(all_ids.index(624))

all_ids_list = list(all_ids)

all_ids_list.append(777)

all_ids = tuple(all_ids_list)

print(all_ids)

tuple_from_str = tuple('tuple')

print(tuple_from_str)
