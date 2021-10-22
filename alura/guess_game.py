import random;
import game_controller;

lose_points = {10, 20, 30}

minimum_number = 1;
maximum_number = random.randrange(50, 100);
secret_number = int(random.randrange(minimum_number, maximum_number));

difficulty = 0;
difficulties = {"Easy", "Medium", "Hard"}
difficulty_rates = list([8, 5, 3])

total_chances = difficulty_rates[difficulty];

current_round = 1;

current_points = 100;
points_to_lose = lose_points[difficulty]

limit = "{} to {}".format(minimum_number, maximum_number);

def start_game():
    print("Welcome to the Guess Game!")

    select_difficulty();
    start_game_loop();

    game_controller.finish_game(current_points);
    print("The secret number is {}".format(secret_number));

def select_difficulty():
    print(get_difficulty_title());
    dif_var = int(input("Type your difficulty level: "));

    if (dif_var < 1 or dif_var > 3):
        difficulty = 1;
        print("You typed a wrong difficulty! Using {} as default.".format(difficulties[difficulty - 1]));

    difficulty = dif_var - 1;
    total_chances = difficulty_rates[difficulty];

    print("You selected the difficult {}, you have a total of {} chances".format(difficulty + 1, total_chances));
    
def get_difficulty_title():
    title = "";
    
    count = 0;
    for difficulty_title in difficulties:
        if (count == len(difficulties)):
            title = title + "[{}] {}.".format(count + 1, difficulty_title)
            continue;
        
        title = title + "[{}] {},".format(count + 1, difficulty_title)
        count = count + 1;
        
    return title;
                                                                             
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

        global current_points;
        current_points = current_points - points_to_lose;