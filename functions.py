#   Functions

from copy import deepcopy
from datetime import date


def sum_fn(a, b):
    return a + b


print(type(sum_fn))
print(sum_fn(2, 2))
print(sum_fn(4, 4))


def increase_person_age(person):
    print(id(person_one))
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21
}

print(id(person_one))

print(person_one['age'])
increase_person_age(person_one)
print(person_one['age'])


# Task:


def merge_lists_to_dict(first_list, second_list):
    return dict(zip(first_list, second_list))


print(merge_lists_to_dict(first_list=[
      'A', 'B', 'C'], second_list=[False, False, True]))
print(merge_lists_to_dict(first_list=[
      'Mikle', 'John', 'Noah'], second_list=[23, 43, 34]))
print(merge_lists_to_dict(['X', 'Y', 'Z'], second_list=[True, True, True]))


# Сoncatenation of arguments into a tuple


def sum_nums(*args):
    print(args)
    print(type(args))

    return sum(args)


print(sum_nums(2, 3, 7))


# Positional arguments


def get_posts_info(name, posts_qty):
    return f"{name} wrote {posts_qty} posts"


print(get_posts_info('John', 22))
print(get_posts_info(22, 'John'), "<<< there is a problem here")


# Keyword arguments


print(get_posts_info(name='Noah', posts_qty=335))
print(get_posts_info(posts_qty=335, name='Noah'))


# Сoncatenation of arguments into a dictionary

def get_posts_info_dict(**person):
    print(person)
    print(type(person))
    info = (
        f"{person.get('name')} wrote "
        f"{person.get('posts_qty')} posts"
    )
    return info


print(get_posts_info_dict(name='Mikle', posts_qty=453))


# Task


def update_car_info(**car):
    print(car)
    clone = deepcopy(car)
    clone['is_available'] = True
    return clone


print(update_car_info(brand='Audi', price='33900'))


# Default parameters


def mult_by_factor(value, multiplier=1):
    return value * multiplier


print(mult_by_factor(10, 2))
print(mult_by_factor(5))


def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = deepcopy(post)
    post_copy['created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 432,
    'author': 'John'
}

print(create_new_post(post=initial_post, weekday='Monday'))
print(create_new_post(post=initial_post))
print(initial_post)
