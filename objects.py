#   Objects

def get_information_about_an_object(object):
    """
    Get information about an object

    Args:
        object (any): any object

    Returns:
        dict: object information
    """

    description = {}
    object_type = type(object)

    description['type'] = type(object)
    description['properties'] = set(dir(object))

    return description


print(get_information_about_an_object([1, 2, 3]))
print(dir([1, 2, 3]).pop)
print(dir([1, 2, 3]).__mul__)
print(dir([1, 2, 3]).__doc__)
print([1, 2, 3].__ne__)
