import random

word_list = ["raspberry", "strawberry", "banana", "mango", "kiwi"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter of the alphabet:\t")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input. The input needs to be a single letter of the alphabet.")