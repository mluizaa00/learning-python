import random;
import game_controller;

# Setted values
difficulty_rates = list([8, 5, 3])
start_points = list([100, 60, 50])
lose_points = list([10, 15, 20])
minimum_number = random.randrange(1, 10);
maximum_number = random.randrange(10, 100);
secret_number = int(random.randrange(minimum_number, maximum_number));

difficulty = 0;
total_chances = difficulty_rates[difficulty];

current_round = 1;

current_points = start_points[difficulty]
points_to_lose = lose_points[difficulty]

limit = "{} to {}".format(minimum_number, maximum_number);

def start_game():
    print("Welcome to the Guess Game!")

    print("[1] Easy [2] Medium [3] Hard")
    dif = int(input("Type your difficulty level: "));

    if (dif < 1 or dif > 3):
        difficulty = 1;
        print("You typed a wrong difficulty! Using Easy as default.");

    difficulty = dif - 1;
    total_chances = difficulty_rates[difficulty];

    print("You selected the difficult {}, you have a total of {} chances".format(difficulty + 1, total_chances))

    start_game_loop();

    game_controller.finish_game();
    print("The secret number is {}".format(secret_number));

def start_game_loop():
    for current_round in range(1, total_chances):
        print("Current round: {}".format(str(current_round)))
        number = int(input("Type your number between {}: ".format(limit)));

        if (number < minimum_number or number > maximum_number):
            print("You can only print numbers between {}! ".format(limit))
            continue;

        if (number == secret_number):
            print("You typed the right number!")
            break;

        if (number > secret_number):
            print("You typed the wrong number! The number typed is higher than the secret number.")
        else:
            print("You typed the wrong number! The number typed is lower than the secret number.")

        current_points = current_points - points_to_lose;
