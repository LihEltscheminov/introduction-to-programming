import time
import random

items = []


def print_pause(game_script):
    print(game_script)
    time.sleep(2)


def intro():
    print_pause("A terrible disease hit your village.")
    print_pause("You were the only one not contaminated by the plague.")
    print_pause("To help your friends and family, "
                "you need to get a unique Buma Flower from the Dark Forest ")
    print_pause("and take it to the Healing River to "
                "prepare the potion of cure.")


def dark_forest():
    collect_flower = input("Would you like to (1) collect the "
                           "Buma Flower or (2) return to your village?")
    if collect_flower == "1":
        print_pause("That's Amazing! You have collected "
                    "the most important ingredient for the potion.")
        items.append("Buma Flower")
        choose_path()
    elif collect_flower == "2":
        print_pause("You are afraid and run back to the village.")
        print_pause("Your family is suffering. Some friends have died.")
        print_pause("What would you like to do?")
        choose_onemore()
    else:
        print_pause("Sorry, this pathway is not available!")
        dark_forest()


def healing_river():
    if "Buma Flower" in items:
        print_pause("You have reached the river.")
        print_pause("Wooww! You have now all the "
                    "elements needed to prepare the medicine.")
        print_pause("You mix them and have in your hands the Healing Potion.")
        print_pause("You run back to the village and distribute the medicine.")
        print_pause("Congratulations, you have saved them all!")
        re_start()
    else:
        print_pause("Good Job, you have located the Healing River.")
        print_pause("But unfortunately you do not have the Buma Flower.")
        print_pause("What you would like to do?")
        choose_path()


def choose_path():
    cure_path = input("Enter 1 to go to the Dark Forest."
                      "Enter 2 to go to the Healing River.")
    if cure_path == "1":
        print_pause("You have reached the Dark Forest.")
        print_pause("The magic spirits have guided "
                    "you too the middle of the forest.")
        print_pause("There you can find a colossal tree.")
        print_pause("When you look up at the highest tree branch, "
                    "you can see the bright coming from a beautiful "
                    "flower.It is the Buma Flower")
        dark_forest()
    elif cure_path == "2":
        print_pause("Wow, you are approaching the Healing River.")
        print_pause("You are one step closer to accomplish your mission.")
        healing_river()
    else:
        print_pause("Unfortunately, this route is not available.")
        print_pause("What you would like to do?")
        choose_path()


def choose_onemore():
    choose_again = input("Would you like to (1) let them die "
                         "or (2) look for the medicine?")
    if choose_again == "1":
        print_pause("All the village popupation have died. End of the game.")
        re_start()
    elif choose_again == "2":
        print_pause(random.choice(["You are a true hero!", "Wise decision!",
                                   "Hurry, your family and friends "
                                   "need your help!",
                                   "Let's start this adventure!"]))
        choose_path()
    else:
        print_pause("Sorry, this pathway is not available!")
        choose_onemore()


def re_start():
    play_again = input("Would you like to play again? yes/no ")
    if play_again == "yes":
        start_game()
    elif play_again == "no":
        exit()
    else:
        print_pause("Unfortunately, this route is not available.")
        re_start()


def start_game():
    items.clear()
    intro()
    print_pause("Are you ready to start this adventure?")
    choose_path()


start_game()
