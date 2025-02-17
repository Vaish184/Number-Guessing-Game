import random as rand
original_number=rand.randint(1,100)
guess=5
print("-"*10+"Welcome to Number Guessing game"+"-"*10)
print("choose a number between 1 to 100")
while(guess>0):
    choosen_number=int(input("Enter your guess: "))
    if choosen_number==original_number:
        print("yay!! you got it!! You won")
        break
    else:
        guess-=1
        if choosen_number<original_number:
            print("Guess a big number than ",choosen_number)
        else:
            print("Guess a small number than ",choosen_number)
        if guess>0:
            print("Go on ! You still have a chance")
        else:
            print("better luck next time")
            print("The original number = ",original_number)
