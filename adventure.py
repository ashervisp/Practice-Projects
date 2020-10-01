import random
room = 0

def direction(room):
    x = input("Which Direction to Go?")
    x=x.lower()

    if x == 'where':
        print('You are in room' + str(room))
        direction(room)

    if (x == 'l' or x=='left') and room == 0:
        print(room)
        room1()
    elif (x == 'r' or x=='right') and room == 0:
        print(room)
        room2()
    elif (x == 'r' or x=='right') and room == 1:
        print(room)
        room3()
    elif (x == 'l' or x=='left') and room == 2:
        print(room)
        room3()
    else:
        print("This is a trap! You died :(")

def room1():
    print("You enter a dungeon with goblins! You should run!")
    room = 1
    direction(room)

def room2():
    print("You enter the kitchen! The cook is busy, so you should leave")
    room = 2
    direction(room)

def room3():
    print("Hooray, you got to the throne room! You are now king!")
    room = 3


##executed part

print("You are at the gates of the Castle. Type L or R to move!")
direction(room)
