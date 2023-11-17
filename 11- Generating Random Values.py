import random
import string

print(random.random())  # returns a floating point number
print(random.randint(1, 10))  # random integer. both numbers included.
print(random.choice([1, 2, 3, 4]))  # randomly picks one of the items in the list
print(random.choices([1, 2, 3, 4], k=2))  # randomly picks specified amount of the items

# we can, for example, generate a random password using the "choices" method:
print("".join(random.choices("abcdefghi", k=4)))

# there is a better way. First => import string
# SIDE NOTE: string module has a bunch of useful methods. For example:
print(string.ascii_letters)  # returns a string of all lowercase and uppercase letters
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)  # returns a string of digits (0...9)

print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# we have another useful method for shuffling an array:
numbers = [1, 2, 3, 4]
random.shuffle(numbers)  # the order of the items are randomly changed
print(numbers)
