#   Docstring

def print_number_info(num):
    """
    Returnt num information

    Args:
        num (int): Integer number

    Returns:
        str: "num is even" if num is even otherwise "num is odd"
    """
    return f"{num} is even" if num % 2 == 0 else f"{num} is odd"


print(print_number_info(5))
print(print_number_info(30))
