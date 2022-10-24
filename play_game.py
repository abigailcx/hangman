from milestone_3 import Hangman

def play_game():
    word_list = ["raspberry", "strawberry", "banana", "mango", "kiwi"]
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost! Better luck next time.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print(f"Congratulations! The word is {game.word.upper()}. You have won the game!")
            break

play_game()
