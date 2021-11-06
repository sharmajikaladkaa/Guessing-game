import random
def guessing_game(guesslimit,num):
    random_num=random.randint(1,num)
    try:
        while guesslimit>0:
            guess=int(input("what is your guess: "))
            guesslimit-=1
            if random_num == guess:
                print("congrats, its correct")
                break
            elif guess > num:
                print("guess is out of limit")
                print(f'you have {guesslimit} guesses left')
            else:
                print("its wrong")
                print(f'you have {guesslimit} guesses left')
        print("Game over")
        print(f'random number was {random_num}')
    
    except ValueError:
        print("only integers are allowed")

def easy():
    print("guess a number between 1 and 10, ypu have 5 guesses")
    guessing_game(5,10)

def medium():
    print("guess a number between 1 and 10, ypu have 4 guesses")
    guessing_game(4,20)

def hard():
    print("guess a number between 1 and 10, ypu have 3 guesses")
    guessing_game(3,40)

def tryagain():
    again=str(input("do you want to play again? Yes or No: "))
    if again.upper=='YES':
        welcome()
    elif again.upper=='NO':
        print("thanks for playing")
    else:
        print("wrong input")
        tryagain()

def welcome():
    print("welcome to the guessing game")
    difficulty=input("choose the level: Easy, Medium and Hard: ")
    if difficulty.upper()=='EASY':
        easy()
        tryagain()
    elif difficulty.upper()=='MEDIUM':
        medium()
        tryagain()
    elif difficulty.upper()=='Hard':
        hard()
        tryagain()
    else:
        print("wrong input")
        welcome()
    
welcome()