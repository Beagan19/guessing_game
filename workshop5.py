import random


def guess_random_num(tries, start, stop):
    target_number = random.randint(start, stop)
    while tries != 0:
        print("You have", tries, "left.")
        user_guess = input("Guess a number between " +
                           str(start) + " and " + str(stop) + ". ")
        if int(user_guess) == target_number:
            print("You guessed the correct number!")
            return
        elif int(user_guess) > target_number:
            print("Guess lower!")
        elif int(user_guess) < target_number:
            print("Guess higher!")

        tries -= 1

        if tries == 0:
            print("You have failed to guess the number:", target_number)
            return -1


guess_random_num(5, 0, 10)

print("\n")


def guess_random_num_linear(tries, start, stop):
    target_number = random.randint(start, stop)
    print("The number for the program to guess is:", target_number)
    # while tries != 0:
    for num in range(start, stop + 1):
        print("Number of tries left:", tries)
        print("The program is guessing: ", num)
        if num == target_number:
            print("The program guessed the correct number!")
            return
        if tries == 1:
            print("The program has failed to guess the correct number.")
            return -1
        tries -= 1


guess_random_num_linear(5, 0, 10)

print("\n")


def guess_random_num_binary(tries, start, stop):
    target_number = random.randint(start, stop)
    print("Random number to find:", target_number)
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot
        if pivot_value == target_number:
            print("Found it!", target_number)
            return
        if pivot_value > target_number:
            print("Guess lower!")
            upper_bound = pivot - 1
        else:
            print("Guess higher!")
            lower_bound = pivot + 1
        if tries == 1:
            print("Your program failed to find the number.")
            return -1
        tries -= 1


guess_random_num_binary(5, 0, 100)
