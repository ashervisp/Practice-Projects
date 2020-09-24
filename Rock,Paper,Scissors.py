#control+shift+b is pseudo-command line
#ctrl + ` is terminal/command line
from random import seed
from random import randint

x=input("Rock,Paper,Scissors!:")
x = x.lower()
value = randint(0,2)

if value == 0:
    hand = "rock"
if value == 1:
    hand = "paper"
if value == 2:
    hand = "scissors"

if x == hand:
    print("Computer played " + hand)
    print("Draw!")
if (x=='rock' and hand=='paper'):
    print("Computer played " + hand)
    print("Lost!")
if (x=='rock' and hand=='scissors'):
    print("Computer played " + hand)
    print("Won!")
if (x=='paper' and hand=='scissors'):
    print("Computer played " + hand)
    print("Lost!")
if (x=='paper' and hand=='rock'):
    print("Computer played " + hand)
    print("Won!")
if (x=='scissors' and hand=='rock'):
    print("Computer played " + hand)
    print("Lost!")
if (x=='scissors' and hand=='paper'):
    print("Computer played " + hand)
    print("Won!")
