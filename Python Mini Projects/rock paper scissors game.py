import random

user_wins=0
computer_wins=0
options=['rock','paper','scissor']
while True:
    user_input=input("Type rock/paper/scissor or q to quit: ").lower()
    if user_input=='q':
        break

    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer picked ",computer_pick,".")
    if user_input == 'rock' and computer_pick == 'scissor':
        print("you won!!")
        user_wins+=1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("you won!!")
        user_wins+=1
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("you won!!")
    elif user_input == computer_pick:
        print("both are same, tied")
    else:
        print("computer won")
        computer_wins+=1



print("you won ",user_wins," times.")
print("computer won ",computer_wins," times.")
print("Goodbye !!")
