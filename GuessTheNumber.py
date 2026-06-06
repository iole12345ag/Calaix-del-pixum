import random

print("I am going to think of a random number between 1 and 100")
print("You have tu guess it")

randomNumber = random.randint(1,100)

def guessNumber():

    number = float(input("What's you guess?: "))    

    if  number == randomNumber:
        print("Wow, you have won!")

    elif number >= randomNumber:
        print("The number is smaller")
        guessNumber()

    elif number <= randomNumber:
        print("The number is higher")
        guessNumber()

guessNumber()