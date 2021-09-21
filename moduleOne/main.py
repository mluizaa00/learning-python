print("Welcome to the Game!")

secret_number = 20;

total_chances = 10;
current_chance = 1;

while (current_chance <= total_chances):
    print("Available chances: " + str(current_chance))
    number = int(input("Type your number: "));

    if (number == secret_number):
        print("You typed the right number!")
    elif (number > secret_number):
        print("You typed the wrong number! The number typed is higher than the secret number.")
    else:
        print("You typed the wrong number! The number typed is lower than the secret number.")

    current_chance = current_chance + 1;