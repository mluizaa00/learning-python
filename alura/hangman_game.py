import random;
import game_controller;

won = False;
lose = False;

words = list(["laila", "luke", "preta", "gigi"])
secret_word = words[random.randrange(0, 4)].lower();

positions_found = list();

chances = 5;
points = 0;

def start_game():
    while(not won and not lose):
        alternative = input("What letter will you choose? ").lower().strip();
        right_guess = False;
        
        for letter in secret_word:
            if (alternative == letter):
                right_guess = handle_correct(letter)
                break;
        
        if (right_guess == False):
            handle_incorrect();

        if (chances == 0):
            game_controller.finish_game(points);
            return;

def handle_correct(letter):
    print("You got it right! It's letter {} in position {}.".format(letter, secret_word.find(letter) + 1));

    global points;
    points = points + 1;
    return True;

def handle_incorrect():
    print("You didn't got it right! Try again...")
    global chances;
    chances = chances - 1;
            
