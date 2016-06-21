'''
Play Rock Paper Scissors against the computer

This project was built as a final project to the Spring 2016 Intro to Python. This project is extremely basic so that I could implement the following components of the course:

'''

import random #How the computer chooses

'''Convert Computers Guess to a Score ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
def computer_number():
    #get a random number in the range of 1 through 3
    num = random.randrange(1,4)
    #if/elif statement
    if num == 1:
        print("Computer choose Rock")
    elif num == 2:
        print("Computer choose Paper")
    elif num == 3:
        print("Computer choose Scissors")
    #return the number
    return num

'''Ask User's Name 1st time ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
firstRun=True
def user_name():
    global firstRun
    if firstRun:
        global user_name
        user_name = raw_input("[What is your name?]")
        firstRun=False
    else:
        pass

'''Convert Users Guess to a Score ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
def user_guess():
    #get the user's guess
    guess = raw_input("[Please enter your choice:]").lower()
    #while guess == 'paper' or guess == 'rock' or guess == 'scissors':
    if is_valid_guess(guess):
        #assign 1 to rock
        if guess == 'rock' or guess == 'r' or guess == '1':
            number = 1
        #assign 2 to paper
        elif guess == 'paper' or guess == 'p' or guess == '2':
            number = 2
        #assign 3 to scissors
        elif guess == 'scissors' or guess == 's' or guess == '3':
            number = 3
        return number

    else:
        print("[!!! Please choose between Rock, Paper, or Scissors !!!]")
        return user_guess()

'''Check Users Input/Guess ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
def is_valid_guess(guess):
    #Convert input to lower case
    return guess.lower() in ('rock','r','1','paper','p','2','scissors','s','3')
    if guess in ('rock','r','1','paper','p','2','scissors','s','3'):
        status = True
    else:
        status = False
    return status

'''Play again ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~~~~~'''
def restart():
    while True:
        answer = raw_input("[Would you like to play again?]").lower()
        #if/elif statement
        if answer == 'y' or answer == 'yes':
            main()
        elif answer == 'n' or answer == 'no':
            print("Thanks %s for playing...Goodbye!" % (user_name))
            return False
        else:
            print("Invalid input yes or no")

'''Determine Winner ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
#results function
def results(num, number):
    #find the difference in the two numbers
    difference = num - number
    #if/elif statement
    if difference == 0:
        print("TIE!")
        #call restart
        restart()
    elif difference % 3 == 1:
        print ("Sorry %s! You lost :)" % (user_name))
        #call restart
        restart()
    elif difference % 3 == 2:
        print ("CONGRATS %s! You won :)" % (user_name))
        #call restart
        restart()

''' Game Sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
def rps():
    user_name()
    #intro message
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Welcome! ~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Let's play some Rock, Paper, Scissors!")
    #call the user's guess function
    number = user_guess()
    #call the computer's number function
    num = computer_number()
    #call the results function
    results(num, number)

'''required to run main function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
if __name__ == '__rps__':
    rps()