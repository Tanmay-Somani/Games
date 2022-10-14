from random import randint
choice = ' '
user_pt = 0
cmp_pt = 0
while True:
    choice = input("Do you wish to play[Y/N]").upper()
    if choice == "N":
        print("Exiting the program")
        break
    elif choice == "Y":
        print("Starting the game................................................................")
        while True:
            user_choice = int(
                input("Enter your choice[ 1 -Rock | 2 - Paper | 3 - Scissor ]"))
            if user_choice == 1:
                print("You have chosen Rock")
                break
            elif user_choice == 2:
                print("You have chosen Paper")
                break
            elif user_choice == 3:
                print("You have chosen Scissor")
                break
            else:
                print("Incorrect choice please choose again")

        choice_dips = randint(1, 3)
        if choice_dips == 1:
            print("Computer chose Rock")
        elif choice_dips == 2:
            print("The computer chose Paper")
        else:
            print("The computer chose Scissors")

        if choice_dips == user_choice:
            # this removes three iterations
            print("The same choice was taken,Its a Tie")
        elif choice_dips != user_choice:  # if its anything else than that
            if user_choice < choice_dips:
                if (choice_dips-user_choice == 2):
                    print("USER WON")
                    user_pt += 1
                elif (choice_dips-user_choice == -2):  # let u_c be 3(S) and c_d be 1(R)
                    print("COMPUTER WON")
                    cmp_pt += 1
                else:
                    print("COMPUTER WON")
                    cmp_pt += 1
            elif user_choice > choice_dips:
                if (user_choice-choice_dips == 2):
                    print("COMPUTER WON")
                    cmp_pt += 1
                elif (user_choice-choice_dips == -2):
                    print("USER WON")
                    user_pt += 1
                else:
                    print("USER WON")
                    user_pt += 1
        print("the current score is", user_pt, "\t", cmp_pt)
