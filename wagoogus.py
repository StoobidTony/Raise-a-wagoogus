import random as rand
import time as t
import json
import math
import sys

def dialogue(text, name=None, sleeptime=1):
    if name != None:
        print(f"{name}: {text}")
        t.sleep(sleeptime)
    else:
        print(text)
        t.sleep(sleeptime)

def main():
    six_wagoogs_plus_deco = "=+- "+("wagoogus "*6)+"=+-"

    # wagoogus info
    # # wagoogus stats
    hp = 100
    energy = 100
    joy = 100
    hunger = 100
    # # inv
    googus_inv = []

    # player info
    username = input("Enter your username. - ")
    # # player stats
    money = 10
    # # inv
    player_inv = ['redbull', 'old skateboard'] # inv means inventory, numbnuts

    # other
    hour = 9
    minute = 0
    time = f"{hour}:{minute}"
    day = 1
    item_details = json.load(open(f"wagoojson/items.json"))

    def notate_time(notated_hour, notated_minute):
        nonlocal time
        if hour >= 10 and minute >= 10:
            time = f"{hour}:{minute}"
        elif hour < 10 and minute >= 10:
            time = f"0{hour}:{minute}"
        elif hour >= 10 and minute < 10:
            time = f"{hour}:0{minute}"
        elif hour < 10 and minute < 10:
            time = f"0{hour}:0{minute}"

    def cap_stats():
        nonlocal hp
        nonlocal energy
        nonlocal hunger
        nonlocal joy
        if hp > 100:
            hp = 100
        if energy > 100:
            energy = 100
        if hunger > 100:
            hunger = 100
        if joy > 100:
            joy = 100
        if hp < 0:
            hp = 0
        if energy < 0:
            energy = 0
        if hunger < 0:
            hunger = 0
        if joy < 0:
            joy = 0

    def stagoogusts(): # show wagoogus stats
        nonlocal hp
        nonlocal hunger
        nonlocal energy
        nonlocal joy
        print(f"WAGOOGUS STATS:")
        print(f"- HEALTH   : {hp}")
        print(f"- HUNGER   : {hunger}")
        print(f"- ENERGY   : {energy}")
        print(f"- HAPPINESS: {joy}")

    def check_balance():
        nonlocal money
        print(f"BALANCE: {money}W$")

    def random_event():
        nonlocal hp
        nonlocal money
        fun_value = rand.randint(1, 4)
        match fun_value:
            case 1:
                # the wagoogus finds money
                print(f"The wagoogus found some money.")
                wagoogus_money_found = rand.randint(10, 50)
                print(f"You got {wagoogus_money_found}W$.")
                money += wagoogus_money_found
            case 2:
                # the wagoogus accidentally injures herself
                print("The wagoogus accidentally injured itself by doing something stupid.")
                wagoogus_accident_damage = rand.randint(5, 26)
                print(f"The wagoogus took {wagoogus_accident_damage} damage.")
                hp -= wagoogus_accident_damage
            case 3:
                # the wagoogus finds treasure
                # choose a random treasure. Each with specific set chances / weight.
                treasure_num = rand.randint(1, 100)
                if treasure_num <= 25: # 25%
                    treasure = "money"
                elif treasure_num <= 60: # 35%
                    treasure = "googus food"
                elif treasure_num <= 65: # 5%
                    treasure = "googus luxury food"
                elif treasure_num <= 75: # 10%
                    treasure = "redbull"
                elif treasure_num <= 80: # 5%
                    treasure = "cabinet"
                elif treasure_num <= 85: # 5%
                    treasure = "telephone"
                elif treasure_num <= 90: # 5%
                    treasure = "skateboard"
                elif treasure_num <= 95: # 5%
                    treasure = "DVDs"
                elif treasure_num <= 99: # 5%
                    treasure = "gun"
                elif treasure_num <= 100: # 1% 
                    treasure = "boardskate"
                # check what type of treasure it is, for wording.
                if treasure not in ['skateboard', 'boardskate', 'gun', 'telephone', 'cabinet', 'money']:
                    print(f"The wagoogus found some {treasure}.")
                    print(f"{treasure.capitalize()} was added to your inventory")
                    player_inv.append(treasure)
                elif treasure != 'money':
                    print(f"The wagoogus found a {treasure}.")
                    print(f"{treasure.capitalize()} was added to your inventory")
                    player_inv.append(treasure)
                else:
                    print(f"The wagoogus found some money.")
                    wagoogus_money_found = rand.randint(10, 50)
                    print(f"You got {wagoogus_money_found}W$.")
                    money += wagoogus_money_found



    def text_sep(char, amount=len(six_wagoogs_plus_deco), endchar="\n"): # text seperator func
        print(amount * char, end=endchar)

    def open_inv(): # open the player's inventory
        # Log the items in case of duplicates
        print(f"--------- INVENTORY ---------")
        nonlocal player_inv
        logged_inv = []
        for item in player_inv:
            if not item in logged_inv:
                print(f"{item} | {player_inv.count(item)}x")
                logged_inv.append(item)
        # Actually display the inventory

    def open_shop(): # opens the wagoogastore
        nonlocal item_details
        nonlocal money
        nonlocal player_inv
        shop_stock = []
        print(f"Welcome to Wagoogamarket!")
        text_sep('-', 30)
        print(f"YOUR BALANCE: {money}W$")
        text_sep('-', 30)
        for key in item_details:
            print(f"{key:<{len('googus luxury food')}} | {item_details[key]['price']}W$")
            shop_stock.append(key.lower())
        text_sep('-', 30)
        shop_action = input("What are you gonna do? (Buy / Sell / Leave) - ")
        while shop_action.lower() not in ['buy', 'sell', 'leave']:
            print("Invalid action. ")
            shop_action = input("What are you gonna do? (Buy / Sell / Leave) - ")
        while shop_action.lower() != "leave":
            if shop_action.lower() == "buy":
                print(shop_stock) # DEV
                buy_choice = input("What item would you like to buy? (nvm to exit) - ")
                if buy_choice.lower() != "nvm":
                    while buy_choice.lower() not in shop_stock:
                        print("Invalid choice.")
                        buy_choice = input("What item would you like to buy? - ")
                    if money >= item_details[buy_choice.capitalize()]['price']:
                        print(f"You have bought {buy_choice.capitalize()}.")
                        money -= item_details[buy_choice.capitalize()]['price']
                        player_inv.append(buy_choice)
                    else:
                        print("Insufficient funds! ")
                        shop_action = input("What do you wanna do? (Buy / Sell / Leave) - ")
                else:
                    print(f"You have decided to not buy anything.")
                    break
            elif shop_action.lower() == 'sell':
                open_inv()
                sell_choice = input("Which item would you like to sell? - ")
                while sell_choice not in player_inv:
                    print("You cannot sell or do not have that item.")
                    sell_choice = input("Which item would you like to sell? - ")
                areyousureaboutsellingthatitemomnimanreferenceomigosh = input("areyousure? (y/n) - ")
                while areyousureaboutsellingthatitemomnimanreferenceomigosh.lower() not in ['n', 'y']:
                    print("Invalid choice. ")
                    areyousureaboutsellingthatitemomnimanreferenceomigosh = input("areyousure? (y/n) - ")
                if areyousureaboutsellingthatitemomnimanreferenceomigosh.lower() == 'y':
                    money += math.floor((item_details[sell_choice.capitalize()]['price'] * 0.75))
                    print(f"You sold {sell_choice.capitalize()}. You have gained {math.floor(item_details[sell_choice.capitalize()]['price'] * 0.75)}W$")
                    player_inv.pop(player_inv.index(sell_choice))
                    text_sep('-', 30)
                    shop_action = input("What are you gonna do? (Buy / Sell / Leave) - ")
                elif areyousureaboutsellingthatitemomnimanreferenceomigosh.lower() == 'n':
                    print(f"You have chosen not to sell {sell_choice}.")

    def gib_goog_presnet(presnet):
        nonlocal joy
        nonlocal hp
        nonlocal player_inv
        nonlocal googus_inv

        possible_presnets = ['old skateboard', 'skateboard', 'boardskate', 'cabinet', 'telephone', 'dvds', 'gun', 'nvm']
        while presnet.lower() not in possible_presnets:
            print("You cannot gift that to the wagoogus.")
            break
        if presnet.lower() not in googus_inv:
            match presnet.lower():
                case 'old skateboard':
                    print("wagoogus: hell yeah")
                    googus_inv.append('old skatebaord')
                    player_inv.pop(player_inv.index('old skateboard'))
                    joy += 10
                    hp -= 5
                    print("The wagoogus became happier but failed a trick.")
                case 'skateboard':
                    print("wagoogus: hell yeah")
                    googus_inv.append('skateboard')
                    player_inv.pop(player_inv.index('skateboard'))
                    joy += 25
                    print("The wagoogus' joy increased!")
                case 'boardskate':
                    print("The wagoogus tried munching on the boardskate")
                    googus_inv.append('boardskate')
                    player_inv.pop(player_inv.index('boardskate'))
                    joy += 8
                case 'cabinet':
                    print("The wagoogus dismantled the cabinet into a pile of wood scraps.")
                    googus_inv.append('wood scraps')
                    player_inv.pop(player_inv.index('cabinet'))
                    joy += 5
                case 'telephone':
                    print("The wagoogus reluctantly accepted the telephone, then realized she can call with her friends.")
                    googus_inv.append('telephone')
                    player_inv.pop(player_inv.index('telephone'))
                    joy += 15
                case 'dvds':
                    print("The wagoogus got a dvd set. And immediately started binging it for hours on end.")
                    googus_inv.append('dvds')
                    player_inv.pop(player_inv.index('dvds'))
                    joy += 25
                case 'gun':
                    print("The wagoogus inspected the gun thoroughly.")
                    print("The wagoogus dismantled the gun.")
                    print("The wagoogus took it to the gun range.")
                    googus_inv.append('gun')
                    player_inv.pop(player_inv.index('gun'))
                    joy += 30
                case 'nvm':
                    print("You have chosen not to gift the wagoogus anything.")

    def gib_goog_foob(foob):
            nonlocal joy
            nonlocal hp
            nonlocal energy
            nonlocal player_inv
            nonlocal hunger

            possible_foobs = ['googus food', 'googus luxury food', 'redbull']
            while foob.lower() not in possible_foobs:
                print("You cannot feed that to the wagoogus.")
                break
            match foob.lower():
                case 'googus food':
                    print("The wagoogus enjoyed the googus food.")
                    player_inv.pop(player_inv.index('googus food'))
                    joy += 5
                    energy += 10
                    hp += 10
                    hunger += 10
                case 'googus luxury food':
                    print("The wagoogus thoroughly enjoyed the luxury googus food!")
                    player_inv.pop(player_inv.index('googus luxury food'))
                    joy += 10
                    energy += 15
                    hp += 20
                    hunger += 15
                case 'redbull':
                    print("The wagoogus has been caffeinated.")
                    player_inv.pop(player_inv.index('redbull'))
                    joy += 15
                    energy += 25
                    hunger += 5
                    
    def advance_time(advanced_hours=0, advanced_minutes=15):
        nonlocal hour
        nonlocal minute
        nonlocal time
        minute += advanced_minutes
        if minute >= 60:
            hour += 1
            minute -= 60
        hour += advanced_hours
        if hour >= 24:
            hour -= 24

    def check_for_neglection():
        nonlocal joy
        nonlocal energy
        nonlocal hunger
        nonlocal hp

        if hp <= 10 and energy <= 10 and hunger <= 10 and hp <= 10:
            dialogue("How dare you...", "Wagoogus", 2.5)
            dialogue("Why did you neglect me?", "Wagoogus", 3)
            dialogue("The wagoogus believes she can take better care of a wagoogus than you can.", None, 3)
            dialogue("Then you felt yourself changing...", None, 3)
            dialogue("And the wagoogus started changing too...", None, 3)
            dialogue("Then you realize...", None, 3)
            dialogue("Your roles have been swapped.", None, 5)
            sys.exit() # END OF GAME

    def starve():
        nonlocal hunger
        nonlocal hp

        if hunger == 0:
            hp -= 25
        elif hunger <= 10:
            hp -= 20
        elif hunger <= 20:
            hp -= 15
        elif hunger <= 30:
            hp -= 10
        elif hunger <= 40:
            hp -= 5

    # THIS IS WHERE THE GAME ACTUALLY STARTS
    text_sep('=')
    print(six_wagoogs_plus_deco)
    text_sep('=')
    dialogue("You have obtained a wagoogus. Take care of her well, or else.")
    text_sep('=')
    print(f"(Yes, this was made with permission and consulting from the\none and only Wagoogus Jr. Props to her.)")
    text_sep("-")
    print("(All brand and song names mentioned that aren't by the \ncreator, StoobidTony, are NOT affiliated to this project \n(why am I saying this? idk))")
    text_sep('=')
    stagoogusts()
    text_sep('=')
    check_balance()
    text_sep('=')

    # ACTIONS
    player_action = input(f"What would you like to do? (Googus / Shop / Ignore / {username} / Quit) - ")
    text_sep('-', 29)
    while player_action.lower() != "quit":
        if player_action.lower() == "googus":
            googus_action = input("What would you like to do with the googus? (Feed / Give present / View stats / Nvm) - ")
            text_sep('-', 29)
            while googus_action.lower() not in ['feed', 'give present', 'view stats', 'nvm']:
                print("Invalid action.")
                text_sep('-', 29)
                googus_action = input("What would you like to do with the googus? (Feed / Give present / View stats / Nvm) - ")
                text_sep('-', 29)
                cap_stats()
            while googus_action.lower() != 'nvm':
                if googus_action == 'feed':
                    open_inv()
                    text_sep('-', 29)
                    chosen_foob = input("What would you like to give the googus? (nvm to go with nothing) - ")
                    if chosen_foob.lower() == 'nvm':
                        print("You have decided to not give the wagoogus anything.")
                    else:
                        gib_goog_foob(chosen_foob.lower()) 
                    text_sep('-', 29)
                    if rand.randint(1, 4) == 1:
                        random_event()
                        text_sep('-', 29)
                    cap_stats()
                    check_for_neglection()
                    starve()
                    advance_time()
                    notate_time(hour, minute)
                    print(f"TIME: {time}")
                elif googus_action == 'give present':
                    open_inv()
                    text_sep('-', 29)
                    chosen_presnet = input("What would you like to give the googus? (nvm to go with nothing) - ")
                    while chosen_presnet.lower() not in player_inv and chosen_presnet.lower() != 'nvm':
                        print("Invalid choice. ")
                        chosen_presnet = input("What would you like to give the googus? (nvm to go with nothing) - ")
                    if chosen_presnet.lower() == 'nvm':
                        print("You have decided to not give the wagoogus anything.")
                    else:
                        gib_goog_presnet(chosen_presnet.lower())
                    text_sep('-', 29)
                    if rand.randint(1, 4) == 1:
                        random_event()
                    cap_stats()
                    check_for_neglection()
                    starve()
                    advance_time()
                    notate_time(hour, minute)
                    print(f"TIME: {time}")
                elif googus_action == 'view stats':
                    text_sep('=')
                    stagoogusts()
                    text_sep('=')
                    cap_stats()
                googus_action = input("What would you like to do with the googus? (Feed / Give present / View stats / Nvm) - ")
                text_sep('-', 29)
                cap_stats()
        elif player_action.lower() == "shop":
            open_shop()
            text_sep('-', 29)
            if rand.randint(1, 4) == 1:
                random_event()
            cap_stats()
            check_for_neglection()
            starve()
            advance_time()
            notate_time(hour, minute)
            print(f"TIME: {time}")
        elif player_action.lower() == "ignore":
            print(f"You have ignored the wagoogus.")
            # insert time change 15 min
            if rand.randint(1, 4) == 1: # 25% chance to trigger a random event.
                random_event()
            else:
                energy -= 10
                joy -= 10
                hunger -= 5
                print(f"The wagoogus' stats decreased.")
            text_sep('-', 29)
            cap_stats()
            check_for_neglection()
            starve()
            advance_time()
            notate_time(hour, minute)
            print(f"TIME: {time}")
        elif player_action.lower() == username.lower():
            check_balance()
            open_inv()
            text_sep('-', 29)
            cap_stats()
        else:
            print("Invalid action. ")
            text_sep('-', 29)
            cap_stats()
        player_action = input(f"What would you like to do? (Googus / Shop / Ignore / {username} / Quit) - ")
        text_sep('-', 29)
        cap_stats()

if __name__ == "__main__":
    main()