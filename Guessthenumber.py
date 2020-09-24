from random import randint

value = randint(0,20)
print(value)
x=int(input("Guess the Number!:"))

if x==value:
    print('Congratulations You got it!')
elif x>value:
    print('Sorry, that is too high!')
else:
    print('Sorry, that is too low!')
