#   Falsy Values

print(
    bool(0),
    bool(0.00),
    bool(0j),
    False,
    bool(None),
    bool([]),
    bool({}),
    bool(()),
    bool(set()),
    bool(range(0)),
    bool('')
)

print('\nnot:')
print(not 10)           # False
print(not 0)            # True
print(not 'abc')        # False
print(not (''))         # True
print(not True)         # False
print(not None)         # True

print('\nnot not:')
print(not not 10)       # True
print(not not 0)        # False
print(not not 'abc')    # True
print(not not (''))     # False
print(not not True)     # True
print(not not None)     # False
