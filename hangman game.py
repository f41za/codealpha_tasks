import random
import nltk


def choose_random():
    """
    Function to choose a random word from the NLTK words corpus.
    """
    words = nltk.corpus.words.words()
    return random.choice(words).lower()


def hangman():
    """
    Main function implementing the Hangman game.
    """
    while True:
        # Choose a random word
        word = choose_random()
        # Initialize the display output and other variables
        out = [" _ "]*len(word)  # Display output for guessed and hidden letters
        len_word = len(word)  # Counter for remaining letters to be guessed
        tries = 10  # Number of allowed tries
        lst_used_letters = []  # List to store already used letters
        print("".join(out))  # Display initial state of the word
        while True:
            # Get user input for letter guess
            letter = (input("Guess a letter: ")).lower()
            # Validate user input
            if len(letter) > 1 or (not letter.isalpha()) or letter == "":
                print("Please enter a valid letter.")
            elif letter not in lst_used_letters:
                # Add the letter to the list of used letters
                lst_used_letters.append(letter)
                if letter in word:
                    # Update the display output if the guessed letter is in the word
                    found_indices = [pos for pos, char in enumerate(word) if char == letter]
                    if found_indices:
                        for pos in found_indices:
                            out[pos] = letter
                            len_word -= 1
                        print("".join(out))  # Display the updated word
                else:
                    # Handle incorrect guess
                    print("Incorrect. Try again! :(")
                    tries -= 1
                    print("".join(out))  # Display the current state of the word
                    print(f"No. of tries left: {tries}")
            else:
                # Inform the user if the letter has already been tried
                print("You have already tried this letter. Try using another!")
                print("".join(out))  # Display the current state of the word
            # Check if the game is won or lost
            if len_word == 0:
                print("Congratulations! You have successfully guessed the word!")
                break
            elif tries == 0:
                print(f'''It appears you have used up the number of tries :(
The word was {word}. Better luck next time!''')
                break
        # Ask the user if they want to play again
        play_again = (input("Do you want to play again? (y/n): ")).lower()
        if play_again != 'y':
            print("Goodbye!")
            break
    return

hangman()  # Call the hangman function to start the game
