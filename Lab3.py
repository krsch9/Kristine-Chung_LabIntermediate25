def updateText(secret_word, maximum_attempts=6):
    guessed_letters = []
    attempts = maximum_attempts

    print("Welcome to Hangman!")
    print(f"Let's guess the word by entering a letter. You have {maximum_attempts} attempts.")

    while attempts > 0:
        display_guess = []
        for char in secret_word:
            if char in guessed_letters:
                display_guess.append(char)
            else:
                display_guess.append("_")
        display_word = ''.join(display_guess)
        print(display_word)

        if display_word == secret_word:
            print(f"Congratulations! You've guessed the word '{secret_word}'!")
            return

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        else:
            if guess in secret_word:
                attempts += 1 
                if guess not in guessed_letters:
                    guessed_letters.append(guess)
                    print("Correct!")
                else:
                    print("You already guessed that letter.")
            else:
                print("Wrong guess!")
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

    print(f"Sorry, you've run out of attempts. The secret word was '{secret_word}'.")

updateText("dinosaur", 6)