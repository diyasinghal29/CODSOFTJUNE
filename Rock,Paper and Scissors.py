import random
list=['r','p','sc']
chance=10
noofchance=0
computer_point=0
human_point=0
print("\t \t \t \t rock,paper,scissors game\n")
print("r for rock \n p for paper \n sc for scissors\n")
while noofchance<chance:
    _input=input('rock,paper,scissors:')
    _random=random.choice(list)
    if _input==_random:
        print("tie both 0 point to each \n")
    elif _input=="r" and _random=="p":
        computer_point=computer_point+1
        print(f"Your guess {_input} and computer guess is {_random}\n")
        print("Computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif _input=="r" and _random=="sc":
        human_point=human_point+1
        print(f"Your guess {_input} and computer guess is {_random}\n")
        print("human wins 1 point")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif _input=="p" and _random=="sc":
        computer_point=computer_point+1
        print(f"Your guess {_input} and computer guess is {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif _input=="p" and _random=="r":
        human_point=human_point+1
        print(f"Your guess {_input} and computer guess is {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif _input=="sc" and _random=="r":
        computer_point=computer_point+1
        print(f"Your guess {_input} and computer guess is {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    elif _input=="sc" and _random=="p":
        computer_point=computer_point+1
        print(f"Your guess {_input} and computer guess is {_random}\n")
        print(f"computer_point is {computer_point} and your point is {human_point}\n")
    else:
        print("You have wrong input\n")
    noofchance=noofchance+1
    print(f"{chance-noofchance}is left of{chance}\n")
    print("Game over")
    if computer_point==human_point:
        print("Tie")
    elif computer_point > human_point:
        print("Computer wins and you loose")
    else:
        print("you win and computer loose")
    print(f"Your point is {human_point} and computer point is {computer_point}")


