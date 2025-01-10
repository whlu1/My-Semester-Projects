#Winni Lu
#10/15/24
#name generator
#init
print("Welcome to Your Pet's Name 1.0") #introduces the user to the game
print("Answer the questions to find out your pet's name") #rules of the game
#main
#cascade of different options
color=input("blue or red: ")
if color=="blue":
    fruit=input("mango or watermelon: ")
    if fruit=="mango":
        food=input("sushi or ramen: ")
        if food=="sushi":
            print("Your pet's name is Daisy!")
        else:
            print("Your pet's name is Lily!")
    if fruit=="watermelon":
        food=input("burger or hot dog: ")
        if food=="burger":
            print("Your pet's name is Oreo!")
        else:
            print("Your pet's name is Cookie!")
else:
    fruit=input("apple or banana: ")
    if fruit=="apple":
        food=input("tacos or quesadilla: ")
        if food=="tacos":
            print("Your pet's name is Penny!")
        else:
            print("Your pet's name is Nickel!")
    if fruit=="banana":
        food=input("pizza or pasta: ")
        if food=="pizza":
            print("Your pet's name is Biscuit!")
        else:
            print("Your pet's name is Buddy!")
