#Winni Lu
#1/8/25
#multiplication quiz
#init
import random
#fucntions
def mult_quiz():
    print("Welcome to the multiplication quiz. Try to answer as many right as you can!") #introduces the game
    global questions
    global correct
    questions=0
    correct=0
    for i in range(5):
        questions=questions+1
        print("Question "+ str(questions)+" of 5") #informs the user the question they're on
        num1=random.randint(0,10)
        num2=random.randint(0,10)
        print("What is "+ str(num1)+" x "+str(num2))
        ur_ans=int(input("Please enter your answer: ")) #get the user input
        print("Your answer: "+str(ur_ans)) #show the user their answer
        if ur_ans==num1*num2:
            print("Correct!")
            correct=correct+1
        else:
            print("Incorrect. The answer was "+str(num1*num2)) #informs the user of the correct answer
    print("Congratulations on completing the quiz. You got "+str(correct)+" out of 5 questions correct!")
#main
mult_quiz()
