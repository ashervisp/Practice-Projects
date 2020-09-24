#control+shift+b is pseudo-command line
#ctrl + ` is terminal/command line


def add(first,second):
    print(first+second)

def sub(first,second):
    print(first-second)

def mult(first,second):
    print(first*second)

def div(first,second):
    print(first/second)

x = int(input('Enter first number:'))
y = int(input('Enter second number:'))
z = input('Enter operation:')

if z == '+':
    add(x,y)
if z == '-':
    sub(x,y)
if z == '*':
    mult(x,y)
if z == '/':
    div(x,y)
