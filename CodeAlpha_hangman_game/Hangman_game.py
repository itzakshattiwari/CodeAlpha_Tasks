import random

def play_hangman():
    words = ["python", "variable", "function", "syntax", "iteration"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_tries = 6
    
    print("Welcome to Hangman!")
    print(f"You have {max_tries} incorrect guesses allowed.")
    
    while incorrect_guesses < max_tries:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"\nWord: {display_word.strip()}")
        print(f"Guesses remaining: {max_tries - incorrect_guesses}")
        
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            return 
            
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            guessed_letters.append(guess)
            
            if guess in secret_word:
                print("Good guess!")
            else:
                print("Incorrect guess.")
                incorrect_guesses += 1
                
    print(f"\nGame Over! The correct word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()