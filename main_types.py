#   Main Types

str = 'Hello'                                                   # class 'str'
int = 10                                                        # class 'int'
float = 10.10                                                   # class 'float'
bool = True                                                     # class 'bool'

list = [str, int, float, bool]                                  # class 'list'
dict = {'str': str, 'int': int, 'float': float, 'bool': bool}   # class 'dict'
tuple = (str, int, float, bool)                                 # class 'tuple'
set = {str, int, float, bool}                                   # class 'set'

# class 'NoneType'
none = None


def fn():                                                       # class 'function'
    pass


print('str =', str, type(str))
print('int =', int, type(int))
print('float =', float, type(float))
print('bool =', bool, type(bool))
print('list =', list, type(list))
print('dict =', dict, type(dict))
print('tuple =', tuple, type(tuple))
print('set =', set, type(set))
print('none =', None, type(none))
print('fn =', fn, type(fn))
