import random

cpu = random.randint(1,100)

counter = 5

game = True
while game:
    user = int(input("Guess the number : "))

    if cpu == user:
        print("Congrats, You have guessed the number...")
        game = False
    elif cpu > user:
        print("You have guessed smaller number...")
    elif cpu < user:
        print("You have guessed larger number...")
    else:
        print("Invalid Input...")

    counter -= 1
    print("Chances Left :",counter)

    if counter == 0:
        print("You lost the game...Number was",cpu)
        break


