import random
randint = random.randint(1,10)
while True:
    guess = int(input("Guess a number between 1 & 10 \n"))
    if guess == randint:
        print("Congrats! You're a winner!")
        break
    else:
        print("Aww... Not a winner this time :( How about you try again!")
