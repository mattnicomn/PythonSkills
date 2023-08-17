# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-argments
#             * unpacking operator
#              1. positional 2. default 3. keyword 4. ARBITRARY

# args example with adding numbers
def add(*args):
    total = 0
    for arg in args:
        total += arg
        return total
print (add(1, 2, 4))
# args example with adding letters
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Leroy", "Harold", "Jenkins")

# Kwargs(keyword argments) example key word and values
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              city="Warner Robins",
              state="GA",
              zip="31088")

# args combined kwargs example (You can not swap the args and kwargs. They have to match the keys or values given in function variables)

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")

shipping_label("Dr.", "Leroy", "Jenkins", "VI",
               street="123 Fake St.",
               apr="100",
               city="Warner Robins",
               state="GA",
               zip="31088")

#Another way to write this same example

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Leroy", "Jenkins", "VI",
               street="123 Fake St.",
               apt="100",
               city="Warner Robins",
               state="GA",
               zip="31088")

# If a key like apt is missing, the output will be None. We do not want that, so we have to add a if statement.

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    #elif "pobox" in kwargs:
        #print(f"{kwargs.get('pobox')})
    else:
        print(f"{kwargs.get('street')}
              
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Leroy", "Jenkins", "VI",
               street="123 Fake St.",
               #pobox="pobox #1001",
               city="Warner Robins",
               state="GA",
               zip="31088")