import guess_game, hangman_game;

def start_selector():
    print("[1] Guess [2] Hangman")
    game = int(input("Choose your game: "))

    if (game < 0 or game > 2):
        print("You typed a wrong game number! Use between 1 to 2");

    if (game == 1):
        print("You selected the Guess game")
        guess_game.start_game();
        return;
    
    if (game == 2):
        print("You selected the Hangman game")
        hangman_game.start_game();

if (__name__ == "__main__"):
    start_selector();
