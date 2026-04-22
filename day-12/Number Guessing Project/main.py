import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
chosen_number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")
while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print("You guessed the number!")
        break
    if guess < chosen_number:
        print("Too low!")
        if attempts != 1:
            print("Guess again.")
        if attempts != 1:
            print(f"You have {attempts - 1} attempts remaining to guess the number.")
    elif guess > chosen_number:
        print("Too high!")
        if attempts != 1:
            print("Guess again.")
        if attempts != 1:
            print(f"You have {attempts - 1} attempts remaining to guess the number.")
    attempts -= 1
    if attempts == 0:
        print(f"You've ran out of attempts! Refresh the page to run again. The number was {chosen_number} ")



