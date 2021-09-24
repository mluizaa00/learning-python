won = False;
lose = False;

words = list(["laila", "luke", "preta", "gigi"])

def start_game():
    while(not won and not lose):
        alternative = input("What letter will you choose? ");
        secret_word = words[0]

        index = 1;
        right_guess = False;
        
        for letter in secret_word:
            if (alternative == letter):
                print("You got it right! It's letter {} in position {}.".format(letter, index))
                index = index + 1;
                right_guess = True;
                break;
        
        if (right_guess == False):
            print("You didn't got it right! Try again...")
            
