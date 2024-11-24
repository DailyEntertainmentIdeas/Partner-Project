#Imports the random library for the guardian's attacks
import random
import time

def typewriter(text, delay=0.1):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(delay)
    print()

#Creates the player
class Player: 
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.attacks = {}
        self.healing_items = {}
    
    def perform_attack(self, attack_name):
        if attack_name:
            damage = self.attacks[attack_name]
            return damage
        else:
            print("\nThe attack you are looking for is not avaliable. ")
            return 0
    
    def heal(self, item_name):
        if item_name in self.healing_items:
            healing = self.healing_items[item_name]
            self.health += healing
            del self.healing_items[item_name]
            return healing
        else:
            print("\nInvalid healing item.")
            return 0


#Creates the enemy
class Enemy:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

#Asks user for their name
name = input("Enter your name: ").capitalize()

#Lets the character choose the class of character and their ability
while True:
    print("""\nWhat class of character would you like to choose?
1. Knight
2. King
3. Horse""")
    time.sleep(2)
    classofcharacter = int(input("\nEnter the number of the class you would like to have: "))
    if classofcharacter == 1:
        classofcharacter = "Knight"
        break
    elif classofcharacter == 2:
        classofcharacter = "King"
        break
    elif classofcharacter == 3:
        classofcharacter = "Horse"
        break
while True:
    print("""\n\nWhat ability would you like to have? 
1. Athletisism
2. Intelligence
3. Trickster""")
    time.sleep(2)
    abilities = int(input("\nEnter the number of the ability you would like to have: "))
    if abilities == 1:
        abilitiies = "athletisism"
        break
    elif abilities == 2:
        abilities = "intelligence"
        break
    elif abilities == 3:
        abilities = "trickster"
        break

#Sets up the characters abilities
player = Player(name = name)
enemy = Enemy(name = "Mara the Rival", health = 50)


#Gives the user an intro and information about each character
print(f"""

Welcome to the start of your adventure {name}! 

You are a {classofcharacter} with {abilities}. 

Your health is 100.

The main objective in this game is to find your brother in a post-apocalyptic adventure. 

Along the way in each location, you may find one item in each room.

Each time your inventory is greater than or equal to 3, you will have an option to remove any items from your inventory.""")

time.sleep(2)
intro = input("\nWould you like to get background on the characters of the game? Y/N: ").upper()

if intro == "Y":    
    print(f"""

The main character of the game is {name}. {name} is a {classofcharacter} who has 100 health, 75 strength, 25 stamina, 135 speed, and 40 attack power. 
S/he has a motivation to find his/her lost sibling and goes through numerous challenges and encounters Mara and the Guardian.""")
    print("""
Mara is a rival scavenger. She is a side character that has 50 health, 40 stength, 15 stamina, 75 speed, and 20 attack power. 
She used to be part of a community that fell apart but now is looking to seek power""")
    print("""
The Guardian is a mentor. He is a side character who has 100 health, 75 stength, 25 stamina, 135 speed, and 40 attack power. 
He was once a scholar but is now a mysterious person who has knowledge of the old world. """)
else:
    pass

#Puzzles
def riddle_puzzle():
    answer = "fire"
    while True:
        response = input("\n\nSolve the riddle to proceed: \n'I am not alive, but I grow, I don't have lungs, but I need air, what am I?':  ").lower()
        if response == answer:
            print("\nCorrect! The door opens allowing you to proceed.")
            break
        else:
            print("\nIncorrect, try again.")        

def number_lock_puzzle():
    correct_code = "91"
    while True:
        response = input("\nEnter the 4-digit code to unlock the cabinet (Hint: 'The code is the product of two prime numbers that add up to 20'): ")
        if response == correct_code:
            print("\nCorrect! The cabinet opens, revealing valuable supplies and a weapon.")
            break
        else:
            print("\Incorrect, try again.")

#The inventory for all the items
inventory = []
visitedLocations = []
def visit_location(location):
    """Adds a location to the visited list if it is not already present."""
    if location not in visitedLocations:
        visitedLocations.append(location)
        print(f"You visited {location}.")
    else:
        print(f"You have already visited {location}.")

#Function to manage inventory - DIFFERENT
def attack_inventory(item, damage):
    if item not in player.attacks:
        if len(player.attacks) >= 3:
            while True:
                choice = input("\nYour attack inventory is full. Remove an item? Y/N: ").upper()
                if choice == "Y":
                    print("\nYour current attack inventory:")
                    attack_list = list(player.attacks.items())
                    for i, (attack_item, attack_damage) in enumerate(attack_list):
                        print(f"{i + 1}. {attack_item} ({attack_damage} damage)")

                    while True:
                        try:
                            remove_choice = int(input("\nEnter the number of the item you want to remove: "))
                            if 1 <= remove_choice <= len(attack_list):
                                item_to_remove = attack_list[remove_choice - 1][0]
                                del player.attacks[item_to_remove]
                                player.attacks[item] = damage
                                print(f"\nYou removed {item_to_remove} and added {item}.")
                                return
                            else:
                                print("\nInvalid choice. Please select a valid number.")
                        except ValueError:
                            print("\nInvalid input. Please enter a number.")
                elif choice == "N":
                    return
                else:
                    print("\nPlease enter Y or N.")
        else:
            player.attacks[item] = damage
            print(f"\n\nYou added {item} to your inventory. It deals {damage} damage.")
    else:
        print(f"\nYou already have {item} in your inventory.")

def healing_inventory(item, healing_value):
    if item not in player.healing_items:
        if len(player.healing_items) >= 3:
            while True:
                choice = input("\nYour healing inventory is full. Remove an item? Y/N: ").upper()
                if choice == "Y":
                    print("\nYour current healing inventory:")
                    heal_list = list(player.healing_items.items())
                    for i, (heal_item, heal_value) in enumerate(heal_list):
                        print(f"{i + 1}. {heal_item} ({heal_value} HP)")

                    while True:
                        try:
                            remove_choice = int(input("\nEnter the number of the healing item you want to remove: "))
                            if 1 <= remove_choice <= len(heal_list):
                                item_to_remove = heal_list[remove_choice - 1][0]
                                del player.healing_items[item_to_remove]
                                player.healing_items[item] = healing_value
                                print(f"\nYou removed {item_to_remove} and added {item}.")
                                return
                            else:
                                print("\nInvalid choice. Please select a valid number.")
                        except ValueError:
                            print("\nInvalid input. Please enter a number.")
                elif choice == "N":
                    return
                else:
                    print("\nPlease enter Y or N.")
        else:
            player.healing_items[item] = healing_value
            print(f"\nYou added {item} to your healing inventory. It restores {healing_value} health.")
    else:
        print(f"\nYou already have {item} in your healing inventory.")


#The starting location for the game and also the addition of a pepper spray. 
def overgrownLibrary():
    global inventory
    attack_inventory("Pepper spray", 5) #Adds pepper spray to inventory along with the damage it causes
    healing_inventory("Chug jug", 15)
    next_location("Overgrown library") #Moves to the location the user chooses

#The second location for the game and also the addition of a taser. 
def burnedOutSchool():
    global inventory
    attack_inventory("Taser", 10) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Flowberry fizz", 12)
    next_location("Burned out school") #Moves to the location the user chooses

#The third location for the game and also the addition of a baton
def crumblingHospital():
    global inventory
    attack_inventory("Baton", 7) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Big pot", 12)
    next_location("Crumbling hospital") #Moves to the location the user chooses

#The fourth location for the game and also the attraction of a knife
def abandonedCitySquare():
    global inventory
    attack_inventory("Knife", 8) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Slurp juice", 13)
    next_location("Abandoned city square") #Moves to the location the user chooses

#The fifth location for the game and also the attraction of a handgun
def ruinedFactory():
    global inventory
    riddle_puzzle()
    attack_inventory("Handgun", 12) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Flopper", 8)
    if "Handgun" not in player.attacks:
        print("\nYou have found your apprentice, Mara. She will come along with you on your journey.")
    next_location("Ruined factory") #Moves to the location the user chooses

#The sixth location for the game and also the attraction of a axe
def hiddenGarden():
    global inventory
    attack_inventory("Axe", 11) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Slurpfish", 8)
    next_location("Hidden garden") #Moves to the location the user chooses

#The seventh location for the game and also the attraction of a bow and arrow
def collapsedSubwayTunnel():
    global inventory
    attack_inventory("Bow and arrow", 13) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Med kit", 10)
    next_location("Collapsed subway tunnel") #Moves to the location the user chooses

#The eight location for the game and also the attraction of a machine gun
def floodedBunker():
    global inventory
    attack_inventory("Machine gun", 15) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Med mist", 10)
    next_location("Flooded bunker") #Moves to the location the user chooses
    

#The ninth location for the game and also the attraction of a sniper rifle
def radioTower():
    global inventory
    attack_inventory("Sniper rifle", 14) #Adds ________ to inventory along with the damage it causes
    healing_inventory("Small pot", 8)
    next_location("Radio tower") #Moves to the location the user chooses

#The final location for the game and also the attraction of a invisibility cloak
def guardiansLair():
    global inventory
    required_locations = {"Crumbling Hospital", "Collapsed Subway Tunnel", "Radio Tower"}
    if required_locations.issubset(set(visitedLocations)):
        typewriter("\nYou are at an old place where the Guardian lives; the final battle happens here.")
        attack_inventory("Nuclear bomb", 15)
        healing_inventory("Guzzle juice", 10)
        guardian = Enemy(name="The Guardian", health=100)
        typewriter(f"\nThe final battle begins! {player.name} vs {guardian.name}. ")

        number_lock_puzzle()
        #Battle loop for the game.
        while player.health > 0 and guardian.health > 0:
            #The player's turn.
            typewriter("\nIt's your turn. ")
            print("\nChoose your attack: ")

            attack_list = list(player.attacks.keys())
            for i in range(len(attack_list)):
                print(f"{i + 1}. {attack_list[i]}")
            
            while True:
                try:
                    choice = int(input("\nEnter the number of the attack you want to use: "))
                    if 1 <= choice <= len(attack_list): #Calls the attack
                        attack_name = attack_list[choice - 1]
                        break
                    else:
                        print("\nInvalid choice. Please enter a valid nymber")
                except ValueError:
                    print("\nInvalid choice. Please enter a valid number")
            
            damage = player.perform_attack(attack_name) #Performs the attack
            guardian.health -= damage #Removes the damage from the guardian's health
            print(f"\n{player.name} attacks {guardian.name} for {damage} damage. ")
            print(f"\n{player.name} has {player.health} health left and {guardian.name} has {guardian.health} health left. ")

            if guardian.health <= 0: #Says the guardian has been defeated
                print(f"\n{guardian.name} has been defeated! You have saved your brother!")
                break

            #POSSIBLE CODE
            if player.health <= 50:  # Optionally trigger healing when health is low
                health_list = list(player.healing_items.keys())
                for i in range(len(health_list)):
                    print(f"{i + 1}. {health_list[i]}")
            
                while True:
                    try:
                        choice = int(input("\nEnter the number of the healing item you want to use: "))
                        if 1 <= choice <= len(health_list): #Calls the healing item
                            item_name = health_list[choice - 1]
                            break
                        else:
                            print("\nInvalid choice. Please enter a valid nymber")
                    except ValueError:
                        print("\nInvalid choice. Please enter a valid number")
                damage = player.heal(item_name) #Performs the heal
                player.health += damage
            



            #The guardian's turn.
            print("\nIt's the Guardian's turn. ")
            damage = random.randint(5, 15) #Damages the player a random amount of damage
            player.health -= damage #Removes the damage from the player's health
            print(f"\n{guardian.name} attacks you for {damage} damage. ")
            print(f"\n{player.name} has {player.health} health left and {guardian.name} has {guardian.health} health left. ")


            if player.health <= 0: #Says the player has been defeated
                print(f"\nYou have been defeated by {guardian.name}. Game over.")
                break
    else:
        #Makes the program go back to a certian location so the user can visit the required locations
        print("\nYou haven't visited all the required locations yet. Please visit the Crumbling Hospital, Collapsed Subway Tunnel, and Radio Tower before continuing.")
        floodedBunker()


    

#Make a list for the options of the next locations. - DIFFERENT
def next_location(current_room):
    rooms = {
        "Overgrown library": {"Description": "\nYou are at a quiet, creepy place with lots of plants and old books full of forgotten knowledge.", "directions": {"East (Abandonded City Square)": abandonedCitySquare, "Southeast (Ruined Factory)": ruinedFactory, "South (Burned-out School)": burnedOutSchool}},
        "Burned out school": {"Description": "\nYou are at a scary reminder of the town's past with burned walls and reminders of a lost world.", "directions": {"North (Overgrown Library)": overgrownLibrary, "Northeast (Abandoned City Square)": abandonedCitySquare, "East (Ruined Factory)": ruinedFactory, "Southeast (Hidden Garden)": hiddenGarden, "South (Crumbling Hospital)": crumblingHospital}},
        "Crumbling hospital": {"Description": "\nYou are at a lonely, falling-apart hospital with broken and old medical stuff and notes from people who died before the disaster.", "directions": {"North (Burned-out School)": burnedOutSchool, "Northeast (Ruined Factory)": ruinedFactory, "East (Hidden Garden)": hiddenGarden}},
        "Abandoned city square": {"Description": "\nYou are at a central place for people looking for possessions, but watch out for traps and other people also looking for belongings.", "directions": {"West (Overgrown Library)": overgrownLibrary, "Southwest (Burned-out School)": burnedOutSchool, "South (Ruined Factory)": ruinedFactory, "Southeast (Flooded Bunker)": floodedBunker, "East (Collapsed Subway Tunnel)": collapsedSubwayTunnel}},
        "Ruined factory": {"Description": "\nThe room you are in is filled with broken machines, dangerous traps, and a place to find cool stuff.", "directions": {"North (Abandoned City Square)": abandonedCitySquare, "Northeast (Collapsed Subway Tunnel)": collapsedSubwayTunnel, "East (Flooded Bunker)": floodedBunker, "Southeast (Radio Tower)": radioTower, "South (Hidden Garden)": hiddenGarden, "Southwest (Crumbling Hospital)": crumblingHospital, "West (Burned-out School)": burnedOutSchool, "Northwest (Overgrown Library)": overgrownLibrary}},
        "Hidden garden": {"Description": "\nYou are at a wild place with plants that can help you heal.", "directions": {"West (Crumbling Hospital)": crumblingHospital, "Northwest": burnedOutSchool, "North (Ruined Factory)": ruinedFactory, "Northeast (Flooded Bunker)": floodedBunker, "East (Radio Tower)": radioTower}},
        "Collapsed subway tunnel": {"Description": "\nThe room you are in is a dark, shaky tunnel full of random creatures; be really careful if you go near it.", "directions": {"West (Abandoned City Square)": abandonedCitySquare, "Southwest (Ruined Factory)": ruinedFactory, "South (Flooded Bunker)": floodedBunker, "Southeast (Guardian's Lair)": guardiansLair}},
        "Flooded bunker": {"Description": "\nYou are at an old underground base with old supplies that could last a soldier 3 years. ", "directions": {"North (Collapsed Subway Tunnel)": collapsedSubwayTunnel, "East (Guardian's Lair)": guardiansLair, "South (Radio Tower)": radioTower, "Southwest (Hidden Garden)": hiddenGarden, "West (Ruined Factory)": ruinedFactory, "Northwest (Abandoned City Square)": abandonedCitySquare}},
        "Radio tower": {"Description": "\nYou are at a tall place where old signals can be found, but there are lots of people trying to keep it safe.", "directions": {"West (Hidden Garden)": hiddenGarden, "Northwest (Ruined Factory)": ruinedFactory, "North (Flooded Bunker)": floodedBunker, "Northeast (Guardian's Lair)": guardiansLair}}
    }
    
    while True:
        print(rooms[current_room]["Description"])
        time.sleep(5)
        print("\n\nPossible directions:")
        
        # Display the available directions with numbers
        direction_list = list(rooms[current_room]["directions"].keys())
        for i, direction in enumerate(direction_list):
            print(f"{i + 1}. {direction}")
        
        # Get user input by number
        try:
            choice = int(input("\nEnter the number of the direction you'd like to go: "))
            if 1 <= choice <= len(direction_list):
                selected_direction = direction_list[choice - 1]
                next_room = rooms[current_room]["directions"][selected_direction]
                next_room()  # Call the function for the next room
                break
            else:
                print("\nInvalid choice. Please select a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#Starts the game

while True:
    startGame = input("\nWould you like to start the game? Y/N: ").upper()
    if startGame == "Y":
        overgrownLibrary()
        break
    elif startGame == "N":
        print("\nType 'Y' whenever you are ready to start the game. ")
        startGame = input("\nWould you like to start the game? Y/N: ").upper()
        if startGame == "Y":
            overgrownLibrary()
            break
        else:
            print("\nPlease enter a valid option. ")          
    else: 
        print("\nPlease enter a valid option. ")
