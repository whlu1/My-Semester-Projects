#Winni Lu
#11/11/24
#number guesser
import random
def random_number_game():
    print("Welcome to number guesser! Insert a random number and try to guess the number.") #introduces the user to the game
    print("You will only have 3 chances to guess the number.") #introduces the rules
    print("There are three levels to choose from: easy, medium, or hard.") #different levels
    level=input("Which level would you like to play?(please type in all lowercase): ") #user chooses level
    if level=="easy": #easy game
        print("Welcome to the easy level, you will have to correctly guess a number from 0-10")
        secret=random.randint(0,10)
    elif level=="medium": #medium game
        print("Welcome to the medium level, you will have to correctly guess a number from 0-30")
        secret=random.randint(0,30)
    elif level=="hard": #hard game
        print("Welcome to the hard level, you will have to correctly guess a number from 0-50")
        secret=random.randint(0,50)
    guess=int(input("Enter Number: "))
    if guess==secret:
        print("Congratulations you have correctly guessed the number!") #congrats the user for guessing right
    elif guess>secret:
        print("You have lost a life. "+str(guess)+" is too high continue guessing!")
        guess=int(input("Enter Number: "))
        if guess<secret:
            print("You have lost another life. "+str(guess)+" is too low continue guessing!")
        if guess>secret:
            print("You have lost another life. "+str(guess)+" is too high continue guessing!")
        if guess==secret:
            print("Congratulations you have correctly guessed the number! It was "+str(secret))
        else:
            guess=int(input("Enter Number: "))
            if guess==secret:
                print("Congratulations you have correctly guessed the number! It was "+str(secret))
            else:
                print("You have lost all your lives and have incorrectly guessed the number. The number was "+str(secret)) #the user has lost the game
    elif guess<secret:
        print("You have lost a life. "+str(guess)+" is too low continue guessing!")
        guess=int(input("Enter Number: "))
        if guess<secret:
            print("You have lost another life. "+str(guess)+" is too low continue guessing!")
        if guess>secret:
            print("You have lost another life. "+str(guess)+" is too high continue guessing!")
        if guess==secret:
            print("Congratulations you have correctly guessed the number! It was "+str(secret))
        else:
            guess=int(input("Enter Number: "))
            if guess==secret:
                print("Congratulations you have correctly guessed the number! It was "+str(secret))
            else:
                print("You have lost all your lives and have incorrectly guessed the number. The number was "+str(secret))
random_number_game()
