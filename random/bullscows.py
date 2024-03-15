secret_number = "549"
attempts = 0

while True:
    guess = input("Enter a number: ")
    attempts += 1
    if len(guess) != 3 or not guess.isdigit():
        print("Invalid input. Enter a 3 digit number")
        continue
    
    bulls = 0
    cows = 0
    
    # Counting bulls and cows
    for digit in guess:
        if digit in secret_number:
            if guess.index(digit) == secret_number.index(digit):
                cows += 1
            else:
                bulls += 1
    
    print(f"{cows} cows, {bulls} bulls")
    
    if cows == 3:
        print(f"Congratulations! You guessed the number in {attempts} attempts")
        break
