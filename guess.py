import random

n =  random.randint(0, 10)
guess = int(input("guess a number between 0 and 10: "))

while True:
    if guess == n:
        print("Topdingiz")
        break
