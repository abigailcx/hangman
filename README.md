# **A Game of Hangman**

## How to Play
In the terminal, navigate to the hangman repo and run `python3 play_game.py`. The terminal will then prompt the input of a single letter of the alphabet. The number of lives is set to 5 by default. Enter a guess and start playing!

---
## The Game Logic
The `play_game` function is called from `play_game.py`. It creates an instance of the Hangman class and iterates through 3 conditional statements which determine whether the player has won or lost (at which point the game ends), or whether the game continues. If the game continues, the `ask_for_input` method is called from `milestone_3.py`. This method prompts the player to enter a letter. It checks that the letter is valid and then runs the `check_guess` method, which verifies whether the letter guessed by the player is in the word to be guessed. If so, it inserts it into the correct index in the `word_guessed` list. Otherwise, the player loses a life. During gameplay, the player continually guesses letters until they either run out of lives or are successful in guessing the word (whichever occurs first).





---
## Milestones

The `milestone_1.py`, `milestone_2.py` and `milestone_3.py` are development scripts which work on constructing various components of the game logic.


### Milestone 1
The `milestone_1.py` script codes the input validation step of the game. It checks whether the player's input is a single alphabetical character and provides feedback to the player as to whether or not it is valid.

### Milestone 2
The milestone_2.py script uses functional programming to code the input validation step, as well as checking whether the letter that the player has guessed is in the randomly chosen word to be guessed.

The Python script comprises of 2 functions: `check_guess` and `ask_for_input`.
`check_guess` asks the user to enter their guess for the hangman game and checks that their guess is valid (i.e. a single letter of the alphabet).
`ask_for_input` iteratively asks for and checks the player's input.
The word to be guessed is defined at the beginning of the script. The word is randomly selected using Python's `random` module. The `random.choice` selects a word from the `word_list` and assigns it to the variable `word`.

### Milestone 3

milestone_3.py uses object-oriented programming (OOP) to implement a hangman game class. `milestone_3.py` is imported into `play_game.py` to form the completed game.

Within the class constructor, the class is defined with 6 class attributes to store information:
1. **word_list**: the words from which the word to be guessed can be selected
2. **num_lives**: the number of lives remaining for the player (this reduces by 1 every time a player guesses an incorrect letter)
3. **word**: the selected word to be guessed
4. **word_guessed**: the list of letters that have been correctly guessed and where they appear in the word (i.e. a visual representation of the word)
5. **num_letters**: the number of unique letters in the word that have not been guessed
6. **list_of_guesses**: the letters that the player has guessed

The class contains 2 methods: `check_guess` and `ask_for_input`.
The `ask_for_input` method prompts the player to enter a guess. It verifies that the guess is valid and then runs the `check_guess` method.
The `check_guess` method checks whether the letter the player guesses is in the word and if so, inserts it into the correct index in the `word_guessed` list). If the guess is incorrect, the player loses a life. Gameplay continues.
