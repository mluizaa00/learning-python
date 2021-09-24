import guess_game;

print("[1] Guess")
game = int(input("Choose your game: "))

if (game < 0 or game > 1):
    print("You typed a wrong game number! Use between 1 to 1");

if (game == 1):
    print("You selected the Guess game")
    guess_game.start_game();
