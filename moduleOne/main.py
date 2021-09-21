print("Welcome to the Game!")

secret_number = 20;

total_chances = 10;
current_chance = 1;

minimum_number = 1;
maximum_number = 100;

limit = "{} to {}", minimum_number, maximum_number;

for current_chance in range(1, total_chances):
    print("Available chances: {}", str(current_chance))
    number = int(input("Type your number between {}: ", limit));

    if (minimum_number < 1 | maximum_number > 100):
        print("You can only print numbers between {}!", limit)
        continue;

    if (number == secret_number):
        print("You typed the right number!")
        break;

    if (number > secret_number):
        print("You typed the wrong number! The number typed is higher than the secret number.")
    else:
        print("You typed the wrong number! The number typed is lower than the secret number.")

print("The game was finished!")