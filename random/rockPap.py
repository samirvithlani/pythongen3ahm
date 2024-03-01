import random
print("###################### ROCK-PAPER-SCISSORS ######################")
choices = ["rock", "paper", "scissors"]
computerCoice =None
computerChoiceData = None
score = 0

while True:
    print("Press y for start game and n for exit")
    start = input()
    if start == "n" or start =="N":
        break
    else:
        gameInput = input("Enter your choice: ")
        if gameInput not in choices:
            print("Invalid choice")
            break
        else:
            print('Your choice is:', gameInput)
            print('Computer choice is')
            computerCoice = random.randint(0,2) #0
            computerChoiceData = choices[computerCoice]
            print("computer choice is:", computerChoiceData)
            
            if gameInput == computerChoiceData:
                print("Match draw")
            elif (gameInput  =="rock" and computerChoiceData =="scissors") or(gameInput == "scissors" and computerChoiceData == "paper") or (gameInput == "paper" and computerChoiceData == "rock"):
                print("You win")
                score += 1
            else:
                print("Computer win")
                break

print("Your score is:", score)                
                
            
        