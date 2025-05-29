#init
import time
import random
foods=[] #empty list for the user to add their own food items
foods_premade=["sushi", "pizza", "pasta", "hamburger", "fried chicken", "fried rice", "steak", "tacos"] #premade list for users if they don't want to add their own items
#functions
def make_table(): #function makes the final choices for the table using the list "foods"
    global final1 #make the variables global so they can be used in other functions as well
    global final2
    global final3
    global final4
    global final5
    global final6
    global final7
    global final8
    print("creating your chart...")
    time.sleep(2) #makes the user wait to build suspense
    final1=random.choice(foods) #randomizes the final choices for the table from the list "foods" with the possibility of repeats
    final2=random.choice(foods)
    final3=random.choice(foods)
    final4=random.choice(foods)
    final5=random.choice(foods)
    final6=random.choice(foods)
    final7=random.choice(foods)
    final8=random.choice(foods)
def make_tablefp(): #function makes the final choices for the table using the list "foods_premade"
    global final_p1 #make the variables global so they can be used in other functions as well
    global final_p2
    global final_p3
    global final_p4
    global final_p5
    global final_p6
    global final_p7
    global final_p8
    print("creating your chart...")
    time.sleep(2) #makes the user wait to build suspense
    final_p1=random.choice(foods_premade) #randomizes the final choices for the table from the list "foods_premade" with the possibility of repeats
    final_p2=random.choice(foods_premade)
    final_p3=random.choice(foods_premade)
    final_p4=random.choice(foods_premade)
    final_p5=random.choice(foods_premade)
    final_p6=random.choice(foods_premade)
    final_p7=random.choice(foods_premade)
    final_p8=random.choice(foods_premade)
def choose_food(): #function asks the user questions to determine the final choice of food using the list "foods"
    color=input("blue or red: ")
    if color=="blue": #depending on what the user chooses, the question after will vary
        time=input("day or night: ")
        if time=="day":
            subject=input("math or english: ")
            if subject=="math":
                print(final1+" has won!") #depending on the user's final choice, a randomized food in the position of final1 will be chosen
            if subject=="english":
                print(final2+" has won!")
        if time=="night":
            subject=input("science or social studies: ")
            if subject=="science":
                print(final3+" has won!")
            if subject=="social studies: ":
                print(final4+" has won!")
    if color=="red":
        place=input("inside or outside: ")
        if place=="inside":
            subject=input("art or music: ")
            if subject=="art":
                print(final5+" has won!")
            if subject=="music":
                print(final6+" has won!")
        if place=="outside":
            event=input("academics or sports: ")
            if event=="academics":
                print(final7+" has won!")
            if event=="sports":
                print(final8+" has won!")
def choose_foodfp(): #function asks the user questions to determine the final choice of food using the list "foods_premade"
    color=input("blue or red: ")
    if color=="blue":
        time=input("day or night: ")
        if time=="day":
            subject=input("math or english: ")
            if subject=="math":
                print(final_p1+" has won!")
            if subject=="english":
                print(final_p2+" has won!")
        if time=="night":
            subject=input("science or social studies: ")
            if subject=="science":
                print(final_p3+" has won!")
            if subject=="social studies: ":
                print(final_p4+" has won!")
    if color=="red":
        place=input("inside or outside: ")
        if place=="inside":
            subject=input("art or music: ")
            if subject=="art":
                print(final_p5+" has won!")
            if subject=="music":
                print(final_p6+" has won!")
        if place=="outside":
            event=input("academics or sports: ")
            if event=="academics":
                print(final_p7+" has won!")
            if event=="sports":
                print(final_p8+" has won!")
def food_game(play): #function is the final food game with introduction and actions that vary depending on the user's input
    if play=="y": #if the user types in "y", the game will start
        print("Welcome to the random food picker where we help you choose the next food to eat!") #introduces the user to the game
        while True: #infinite loop that will continue to play even after the game ends. it won't end until the user chooses to quit
            print("""What activity would you like to do?
        1. add foods to the list
        2. view the list
        3. remove an item from the list
        4. start playing to get a random food item from your list
                -you need to add food items to your list first (activity 1)
                -you will be given 2 choices to choose from and that will determine the food item you will get
        5. empty the whole list
        6. use a pre-made list
        7. quit""") #explains to the user the activities they could do in the game
            try: #makes sure that the user inputs a number
                choice=int(input("Please input the number of the activity you want to do (1-7): "))
                if choice==1: #if the user chooses to do activity 1, they will be able to add an item to the list "foods"
                    foods.append(input("What food would you like to add to the list?: ")) #adds items of their choice to the list "foods"
                    print("Your item has been successfully added!")
                if choice==2: #if the user chooses to do activity 2, they will be able to view the list "foods"
                    print(foods)
                if choice==3: #if the user chooses to do activity 3, they will be able to remove an item from the list "foods"
                    print(foods) #prints the list to allow the user to see what's in the list
                    foods.remove(input("What food would you like to remove from the list?: ")) #removes items of their choice from the list "foods"
                    print("Your item has been successfully removed!")
                if choice==4: #if the user chooses to do activity 4, the game will start with the "foods" list
                    make_table() #a table will be made using the foods that the user had inputted
                    choose_food() #a series of questions will be asked to choose what food the user will get
                if choice==5: #if the user chooses to do activity 5, they will be able to empty everything in the list "foods"
                    foods.clear()
                    print("The list has been successfully emptied")
                if choice==6: #if the user chooses to do activity 6, they will be able to play with the pre-made list
                    print("This is the pre-made list")
                    for i in range(len(foods_premade)):
                        print(foods_premade[i])
                    yon=input("Would you like to play with this list of foods? (please enter y or n): ") #asks the user if they would like to play with the preamde list
                    if yon=="y": #if they input "y", they would be able to play but nothing will happen if they type "n" and they will be taken back to the menu
                        make_tablefp()
                        choose_foodfp()
                if choice==7: #if the user chooses activity 7, they will be able to end the while loop and quit the game
                    break
            except: #if the user inputs anything other than a number, a message will tell them to input a number
                print("Invalid response, please enter a number")
#main
food_game(input("Would you like to play the game? (please enter y or n): "))
