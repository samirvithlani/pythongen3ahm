secret_number = "549"
attempts = 0

#465
while True:
    guess = input("Enter a number: ")
    attempts += 1
    if  len(guess)!= 3 or guess.isdigit() == False:
        print("Invalid input. Enter a 3 digit number")
        continue
    
    bulls = 0
    cows = 0
    
    for i in range(3):
        if secret_number[i] == guess[i]:
            cows += 1
        elif guess[i] in secret_number:
            bulls += 1
    
    print(f"{cows} cows, {bulls} bulls")
    
    if cows == 3:
        print(f"Congratulations! You guessed the number in {attempts} attempts")
        break            