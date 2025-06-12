import random
print("Guess the number".upper())
answer = random.randint(1,50)
print("Do you want to play this game?")
agree = input("YES/NO: ")
name = input("Enter your name: ")
if agree == "YES" or agree == "yes":
    print("Welcome,",name, "to the game!")
    print("RULE:\n1.There are two levels to the game EASY and HARD.\n2.Guess the number wisely before running out of the attempts." \
    "\n3.You have to guess number between 1 to 50")
    confirm = input("type \"GO\" to start the game: ")
    if confirm == "GO" or confirm == "go":
        start = int(input("Choose the Level of the game:\n1.press '1' for EASY LEVEL.\n2.press '2' for HARD LEVEL.\nENTER YOUR CHOICE:"))
        if start == 1:
            print("You have chosen EASY LEVEL")
            attempt = 10
            while attempt > 0 and attempt <= 10:
                print("You have", attempt, "attempts")
                try:
                    guess = int(input("Enter your guessed number: "))
                except ValueError:
                    print("Invalid number input. Please, enter a WHOLE number")
                    continue
                if guess == answer:
                    print("You guessed the number RIGHT, it was:", answer)
                    print("Congratulation,", name, "you won!!")
                    quit()
                elif guess > answer:
                    print("Your guessed number is BIGGER then actual answer. ")
                elif guess < answer:
                    print("Your guessed number is SMALLER then actual answer.")
                attempt-=1
            else:
                print("GAME OVER!")
                print("The answer was:", answer)
        elif start == 2:
            print("You have chosen HARD LEVEL")
            attempt = 5
            while attempt > 0 and attempt <= 5:
                print("You have", attempt, "attempts")
                try:
                    guess = int(input("Enter your guessed number: "))
                except ValueError:
                    print("Invalid number input. Please, enter a WHOLE number")
                    continue
                if guess == answer:
                    print("You guessed the number RIGHT, it was:", answer)
                    print("Congratulation,", name, "you won!!")
                    quit()
                elif guess > answer:
                    print("Your guessed number is BIGGER then actual answer. ")
                elif guess < answer:
                    print("Your guessed number is SMALLER then actual answer.")
                attempt-=1
            else:
                print("GAME OVER!")
                print("The answer was:", answer)
                    
    else:
        print("We would surely like to, Welcome you later any time!")
        quit()
elif agree == "NO" or agree == "no":
    print("We would surely like to, Welcome you later any time!")
    quit()
