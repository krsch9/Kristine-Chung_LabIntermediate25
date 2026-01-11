secret = "table"
letters = ("t", "a", "b", "l", "e")
found_letters = []

print("Guess the Secret Word!")
print("First, guess the letters inside this secret word.")

while len(found_letters) < len(letters):
    letter_input = input("Guess the letter: ").lower()
    if len(letter_input) == 1 and letter_input.isalpha():
        if letter_input in letters:
            if letter_input not in found_letters:
                found_letters.append(letter_input)
                print("Correct! Guess the other letters.")
            else:
                print("You already found that letter! Try another one")   
        else:
            print("Wrong! Try again.")
    else:
        print("Invalid input. Please enter a single letter.")
        
print("You have found all the letters! Now guess the secret word.")
word_input = input("Enter the secret word: ").lower()
if word_input == secret:
    print("That is Correct!")
else:
    print("That is wrong! The secret word is 'table'.")