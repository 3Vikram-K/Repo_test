import random

while True:
    random_num = random.randint(1, 100)
    guess_num = 0
    count = 0
    while not guess_num == random_num:
        guess_num = int(input("Guess a number between 1 and 100 : "))
        if not guess_num == random_num:
            print("\nWrong guess")

        if guess_num > random_num:
            difference = guess_num - random_num
            if difference < 10:
                print("Higher,but almost near.")
            elif (difference > 10) and (difference < 20):
                print("High.")
            else:
                print("Too High.")
        elif random_num > guess_num:
            difference = random_num - guess_num
            if difference < 10:
                print("Lower,but almost near.")
            elif (difference > 10) and (difference < 20):
                print("Low.")
            else:
                print("Too Low.")
        count = count + 1
    print("Well done. You guessed the number right.")
    print(f"You took {count} turns.")
    Invalid = True
    while Invalid:
        Invalid = False
        print("1.Replay the game.\t2.Exit the game.")
        opt = input("Enter your choice : ")
        if opt == "1":
            continue
        elif opt == "2":
            exit(0)
        else:
            Invalid = True
            print("Invalid Choice.Try again.")
