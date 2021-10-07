import random;
import game_controller;

won = False;
lose = False;

words = ["laila", "luke", "preta", "gigi"]
secret_word = words[random.randrange(0, len(words))].lower();

positions_found = [];

chances = 5;
points = 0;

def start_game():        
    while(not won and not lose):
        right_guess = False;
        already_found = False;
    
        alternative = input("What letter will you choose? ").lower().strip();
        
        for letter in secret_word:
            index = secret_word.find(letter);
            
            # Check if the letter from that position was already found
            if (index in positions_found):
                already_found = True;
                continue;
            
            if (alternative == letter):
                right_guess = handle_correct(letter, index)
                break;
        
        if (already_found == True):
            print("You already found that position!")
        
        if (right_guess == False):
            handle_incorrect();

        if (chances == 0 | points >= len(secret_word)):
            game_controller.finish_game(points);
            return;

def handle_correct(letter, index):
    print("You got it right! It's letter {} in position {}.".format(letter, index + 1));

    global points;
    points = points + 1;
    
    positions_found.append(index);
    return True;

def handle_incorrect():
    print("You didn't got it right! Try again...")

    global chances;
    chances = chances - 1;
            
