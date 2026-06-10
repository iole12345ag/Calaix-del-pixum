import random

while True:

    print("We are going to play rock paper scissors")


    def tryd():
    
        print("1. Paper")
        print("2. Rock")
        print("3. Scissors")

        guess = int(input("Which one do you want to choose?: "))

        randomChoice =random.randint(1,3)

        if guess == randomChoice:
            print("I choosed the same, thats a tie!")

        if guess == 2 and randomChoice == 1:
            print("I choosed Paper, I won!")

        if guess == 3 and randomChoice == 2:
            print("I choosed Rock, I won!")

        if guess == 1 and randomChoice == 3:
            print("I choosed Paper, I won!")

        if guess == 1 and randomChoice == 2:
            print("I choosed Rock, You won...")

        if guess == 2 and randomChoice == 3:
            print("I choosed Scissors, You won...")

        if guess == 3 and randomChoice == 1:
            print("I choosed Paper, You won...")
 
    tryd()

