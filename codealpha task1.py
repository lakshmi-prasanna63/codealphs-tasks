import random

def hangman():
    word_list = ['python', 'hangman', 'developer', 'code', 'program']
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")

    while tries > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"\nWord: {display_word}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            tries -= 1
            print(f"Wrong guess. Tries left: {tries}")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! The word was '{word}'")
            break
    else:
        print(f"Game Over! The word was '{word}'")

hangman()