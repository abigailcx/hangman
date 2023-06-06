import random


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = [''] * len(self.word) # list of the letters of the word, with '' for each letter not yet guessed
        self.num_letters = len(set(self.word).difference(set(self.word_guessed))) # num unique letters in word that have not been guessed
        self.list_of_guesses = []


    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess.upper()} is in the word.")
            for index, char in enumerate(self.word):
                if char == guess:
                    self.word_guessed[index] = guess
            print(f"{self.word_guessed}")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess.upper()} is not in the word.")
            if self.num_lives == 1:
                print(f"You have {self.num_lives} life left.")
            else:
                print(f"You have {self.num_lives} lives left.")
        self.num_letters = len(set(self.word).difference(set(self.word_guessed)))


    def ask_for_input(self):
        guess = input("Enter a single letter of the alphabet:\t")
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")  
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
