user_guess = input("Enter the word to be guessed")
user_clue = input("Enter the hint for the guess")
guess_count = 0
guess_limit =3

while guess_count < guess_limit:

    user_entry = input("Enter the Word")

    if user_entry != user_guess:
        print("Sorry!!! not Correct, Try Again!!!")

    else:

        print("Hurray!!! You Guessed It Right!!!")
        print("You are a CHAMPION")
        break
    guess_count = guess_count + 1

if guess_count == guess_limit :
    print("OOPSS you are out of Attempts!!!HA! HA! HA! Game Wins ")
