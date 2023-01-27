#   Zip

# fruits = ['apple', 'banana', 'lime', 'orange']
# quantities = [100, 70, 50, 80]
# availability = [True, False, False, True]

# fruit_qtys_zip = zip(fruits, quantities, availability)

# print(fruit_qtys_zip)
# print(list(fruit_qtys_zip))

fruits = ['apple', 'banana', 'lime', 'orange']
quantities = [100, 70, 50, 80]

fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)
print(dict(fruit_qtys_zip))

# Task
goods = ['A', 'B', 'C', 'D', 'E']
prices = [10, 12, 19, 22, 13]

goods_prices_zip = zip(goods, prices)
goods_prices_list = list(goods_prices_zip)
goods_prices_dict = dict(goods_prices_list)

print(goods_prices_list)
print(goods_prices_dict)

# Improved Task
print("\nImproved task with function:")


def zip_two_seqences(first, second, DICT=True):
    first_clone = first.copy()
    second_clone = second.copy()

    return dict(zip(first_clone, second_clone)) if DICT else list(zip(first_clone, second_clone))


print(zip_two_seqences(first=['E', 'F', 'G'], second=[120, 232, 328]))
print(zip_two_seqences(first=['E', 'F', 'G'], second=[12, 23, 32], DICT=False))
