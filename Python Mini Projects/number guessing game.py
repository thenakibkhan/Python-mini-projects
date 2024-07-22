import random
maxrange=input("Enter a number to set the max limit from 0 for you to guess between : ")

if maxrange.isdigit():
    maxrange=int(maxrange)

    if maxrange<=0:
        print("please type a number greater than 0")
        quit()

else:
    print("please enter a number next time")
    quit()

random_number=random.randint(0,maxrange)
guesses=0

while True:
    guesses+=1
    user_guess=input("make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time")
        continue

    if user_guess == random_number:
        print("you got it right!!")
        break

    elif user_guess > random_number:
        print("you are above the number")
    else:
        print("you are below the number")


print("you got it in ",guesses," guesses")