from random import randint
import string
import random

x = int(input('How long is the password?'))

if x<6:
    print('I\'m sorry, that is too short! Try again')
else:
    y = ''
    for i in range(0,x):
        decider = randint(0,2)
        if decider == 0:
            value = randint(0,9)
            value = str(value)
            y = y + value
        elif decider == 1:
            lower_upper_alphabet = string.ascii_letters
            random_letter = random.choice(lower_upper_alphabet)
            y = y + random_letter
        else:
            characters = '!@#$%^&*'
            random_character = random.choice(characters)
            y = y + random_character
    print(y)
