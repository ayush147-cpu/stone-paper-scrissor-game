# this module is used to print an random input by computer itself so user can't see that input to win the game easily.
import random
# in this phase we are simply giving values to stone paper and scissor as we give in our module 0,1 and 2 respectively.
comp = print("comp turn: stone(st) paper(p) scrissor(s): ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'st'
elif randNo == 2:
    comp = 'p'
elif randNo == '3':
    comp = 's'


# in this we create a function to check computer's turn and user's turn to find out who is the winner winner chicken dinner.
def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'st':
            return True
    elif comp == 'st':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'st':
            return False
        elif you == 's':
            return True


you = input("user's turn: stone(1) paper(2) scrissor(3): ")
a = gamewin(comp, you)
if a == None:
    print("the game is tie!!!")
elif a:
    print("you win!!!")
else:
    print("you lose!!")
