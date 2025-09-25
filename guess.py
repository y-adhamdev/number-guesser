import random
# Ushbu o'yin foydalanuvchi raqam kiritadi qachonki u yutmagunigacha
n =  random.randint(0, 10)

while True:
    guess = int(input("guess a number between 1  and 10: "))
    if guess == n:
        print("Topdingiz🔥")
        break
