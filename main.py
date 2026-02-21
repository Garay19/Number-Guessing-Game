import random
import os
import time

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def counter(val: int | float) -> int | float:
    time.sleep(val)

def space():
    print()

def chances(option):
    match option:
        case 1:
            return 10
        case 2:
            return 5
        case 3:
            return 3
        case _:
            return 5

def main():
    difficulty = [
        "Easy", 
        "Medium", 
        "Hard"
        ]
    
    while True:
        clear_terminal()
        print("Welcome to the Number Guessing Game!")
        counter(0.5)
        print("I'm thinking of a number between 1 and 100.")
        counter(0.5)

        print("Please select the difficulty level:")
        counter(0.2)
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")


        option = int(input("Enter Choice (1-3): "))
        while option not in [1, 2, 3]:
            option = int(input("Enter Choice (1-3): "))        
        space()

        number = random.randint(1, 100)
        chance = chances(option)
        attempts = 0

        print(f"Great! You have selected the {difficulty[option - 1]} difficulty level.")
        print(f"You have {chance} chances to guess the correct number.")

        guessed = False

        while not guessed:
            space()
            if chance == 0:
                print("You've run out of chances. You lose!")
                break
            
            try:
                guess = int(input("Enter guess: "))
            except ValueError:
                guess = int(input("Enter guess (numbers only): "))

            if guess < number:
                chance -= 1
                attempts += 1
                print(f"The number is higher than {guess}.")
            elif guess > number:
                chance -= 1
                attempts += 1
                print(f"The number is lower than {guess}.")
            else:
                attempts += 1
                guessed = True
                break

        if guessed == True:
            print(f"You've guessed the correct number in {attempts} attempts, congrats!")

        print("Thanks for playing the game :3")
        space()
        restart = input("Play again? (y/n): ").lower()
        while restart not in ["y", "n"]:
            restart = input("Enter (y/n) only: ")
        if restart == "n":
            break
        
if __name__ == "__main__":
    main()