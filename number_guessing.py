import random

attempt_list = []

def showScore():
    if len(attemt_list) <= 0:
        print("There is currently no high score. It's your for taking.")
    else:
        print("The currnt high score is{}".format)
def startGame():
    random_number = random.randint(1,10)
    print("Hello, welcome to the number guessing game.")
    player_name = input("Enter your name")
    wannaPlay = input("hi, {} do you want to play the game? Enter(yes/no)").format((player_name))

    attempt = 0
    showScore()

    while wannaPlay.lower() == "yes":
        try:
            guess = input("Guess a number betweenn 1 to 10")

            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please enter a number whithin a valid range")
            if int(guess) == random_number:
                print("Congrats you guessd it!")
                attempt +=1
                attempt_list.append(attempt)
                print(" it took you {} attempts".format(attempt))
                playagain = input("Would you like to play again?")
                