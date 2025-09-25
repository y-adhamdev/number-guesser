import random

n =  random.randint(0, 10)

while True:
    guess = int(input("guess a number between -3 and 10: "))
    if guess == n:
        print("Topdingiz")
        break
