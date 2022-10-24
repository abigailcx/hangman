import random

word_list = ["raspberry", "strawberry", "banana", "mango", "kiwi"]
word = random.choice(word_list)
print(word)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single letter of the alphabet:\t")
        if len(guess) == 1 and guess.isalpha() == True:
            check_guess(guess)
        else:
            print("Invalid input. Please enter a single alphabetical character.")
        

ask_for_input()
