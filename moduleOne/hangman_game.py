import random;

won = False;
lose = False;

words = list(["laila", "luke", "preta", "gigi"])
secret_word = list[random.randrange(1, words.__len__)]

def start_game():
    while(not won and not lose):
        alternative = input("Qual a letra? ");

        index = 0;
        for letter in secret_word:
            if (alternative == letter):
                print("You got it right! It's letter {} in position {}.".format(letter, index))
                index = index + 1