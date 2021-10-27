import random;
import json;
import game_controller;

def load_words():
    with open("/resources/words.json") as file:
        words_file = file;
        words_data = json.loads(words_file.read());
        words = [word.lower() for word in words_data];
    
    return words;
        
points = 0;
positions_found = [];
chances = 0;

def start_game():   
    won = False;
    lose = False;   
   
    words = load_words();
    secret_word = words[random.randrange(0, len(words))].lower();
    
    global chances;
    chances = len(secret_word) * 2;
    
    while(not won and not lose):
        right_guess = False;
        already_found = False;
    
        print("-------------------------")
        alternative = input("What letter will you choose? ").lower().strip();
        print(" ")
        
        for letter in secret_word:
            index = -1;
            
            count = 0;
            # Finds available letter depending on it's position
            for letterFound in secret_word:
                if (letterFound == letter and count not in positions_found):
                    index = count;
                    break;
                count = count + 1;
                
            if (index == -1):
                break;
            
            # Check if the letter from that position was already found
            if (index in positions_found):
                already_found = True;
                continue;
            
            if (alternative == letter):
                right_guess = handle_correct(letter, index)
                break;
        
        handle_guess(already_found, right_guess, secret_word);
        
        letters_left = len(secret_word) - len(positions_found);
        print("You still got {} letters left!".format(letters_left))

def handle_guess(already_found, right_guess, secret_word):
    if (already_found == True):
        print("You already found that position!")
        
    if (right_guess == False):
        handle_incorrect();

    if (chances == 0 or points >= len(secret_word)):
        game_controller.finish_game(points);
        
        print("The correct word is: {}".format(secret_word))
        return;
    
def handle_correct(letter, index):
    print("You got it right! It's letter {} in position {}.".format(letter.upper(), index + 1));

    global points;
    points = points + 1;
    
    positions_found.append(index);
    return True;

def handle_incorrect():
    print("You didn't got it right! Try again...")

    global chances;
    chances = chances - 1;
            
