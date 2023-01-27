#   Callback Functions

def print_number_info(number):
    if (number % 2) == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def print_square_number(number):
    print(f"Square of the {number} is", pow(number, 2))


def process_number(number, callback_fn):
    callback_fn(number)


entered_number = int(input("Enter any number: "))

process_number(entered_number, print_number_info)
process_number(entered_number, print_square_number)
