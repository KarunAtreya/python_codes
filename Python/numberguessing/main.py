import random

print("Welcome to number Guessing Game")
while input("Do you want to play?(Y/N)")=="Y":
    game_type=input("Enter the difficulty level you want? Type E for Easy or H for Hard")
    print("I am guessing a number from 1 to 100")
    game_level={
    "H": 5,
    "E": 10,
    }
    no_of_attempts=game_level[game_type]
    computer_number=random.randint(0,100)
    user_guess=int(input("Make a guess:"))
    game_won=False
    while no_of_attempts!=0 and game_won is False:
        if computer_number==user_guess:
            no_of_attempts-=1
            print(f"You have {no_of_attempts} attempts left")
            print("You guessed it right. You Won")
            game_won=True
        elif computer_number>user_guess:
            print("Number is higher")
            no_of_attempts-=1
            print(f"You have {no_of_attempts} attempts left")
            user_guess=int(input("Make another guess:"))  
        else:
            print("Number is lower")
            no_of_attempts-=1
            print(f"You have {no_of_attempts} attempts left")
            user_guess=int(input("Make another guess:"))  
        print("You have run out of guesses. You Loose.")

