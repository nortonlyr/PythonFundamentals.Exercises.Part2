def exponentiate(x,y):
    """
    Create a exponential function, add two interger x and y, then set x^y
    """
    return x**y

def raise_to_fourth_power(z):
    """
    Create the other function with power of 4 with argument called z, z^4
    """
    return z**4

square = lambda a:exponentiate(a,2)

cube = lambda b:exponentiate(b,3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
