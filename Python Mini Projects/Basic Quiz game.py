a=input("Heyy, Do you want to play this basic quiz game??? ")
if a.lower() != "yes":
    print("Byee byee")
    quit()

print("Welcome to the game!!!")
score=0

answer=input("What is the full form of CPU ?? ")
if answer.lower() == "central processing unit":
    print("Correct answer!!")
    score+=1
else:
    print("Incorrect!! The correct answer is central processing unit")

answer = input("What is the full form of GPU ?? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer!!")
    score += 1
else:
    print("Incorrect!! The correct answer is graphics processing unit")

answer = input("What is the full form of PSU ?? ")
if answer.lower() == "power supply":
    print("Correct answer!!")
    score += 1
else:
    print("Incorrect!! The correct answer is power supply")

answer = input("What is the full form of RAM ?? ")
if answer.lower() == "random access memory":
    print("Correct answer!!")
    score += 1
else:
    print("Incorrect!! The correct answer is random access memory")

answer = input("What is the full form of ROM ?? ")
if answer.lower() == "read only memory":
    print("Correct answer!!")
    score += 1
else:
    print("Incorrect!! The correct answer is read only memory")

print("your final score is ",score," out of 5")
print("your percentage is ",score*20," %")

print("Thanks for playing !!!")