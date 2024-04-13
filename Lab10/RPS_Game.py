"""
* This program is RPS game
* Teruaki Murakami
* 2023/11/8

* 1. Input the chose
* 2. generate CPU chose
* 3. check PRC game
* 4. count games
"""


import random

intro = "This is PRS game please input your choice"
introSelection = "Please choose your choice"
example ="Please enter your selection for game:\n" \
            "Enter:\n" \
            "\t'R' for Rock\n" \
            "\t'P' for Paper\n" \
            "\t'S' for Scissor\n"
ROCwin = "\nRock crushes scissors"
PAPwin= "\nPaper wraps rock"
SCIwin= "\nScissors cuts paper"
resultwin = "You win!"
resultlose = "You lose!"
resultsame = "Same try again"
def greeting():
    print(intro)

def generateComputersChoice():
    randomnumber = random.randint(1,3)
    if (randomnumber == 1):
        CPUchoice = 'R'
    elif (randomnumber == 2):
        CPUchoice = 'P'
    else:
        CPUchoice = 'S'

    return CPUchoice

def enterPlayersChoice(gameNumber):
    print(introSelection + " #"+ str(gameNumber) + ".")
    print(example)
    choice = input("your choice: ")
    return choice
#game count
i = 0
#data for games
ties = 0
wins = 0
lose = 0
#accumulated wins
accumulatedwins = 0


greeting()

while True:
    i += 1

    #input human chose
    HUM = enterPlayersChoice(i)

    #generate computer choice
    CPU = generateComputersChoice()

    print("For game " + str(i)+"\n")

    if (HUM == 'R'):
        if (CPU == 'R'):
            print("you played 'Rock' and \nComputer played 'Rock'")
            print(resultsame)
            ties += 1
        elif (CPU == 'P'):
            print("you played 'Rock' and \nComputer played 'Paper'")
            print(PAPwin)
            print(resultlose)
            lose += 1
        elif (CPU == 'S'):
            print("you played 'Rock' and \nComputer played 'Scissors'")
            print(SCIwin)
            print(resultwin)
            wins += 1
            accumulatedwins += 1
    elif (HUM == 'P'):
        if (CPU == 'R'):
            print("you played 'Paper' and \nComputer played 'Rock'")
            print(ROCwin)
            print(resultlose)
            lose += 1
        elif (CPU == 'P'):
            print("you played 'Paper' and \nComputer played 'Paper'")
            print(resultsame)
            ties += 1
        elif (CPU == 'S'):
            print("you played 'Paper' and \nComputer played 'Scissors'")
            print(SCIwin)
            print(resultwin)
            wins += 1
            accumulatedwins += 1
    elif (HUM == 'S'):
        if (CPU == 'R'):
            print("you played 'Scissors' and \nComputer played 'Rock'")
            print(SCIwin)
            print(resultlose)
            lose += 1
        elif (CPU == 'P'):
            print("you played 'Scissors' and \nComputer played 'Paper'")
            print(SCIwin)
            print(resultwin)
            wins += 1
            accumulatedwins += 1
        elif (CPU == 'S'):
            print("you played 'Scissors' and \nComputer played 'Scissors'")
            print(resultsame)
            ties += 1

    if i%3 == 0:
        print("For total of 3 games,")
        print("There were "+ str(ties) +" ties")
        print("There were "+ str(wins) +" wins for you")
        print("There were "+ str(lose) +" wins for computers")
        print("accumulated wins "+ str(accumulatedwins))

        ties = 0
        wins = 0
        lose = 0

        if input("would you play again?(y or n):") == 'y':

            i = 0

        else:

            break