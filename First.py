import random
computer = random.choice([1,2,3])
myStr = input("Enter a number between 1 and 3: ")
myDict = {"1": "snake", "2": "water", "3": "gun"}
reverseDict = {"snake": "1", "water": "2", "gun": "3"}

if myStr not in myDict:
    print("Invalid input. Please enter 1, 2, or 3.")
else:
    me = myDict[myStr]
    print("You chose:", me)
    print("Computer chose:", myDict[str(computer)])
    if myStr == str(computer):
        print("It's a Draw!")
    elif (myStr == "1" and computer == 3) or (myStr == "2" and computer == 1) or (myStr == "3" and computer == 2):
        print("You Lose!")
    else:
        print("You Win!")