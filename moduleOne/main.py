import random;

print("Welcome to the Game!")

difficulty_rates = list([8, 5, 3])

start_points = list([100, 60, 50])
lose_points = list([10, 15, 20])

print("[1] Easy [2] Medium [3] Hard")
difficulty = int(input("Type your difficulty level: "));

if (difficulty < 1 or difficulty > 3):
    difficulty = 1;
    print("You typed a wrong difficulty! Using Easy as default.");

difficulty = difficulty - 1;

total_chances = difficulty_rates[difficulty];
print("You selected the difficult {}, you have a total of {} chances".format(difficulty + 1, total_chances))

current_round = 1;

minimum_number = 1;
maximum_number = 100;

current_points = start_points[difficulty]
points_to_lose = lose_points[difficulty]

secret_number = int(random.randrange(minimum_number, maximum_number));

limit = "{} to {}".format(minimum_number, maximum_number);

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

print("The game was finished!");
print("Final points: {}".format(current_points))
print("The secret number is {}".format(secret_number));