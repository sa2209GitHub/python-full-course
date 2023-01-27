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
