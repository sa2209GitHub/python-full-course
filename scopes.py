#   Scopes

a = 10


def my_fn():

    a = True
    b = 15

    global G
    G = "GLOBAL VARIABLE DECLARED IN FUNCTION BODY"

    print(a, b)


my_fn()

print(a)
print(G)
# print(b)
