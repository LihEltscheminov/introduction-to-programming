import time

def print_pause(message_to_print):
        print(message_to_print)
        time.sleep(3)

def intro():
        print_pause("Hello! I am Bob, the Breakfast Bot.")
        print_pause("Today we have two breakfasts available.")
        print_pause("The first is waffles with strawberries and whipped cream.")    
        print_pause("The second is sweet potato pancakes with butter and syrup.")
 
def order_breakfast():
        intro()
        while True:

                while True: 

                        order = input("Please, place your order.\nWould you like waffles or pancakes? ").lower()
                        if "waffles" in order:
                                print_pause("Waffles it is!")
                                break
                        elif "pancakes" in order:
                                print_pause("Pancakes it is!")
                                break
                        else:
                                print_pause("Sorry, that's not on our menu.")
                        
                print_pause("Your order will be ready shortly.")
                        
                while True:

                        re_order = input("Would you like to place another order? Please say 'yes' or 'no'.").lower()
                        if "no" in re_order:
                                print_pause("OK, goodbye!")
                                break
                        elif "yes" in re_order:
                                print_pause("Very good, I'm happy to take another order.")
                                break
                        else:
                                print_pause("Sorry, I don't understand.")
                                
                if "no" in re_order:
                        break
                
order_breakfast()
