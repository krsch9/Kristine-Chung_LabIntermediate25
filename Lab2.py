
word = "cold"
guessed = []
attempts = 6

print("Welcome to Hangman 2.0!")
print("Try to guess the word by entering a letter. You have 6 attempts.")
while attempts > 0:
    guess = input("Enter a letter:").lower()
    for char in word:
        if char in guessed:
            print(char, end=" ")
        else:
            print("_", end=" ")
    

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
    else:
        if guess in word:
            if guess not in guessed:
                guessed.append(guess)
                attempts -= 1
                print("Correct!")
                if all(char in guessed for char in word):
                 print("Congratulations! You've guessed the word 'cold'!")
                 break
            else:
                print("You already guessed that letter.")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

