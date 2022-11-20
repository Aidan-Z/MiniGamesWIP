# Guess the random computer generated number


import random
import os
import sys

print('------------------------------')
print("Computer Generated Number:")
print('------------------------------')

def computer_gen(number):
    num = random.randint(1, m+1)
    if number == num:
        print('=======================')
        print("You are correct!")
        print('=======================')
    elif number > m:
        print("Number was out of range")
        print("Try again")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Wrong number")
    final()


def final():
    print()
    x = input("Play again?: yes/no: ")
    m = x.upper()
    if m == 'YES':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else: 
        print()
        sys.exit("Goodbye")
        print()
            

r = input("choose a range: ")
print("The number will be between 1 and", r)
m = int(r)

x = (input("guess my number: "))
number = int(x)
computer_gen(number)


# add some catch features for input functions