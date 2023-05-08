# Created by James Lee
# IT 140 Introduction to Scripting
# Module Six Milestone

if __name__ == '__main__':

    # A dictionary for the simplified text castle adventure game
    # The dictionary links a room to other rooms.
    rooms = {
        'Foyer':          {
                            'east': 'Study Hall',
                            'west': 'Armory',
                            'item': None
                          },
        'Study Hall':     {
                            'west': 'Foyer',
                            'north': 'Garden',
                            'item': 'Lockpick'
                          },
        'Armory':         {
                            'east': 'Foyer',
                            'south': 'Cellar',
                            'north': 'Dining Hall',
                            'item': 'Shield'
                          },
        'Cellar':         {
                            'north': 'Armory',
                            'item': 'Torch'
                          },
        'Dining Hall':    {
                            'east': 'Great Hall',
                            'south': 'Armory',
                            'item': 'Silver Key'
                          },
        'Great Hall':     {
                            'east': 'Garden',
                            'west': 'Dining Hall',
                            'north': 'Throne Room',
                            'item': 'Sword'
                          },
        'Garden':         {
                            'west': 'Great Hall',
                            'north': 'Alchemy Room',
                            'south': 'Study Hall',
                            'item': 'Step Ladder'
                          },
        'Alchemy Room':   {
                            'south': 'Garden',
                            'item': 'Health Potion'
                          },
        'Throne Room':    {
                            'south': 'Great Hall',
                            'item': None
                          },
    }

    # Intro message to the player
    print('\n------------------------Castle Text Adventure Game------------------------')
    print('It started off as another mundane day at the kingdom’s castle. \n'
          'However, that all changed when the giant evil python infiltrated the castle, \n'
          'took down all the knights and guards, and captured the king and queen as \n'
          'hostages in the Throne Room. You are the bravest and strongest villager \n'
          'from the nearby town, and you were chosen by the townsfolk to go to the castle \n'
          'to free the king and queen. You know that taking down the giant evil python \n'
          'won’t be an easy task. You arrive at the castle’s gate, and without hesitation, \n'
          'you rush inside the castle.')
    print()
    print('In order to successfully defeat the giant evil python, you must explore \n'
          'every nook and cranny of the castle and collect all 7 items located \n'
          "throughout the castle. However, you soon realize that collecting all items isn't \n"
          'as easy as it sounds--each item you obtain is a puzzle piece that opens up inner \n'
          'reaches of the castle... ')
    print()
    print('HOW TO WIN: Collect 7 items before facing the giant evil python, or else be eaten by the python. \n'
          "Move commands: 'go South', 'go North', 'go East', 'go West', 'exit' \n"
          "Add to Inventory: get 'item name' \n"
          "Type 'Exit' at any time to exit the game.")
    print('--------------------------------------------------------------------------')

    # Initialize the game
    current_room = 'Foyer'  # Starting room
    inventory = []  # Starting inventory is an empty list
    item_used = []   # list for item(s) used. Affect prompt messages

    # Define function prompt_message
    def prompt_message(room):
        destination = None
        print('You are in the {}.'.format(room))
        print('Inventory:', inventory)

        # Print item messages depending on room and what items are in the inventory:
        # ----------------Foyer----------------
        if room == 'Foyer':
            print('It is cold and dark in here. \n'
                  'There is a dimly lit hallway to the east and to the west from here.')

        # ----------------Study Hall----------------
        elif room == 'Study Hall':
            # First if statement in Study Hall checks if the Lockpick is in the inventory.
            if 'Lockpick' in inventory:
                print('In the corner you see a desk and a flickering candle.')
            else:   # If the player has not obtained a lockpick:
                print('In the corner you see a desk with a dimly lit candle. \n'
                      'You see a Lockpick on the desk. ')
            # Second if statement in Study Hall checks if Torch is in inventory.
            if 'Torch' in inventory:
                print('The hallway to the west leads back to the Foyer. \n'
                      'The hallway to the north is pitch black, but you are able to see the path using the Torch.')
            else:
                print('The hallway to the west leads back to the Foyer. \n'
                      'The hallway to the north is pitch black. It is impossible to see where you are going.')

        # ----------------Armory----------------
        elif room == 'Armory':
            # First if statement checks if player has Shield in the inventory.
            if 'Shield' in inventory:
                print('There are destroyed armors and shields strewn all over the floor. \n'
                      'This must be the doings of the giant evil python...')
            else:
                print('There are destroyed armors and shields strewn all over the floor. \n'
                      'This must be the doings of the giant evil python... \n'
                      'In the corner of the room, you see an undisturbed Shield displayed on the wall.')
            # Second if statement checks if the player has Torch in the inventory.
            if 'Torch' in inventory:
                print('The hallway to the north is pitch black, but you are able to see the path using the Torch.')
            else:
                print('The hallway to the north is pitch black. It is impossible to see where you are going.')
            # Third if statement checks if the player has Lockpick in the inventory.
            if ('Lockpick' in inventory) and ('Lockpick' not in item_used) :
                print('There is a wooden door on the south wall. \n'
                      'You walk up to it and try to open it, but it is locked. \n'
                      'You use the Lockpick to open the locked door.')
                item_used[len(item_used):] = ['Lockpick']
            elif ('Lockpick' in inventory) and ('Lockpick' in item_used) :
                print('There is a wooden door on the south wall. \n'
                      'You already opened the locked door using the Lockpick.')
            else:
                print('There is a wooden door on the south wall. \n'
                      'You walk up to it and try to open it, but it is locked. \n'
                      'If only you had something to unlock this door...')

        # ----------------Cellar----------------
        elif room == 'Cellar':
            # if statement checks if the Torch is in the inventory.
            if 'Torch' in inventory:
                print('You are in the cellar. It is cold, damp, and empty. There is a door to the north.')
            else:
                print('You are in the cellar. It is cold and damp. There is a brightly lit Torch on the wall.\n'
                      'There is a door to the north.')

        # ----------------Dining Hall----------------
        elif room == 'Dining Hall':
            print('You are in the Dining Hall. There are cold half-eaten meals sitting on the banquet table. \n'
                  'There is a hallway to the east and to the south.')
            # if statement checks if Step Ladder is in the inventory
            if ('Step Ladder' in inventory) and ('Step Ladder' not in item_used):
                print('Your Torch illuminates the room, including the grand chandelier suspended above the table. \n'
                      'You notice a shiny object on the chandelier. Upon closer look, it looks to be a Silver Key.\n'
                      'The key is too high to reach. You use the Step Ladder to reach for the Silver Key.')
            elif ('Step Ladder' in inventory) and ('Step Ladder' in item_used):
                print('Your Torch illuminates the room, including the grand chandelier suspended above the table.')
            else:
                print('Your Torch illuminates the room, including the grand chandelier suspended above the table. \n'
                      'You notice a shiny object on the chandelier. Upon closer look, it looks to be a Silver Key.\n'
                      'The key is too high to reach on foot. If only you had something to help you reach up there...')

        # ----------------Garden----------------
        elif room == 'Garden':
            print('You are in the Garden. There is a hallway to the west and to the south.')
            # First if statement checks if Alchemy Room has been accessed:
            if 'Health Potion' not in inventory:
                  print('There looks to be a path to the north, but it is blocked by an overgrowth of vines.')
            else:
                print('There is a path leading to the Alchemy Room to the north.')
            # Second if statement checks for Sword in inventory
            if 'Sword' in inventory:
                print('You used the Sword to cut down the vines. The path is now accessible.')
            else:
                print('If only you had something to clear the vines blocking the path...')
            # Third if statement checks for Step Ladder in inventory
            if rooms['Garden']['item'] not in inventory:
                print('You see a Step Ladder in the corner of the Garden. Looks like it could be useful somewhere else.')

        # ----------------Alchemy Room----------------
        elif room == 'Alchemy Room':
            print('You are in the Alchemy Room. There are shelves full of mysterious books. \n'
                  'There is a path out of this room to the south.')
            # if statement to check for Health Potion in inventory
            if rooms['Alchemy Room']['item'] not in inventory:
                print('In the middle of the room, there is an alchemy table with a single Health Potion.')

        # ----------------Great Hall----------------
        elif room == 'Great Hall':
            print('You are in the Great Hall. It is cold and dark in here. A lot of damage was done to this place.\n'
                  'It is clear that a significant fight took place here. There is a hallway to the east and to the west.\n'
                  'There is a staircase to the north that looks to lead somewhere upstairs. \n'
                  'You hear a high-pitch hissing sound coming from there...')
            # First if statement checks for Sword in inventory
            if 'Sword' not in inventory:
                print('You see an undisturbed display case with a Sword inside. The display case is locked.')
            # Second if statement checks for Silver Key in inventory
            if ('Silver Key' in inventory) and ('Silver Key' not in item_used):
                print('You use the Silver Key to open the display case.')
            elif ('Silver Key' not in inventory):
                print('If only you had a key to unlock the display case...')

        move = input('Enter your move: ').lower()
        print('--------------------------------------')

        # Input command decision branch in Foyer:
        if room == 'Foyer':
            if move == 'go east':
                destination = rooms['Foyer']['east']
            elif move == 'go west':
                destination = rooms['Foyer']['west']
            elif move == 'exit':
                destination = 'Exit Room'
            else:
                print('Invalid command.')
                destination = 'Foyer'

        # Input command decision branch in Study Hall:
        elif room == 'Study Hall':
            if move == 'go north':
                if 'Torch' in inventory:
                    destination = rooms['Study Hall']['north']
                else:
                    print('You stumble down the pitch dark hallway. It is too dark to see anything. It leads you\n'
                          'back to the Foyer.')
                    destination = 'Foyer'
            elif move == 'go west':
                destination = rooms['Study Hall']['west']
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get lockpick':
                if 'Lockpick' in inventory:
                    print('Invalid command. Lockpick is already in the inventory!')
                    destination = 'Study Hall'
                else:
                    inventory[len(inventory):] = ['Lockpick']
                    print('Lockpick obtained!')
                    destination = 'Study Hall'
            else:
                print('Invalid command.')
                destination = 'Study Hall'

        # Input command decision branch in Armory:
        elif room == 'Armory':
            if move == 'go east':
                destination = rooms['Armory']['east']
            elif move == 'go south':
                if 'Lockpick' in inventory:
                    destination = rooms['Armory']['south']
                else:
                    print("Invalid command. You can't go that way!")
                    destination = 'Armory'
            elif move == 'go north':
                if 'Torch' in inventory:
                    destination = rooms['Armory']['north']
                else:
                    print('You stumble down the pitch dark hallway. It is too dark to see anything. It leads you\n'
                          'back to the Foyer.')
                    destination = 'Foyer'
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get shield':
                if 'Shield' in inventory:
                    print('Invalid command. Shield is already in the inventory!')
                    destination = 'Armory'
                else:
                    inventory[len(inventory):] = ['Shield']
                    print('Shield obtained!')
                    destination = 'Armory'
            else:
                print('Invalid command.')
                destination = 'Armory'

        # Input command decision branch in Cellar:
        elif room == 'Cellar':
            if move == 'go north':
                destination = rooms['Cellar']['north']
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get torch':
                if 'Torch' in inventory:
                    print('Invalid command. Torch is already in the inventory!')
                    destination = 'Cellar'
                else:
                    inventory[len(inventory):] = ['Torch']
                    print('Torch obtained!')
                    destination = 'Cellar'
            else:
                print('Invalid command.')
                destination = 'Cellar'

        # Input command decision branch in Dining Hall:
        elif room == 'Dining Hall':
            if move == 'go east':
                destination = rooms['Dining Hall']['east']
            elif move == 'go south':
                destination = rooms['Dining Hall']['south']
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get silver key':
                if 'Silver Key' in inventory:
                    print('Invalid command. Silver Key is already in the inventory!')
                    destination = 'Dining Hall'
                else:
                    if 'Step Ladder' in inventory:
                        inventory[len(inventory):] = ['Silver Key']
                        print('Silver Key obtained!')
                        item_used[len(item_used):] = ['Step Ladder']
                        destination = 'Dining Hall'
                    else:
                        print('Cannot obtain the Silver Key! It is too high to reach!')
                        destination = 'Dining Hall'
            else:
                print('Invalid command.')
                destination = 'Dining Hall'

        # Input command decision branch in Great Hall:
        elif room == 'Great Hall':
            if move == 'go east':
                destination = rooms['Great Hall']['east']
            elif move == 'go west':
                destination = rooms['Great Hall']['west']
            elif move == 'go north':
                destination = rooms['Great Hall']['north']
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get sword':
                if 'Sword' in inventory:
                    print('Invalid command. Sword is already in the inventory!')
                    destination = 'Great Hall'
                else:
                    if 'Silver Key' in inventory:
                        inventory[len(inventory):] = ['Sword']
                        print('Sword obtained!')
                        item_used[len(item_used):] = ['Silver Key']
                        destination = 'Great Hall'
                    else:
                        print('Cannot obtain the Sword. The display case is locked!')
                        destination = 'Great Hall'
            else:
                print('Invalid command.')
                destination = 'Great Hall'

        # Input command decision branch in Garden:
        elif room == 'Garden':
            if move == 'go north':
                if 'Sword' in inventory:
                    destination = rooms['Garden']['north']
                else:
                    print('Invalid command. The path is blocked by vines.')
                    destination = 'Garden'
            elif move == 'go west':
                destination = rooms['Garden']['west']
            elif move == 'go south':
                destination = rooms['Garden']['south']
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get step ladder':
                if 'Step Ladder' in inventory:
                    print('Invalid command. Step Ladder is already in the inventory!')
                    destination = 'Garden'
                else:
                    inventory[len(inventory):] = ['Step Ladder']
                    print('Step Ladder obtained!')
                    destination = 'Garden'
            else:
                print('Invalid command.')
                destination = 'Garden'

        # Input command decision branch in Alchemy Room:
        elif room == 'Alchemy Room':
            if move == 'go south':
                destination = rooms['Alchemy Room']['south']
            elif move == 'exit':
                destination = 'Exit Room'
            elif move == 'get health potion':
                if 'Health Potion' in inventory:
                    print('Invalid command. Health potion is already in the inventory!')
                    destination = 'Alchemy Room'
                else:
                    inventory[len(inventory):] = ['Health Potion']
                    print('Health Potion obtained!')
                    destination = 'Alchemy Room'
            else:
                print('Invalid command.')
                destination = 'Alchemy Room'

        # Input command decision branch in Throne Room:
        elif room == 'Throne Room':
            if move == 'go south':
                destination = rooms['Throne Room']['south']
            else:
                print('Invalid command.')
                destination = 'Throne Room'

        return destination


    while (current_room != 'Throne Room') and (current_room != 'Exit Room'):
        new_room = prompt_message(current_room)
        current_room = new_room
        while current_room == 'Exit Room':
            print('You underestimated the trials of this adventure and it has taken \n'
                  'a significant physical and emotional toll on you. You decide to exit \n'
                  'the castle for now. You must steel your body and mind and return to \n'
                  'the castle, as the fate of the king and the queen, as well as the \n'
                  'kingdom rests upon your shoulders. \n')
            exit_game = input("Type 'exit' to exit the program, or type 'try again' to start over from the beginning: ").lower()
            if exit_game == 'exit':
                break
            elif exit_game == 'try again':
                current_room = 'Foyer'
                inventory = []
                item_used = []
                print('--------------------------------------')
                break
        while current_room == 'Throne Room':
            print('You are in the Throne Room. \n'
                  'The giant evil python was about to eat the king and queen, until it sees you. \n'
                  'You come face to face with the giant evil python.')

            if 'Shield' not in inventory:
                print(
                    'The python hisses, and swiftly strikes! You are unable to block its bite, and it swallows you whole.\n'
                    'You failed to save the king and the queen. \n'
                    'Thanks for playing, hope you had fun. Try again!')

            elif ('Sword' not in inventory) and ('Shield' in inventory):
                print('The python hisses, and swiftly strikes! You blocked its attack with the Shield. \n'
                      'However, you are unable to do any damages to the python without a weapon. \n'
                      'Eventually, the python strikes and lands, and it swallows you whole. \n'
                      'You failed to save the king and the queen. \n'
                      'Thanks for playing, hope you had fun. Try again!')

            elif (('Sword' and 'Shield') in inventory) and ('Health Potion' not in inventory):
                print('The python hisses, and swiftly strikes! You blocked its attack with the Shield. \n'
                      "You strike back at the python with the Sword! It's a hit! \n"
                      "The python strikes again, but you block again with the Shield. But the python's fang grazes and tears your flesh! \n"
                      'You start to feel weak, and you fall to your knees. You slowly lose consciousness. The python swallows you whole. \n'
                      'You failed to save the king and the queen. \n'
                      'Thanks for playing, hope you had fun. Try again!')

            elif ('Sword' and 'Shield' and 'Health Potion') in inventory:
                print('The python hisses, and swiftly strikes! You blocked its attack with the Shield. \n'
                      "You strike back at the python with the Sword! It's a hit! \n"
                      "The python strikes again, but you block again with the Shield. But the python's fang grazes and tears your flesh! \n"
                      'You start to feel weak, and you fall to your knees. You quickly take out the Health Potion and drink it. \n'
                      'You start to feel stronger immediately. You rise to your feet, and you charge at the python with all of your might. \n'
                      'You land a fatal blow to the python. The python shrieks and collapses. You have slayed the giant evil python! \n'
                      'You saved the king and the queen, as well as the kingdom! All of the kingdom celebrates your bravery and courage! \n'
                      'Thanks for playing the game. Hope you had fun!')

            exit_game = input(
                "Type 'exit' to exit the program, or type 'try again' to start over from the beginning: ").lower()
            if exit_game == 'exit':
                break
            elif exit_game == 'try again':
                current_room = 'Foyer'
                inventory = []
                item_used = []
                print('--------------------------------------')
                break

