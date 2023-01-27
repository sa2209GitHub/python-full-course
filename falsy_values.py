#   Falsy Values

falsy_values = (0, 0.0, 0j, False, None, [], {}, (), set(), range(0), '')

print('Falsy values in Python:')

for value in falsy_values:
    print(f"value = {value}, {type(value)}, {bool(value)}")
