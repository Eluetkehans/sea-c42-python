import random

answer = random.randint(1, 10)

done = False

while(True):
    guess = int(input("Pick a number between 1 and 10, silly: "))
    if(guess < answer):
        print("Too low!")
    elif(guess > answer):
        print("Too high!")
    else:
        print("Winner, winner, chicken dinner!")
        break
