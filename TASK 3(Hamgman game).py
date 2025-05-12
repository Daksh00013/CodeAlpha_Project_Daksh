import random  # Importing the random module to choose a random word

# List of words
words = ["python", "hangman", "programming", "challenge", "developer"]

# Choose a random word from the list
word = random.choice(words)

# List to show the word with underscores (e.g. _ _ _ _)
guessed_word = ["_"] * len(word)

# Set to hold letters the player has already guessed
guessed_letters = set()

# Number of attempts the player has
attempts_left = 6

print("Welcome to Hangman!")
print("Guess the word letter by letter.")

# Main game loop: runs until player runs out of attempts or guesses word
while attempts_left > 0 and "_" in guessed_word:
    # Print current state of the guessed word and attempts remaining
    print("\nWord: " + " ".join(guessed_word))
    print(f"Attempts remaining: {attempts_left}")
    
    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Check if input is valid (only one alphabet letter)
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to the set of guessed letters
    guessed_letters.add(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        # Reveal the positions of the correctly guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        attempts_left -= 1
        print("Wrong guess.")

# After exiting the loop, check win/loss
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
