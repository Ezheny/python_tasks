from string import digits, ascii_letters
import random

def password_generator(len):
    valid_values = list(digits + ascii_letters)
    random.shuffle(valid_values)
    password = ''.join([random.choice(valid_values) for x in range(len)])
    while 1:
        yield password


# password_generator(25)

