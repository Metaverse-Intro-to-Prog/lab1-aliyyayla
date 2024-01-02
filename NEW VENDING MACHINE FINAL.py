#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:33:54 2023

@author: aliyya
"""

main_menu = ["Drinks", "Chips"]
drinks_dict = {
    1:{'name': 'Our Summer Orange Juice', 'price': 2},
    2:{'name': 'Magic Island Green Drink', 'price': 1.50},
    3:{'name': 'Frost Ice Water', 'price': 1.50},
    4:{'name': 'Blue Hour Energy Drink', 'price': 2.50},
    5:{'name': 'Eternally Purple Drink', 'price': 2}
    }
chips_dict = {
    1:{'name': 'Poppin Star Candy', 'price': 3.50},
    2:{'name': '9 and 3 Quarters Chocolate Bar', 'price': 3.50},
    3:{'name': 'Crown Waffles', 'price': 3.50},
    4:{'name': 'Blue Orangade Ice Cream', 'price': 3.50},
    5:{'name': 'Anti-Romantic Sliced Cake', 'price': 3.50}
    }
addons_dict = {
    1:{'name': 'Dear Sputnik Energy Drink', 'price': 4.0},
    2:{'name': 'MOA Diary Special Combo', 'price': 5.0},
    3:{'name': 'Happily Ever After Donuts', 'price': 3.0},
    4:{'name': 'Hydrangea Muffins', 'price': 3.0},
    5:{'name': 'Love Sight Sparkling Water', 'price': 3.0},
    6:{'name': 'is', 'price': 5.0}
    }
total = 0

def main_menu_func():
    print(main_menu)
    x = str(input("\n\nCHOOSE THE CATEGORY YOU WANT PLEAJEU. Type GOODBYE NOW to finish.\n\n"))
    if x == 'Drinks': #using the if condition when the consumer chose drinks
        drinks_func()
    elif x == 'Chips': #using the if condition when the consumer chose chips
        chips_func()
    else:
        print("\n\n... ✿°•∘ɷ∘•°✿ ..MANSEEE !!! NOW YOU CAN PICK UP YOUR ITEMS. DON'T FORGET YOUR CHANGEU JUSEYOO !... ✿°•∘ɷ∘•°✿ ..\n")
        change_func() #will print the receipt once the purchase is done

def another_drink():
    x = input("\n\nWOULD YOU CARE FOR ANOTHER DRINKEU ? Type NEW RULES or NO RULES:\n")
    if x == 'NEW RULES': #using the if condition to ask the buyer for another purchase 
        drinks_func()
    else:
        main_menu_func() #will return to main menu

def another_chips():
    x = input("\n\nWOULD YOU LIKE TO GET ANOTHER CHIPSEU ? Type NEW RULES or NO RULES:\n")
    if x == 'NEW RULES': #using the if condition to ask the buyer for another purchase 
        chips_func()
    else:
        main_menu_func() #will return to main menu

def add_ons_func():
    global total
    print(addons_dict)
    print("\n\nTYPE IN THE ADDEU-ON YOU WANT :3. KEUROJIMAN,IF YOU ANIYEYO ADDEU-ON, type GOODBYE NOW.\n") 
    addon_input = input()  #Reading this input as a string
    if addon_input.upper() == 'GOODBYE NOW':  #using uppercase method to compare as string
        main_menu_func()
    else:
        addon_id = int(addon_input)  #this is to convert to an integer, if not 'GOODBYE NOW'
        if addon_id in addons_dict:
            addon_cost = addons_dict[addon_id]['price']
            total += addon_cost
            main_menu_func()
        else:
            print("\n\nOMO ! ENTER A VALID ADD-ON JUSEYOOO.\n")
            add_ons_func()

def drinks_func():
    global total
    print(drinks_dict)
    print("\n\nPLEAJEU TYPE IN THE DRINKEU YOU WANT :>. IF YOU ANIYEYO A DRINK, type GOODBYE NOW:\n") 
    drink_input = input()  #Reading this input as a string
    if drink_input.upper() == 'GOODBYE NOW':  #using uppercase method to compare as string
        main_menu_func()
    else:
        drink_id = int(drink_input)  #this is to convert to an integer, if not 'GOODBYE NOW'
        if drink_id in drinks_dict:
            drink_cost = drinks_dict[drink_id]['price']
            total += drink_cost
            add_ons_func()
        else:
            print("\n\nOMO ! PLEAJEU ENTER A VALID DRINKEU.\n\n")
            drinks_func()
            
def chips_func():
    global total
    print(chips_dict)
    print("\n\nPLEAJEU TYPE IN THE CHIPSEU YOU WANT :> :\n") #using the integer to print the item id for chips
    chips_id = int(input()) #using the integer to print the item id for chips
    if chips_id in chips_dict:
        chips_cost = chips_dict[chips_id] ['price']
        total += chips_cost #using the assignment orperator to total the cost of the chips
        add_ons_func()
    else:
        print("\n\nOMO ! ENTER A VALID CHIPS OPTION JUSEYOOO.\n\n")
        chips_func() #the loop will continue to print unless the input is correct.

def change_func():
    global total
    print("\n\n°.✩┈┈∘*┈🌙┈*∘┈┈✩.°KAMSAMI FOR BUYING OUR NEVERLAND COLLECTION !!!!!°.✩┈┈∘*┈🌙┈*∘┈┈✩.°.")
    change = coins - total #using the arithmetic operators to subtract the total to the coins for the change
    print("\nYOU PAID", coins, "WITH", str(total), ". AND YOUR CHANGE WILL BE:", change)

print('·̇·̣̇̇·̣̣̇·̣̇̇·̇ •❣•୨୧┈┈┈୨୧•❣• ·̇·̣̇̇·̣̣̇·̣̇̇·̇WELCOME TO NEVERLAND. TASTE THE SWEET MIRAGE OF OUR VENDING MACHINE·̇·̣̇̇·̣̣̇·̣̇̇·̇ •❣•୨୧┈┈┈୨୧•❣• ·̇·̣̇̇·̣̣̇·̣̇̇·̇. \n\n̶̶̶̶  «̶ ̶̶̶ ̶ «̶ ̶̶̶ 　THE MAXIMUM NUMBER OF COINS YOU CAN ENTER IS 15. BUTAKHAMNIDA.　　　 ̶ ̶ ̶»̶ ̶̶̶ ̶ »̶ ̶̶̶  ')
coins = float(input('\nPleajeu enter your coins down here:\n '))

coin_type = str(input('\n\nCheogiyeo ! Are your coins WONs ? Pleajeu type NEW RULES or NO RULES:\n'))
if coin_type == "NEW RULES": #while true to continue with the next print
    print("\n•┈••✦ ❤ ✦••┈•YOU HAVE ENTERED", str(coins), "WON. SELECT THE CATEGORY YOU LIKE JUSEYOO•┈••✦ ❤ ✦••┈•\n")
    print(main_menu)
    print("\n\nTYPE THE TEMPTING CATEGORY YOU WANT JUSEYOOO:\n")
    category_selection = str(input()) #to choose between drinks and chips in main menu 
    if category_selection == 'Drinks':
        drinks_func()
    elif category_selection == 'Chips':
        chips_func() #using the if-elif condition for the main menu 
    else:
        print("OMO ! try again.") #the loop will break once there is an error in the input
else:
    print('\nAigooo.... mianhada but we only accepteu WONs. BUTAKAMNIDA !') #the loop will break once there is an error in the input