def guessSecret():
    secret = "secret"
    guess = input("Please enter secret code: ")

    if guess == secret:
        print("Secret code is correct!")
    else:
        print("Secret code is incorrect!")
        tryagain = input("Do you want to try again? (y/n)")
        if tryagain == 'y':
            guessSecret()
        else:
            exit()

guessSecret()

