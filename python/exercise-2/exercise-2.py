import time
items = []

def print_delay (message_displayed):
    print(message_displayed)
    time.sleep(2)

def intro ():
    print_delay("You have just arrived at your new job!\n")
    print_delay("You are in the elevator.\n")

def first_floor():
    print_delay("You push the button for the first floor.\nAfter a few moments, you find yourself in the lobby.\n")
    if "ID card" in items:
        print_delay("The clerk greets you, but she has already given you your ID card.")
        print_delay("so there is nothing more to do here now.")
    else:
        print_delay("The clerk greets you and gives you your ID Card.")
        items.append("ID card")
    choose_floor_again()

def second_floor():
    print_delay("You push the button for the second floor.")
    print_delay("After a few moments, you find yourself in the human resources department.")
    if "Handbook" in items:
        print_delay("The HR folks are busy at their desks.")
        print_delay("There doesn't seem to be much to do here.")
    else:
        print_delay("The head of HR greets you.\n")
        if "ID card" in items:
            print_delay("He looks at your ID card and then gives you a copy of the employee handbook.")
            items.append("Handbook")
        else:
            print_delay("He has something for you.")
            print_delay("But says he can't give it to you until you go get your ID card.")
    print_delay("You head back to the elevator.")
    choose_floor_again()
    

def third_floor():
    print_delay("You push the button for the third floor.\nAfter a few moments, you find yourself in the engineering department.\n")
    print_delay("This is where you work!")
    if "ID card" in items:
        print_delay("You use your ID card to open the door.")
        print_delay("Your program manager greets you and tells you that you need to have a copy of the employee handbook in order to start work.")   
        if "Handbook" in items:
            print_delay("Fortunately, you got that from HR!\nCongratulatons!\nYou are ready to start your new job as vice president of engineering!")
        else:
            print_delay("They scowl when they see that you don't have it, and send you back to the elevator.")
    else:
        print_delay("Unfortunately, the door is locked and you can't get in.")
        print_delay("It looks like you need some kind of key card to open the door.")
        print_delay("You head back to the elevator.")
    choose_floor_again()

def choose_floor ():
    floor = input("Please enter the number for the floor you would like to visit: \n1. Lobby \n2. Human resources \n3. Engineering department\n")
    if floor == "1":
        first_floor()
    elif floor == "2":
        second_floor()
    elif floor == "3":
        third_floor()    
    else:
        print_delay ("Sorry, this floor does not exist!/n")
        choose_floor()

def choose_floor_again():
    print_delay("Where would you like to go next?\n")
    choose_floor()


def ride_elevator():
    while True:
        intro()
        choose_floor()
        choose_floor_again()


ride_elevator()