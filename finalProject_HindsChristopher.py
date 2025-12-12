#Christopher Hinds

#7 Dec 2025

#Final Project

#This project is a text-based adventure game written in Python called "The Wizard's Apprentice."
#Players take on the role of Alex the apprentice, tasked with gathering magical ingredients to brew a Potion of Vigor.

# Import required libraries
import random
import time
import sys 

# --- Character Data (Dictionary) ---

player = {
    'name': '',
    'health': 100,
    'strength': 10,
    'defense': 5,
    'inventory': {
        'coins': 10,
        'potion_ingredients': [],
    },
    'location': 'Forest Entrance',
    'status': 'Healthy',
    'has_potion': False
}

# --- Game Functions ---

def create_character():
    """Allows user to input character attributes and stores them in the player dictionary."""
    clear_screen()
    print("=== CHARACTER CREATION ===")
    player['name'] = input("Enter your character's name: ").strip() or "Apprentice Alex"

    while True:
        try:
            health = int(input("Enter your starting health (50-150): "))
            if 50 <= health <= 150:
                player['health'] = health
                break
            else:
                print("Please enter a number between 50 and 150.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            strength = int(input("Enter your strength (5-20): "))
            if 5 <= strength <= 20:
                player['strength'] = strength
                break
            else:
                print("Please enter a number between 5 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            defense = int(input("Enter your defense (1-10): "))
            if 1 <= defense <= 10:
                player['defense'] = defense
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nWelcome, {player['name']}! Your adventure begins...")
    time.sleep(2)

def calculate_damage(attacker_strength, base_damage):
    """
    VALUE-RETURNING FUNCTION: Calculates damage based on attacker's strength.
    Returns the total damage dealt.
    """
    bonus_damage = attacker_strength // 2
    total_damage = base_damage + bonus_damage
    return total_damage

def clear_screen():
    """A helper function for presentation."""
    print("\n" + "="*60 + "\n")

def display_status():
    """Displays the player's current status and inventory."""
    clear_screen()
    print("✨ **CURRENT STATUS** ✨")
    print(f"Name: {player['name']} | Health: {player['health']} | Status: {player['status']}")
    print(f"Strength: {player['strength']} | Defense: {player['defense']}")
    print(f"Location: {player['location']}")
    print(f"Inventory Coins: {player['inventory']['coins']}")
    print(f"Potion Ingredients Collected: {', '.join(player['inventory']['potion_ingredients']) or 'None'}")
    print("\n" + "="*60 + "\n")
    time.sleep(1)

def game_over():
    """Ends the game when health reaches zero."""
    clear_screen()
    print("💀 GAME OVER 💀")
    print(f"{player['name']} has fallen. The quest ends here.")
    print("Thanks for playing!")
    sys.exit()

def fight_slime():
    """A simple combat encounter using random and time libraries. Demonstrates attack functionality."""
    clear_screen()
    print("A giant, gooey SLIME MONSTER blocks your path! 🦠")
    print("Time to fight!")
    time.sleep(1.5)

    slime_health = 50
    slime_strength = 8

    while slime_health > 0 and player['health'] > 0:
        player_roll = random.randint(1, 10)
        slime_roll = random.randint(1, 6)

        print(f"\nRolling initiative... (Pausing for {random.randint(1, 3)} seconds)")
        time.sleep(random.randint(1, 3)) # Use time and random

        if player_roll >= slime_roll:
            # Player attacks: uses calculate_damage (value-returning function)
            base_damage = random.randint(5, 10)
            damage_dealt = calculate_damage(player['strength'], base_damage)
            slime_health -= damage_dealt
            print(f"🗡️ You strike the slime for {damage_dealt} damage (base: {base_damage} + strength bonus)! Slime health: {slime_health}")
        else:
            # Slime attacks: reduces player health based on slime's strength
            base_damage = random.randint(3, 8)
            damage_taken = calculate_damage(slime_strength, base_damage)
            # Player's defense reduces damage taken
            actual_damage = max(1, damage_taken - player['defense'])
            player['health'] -= actual_damage
            player['status'] = 'Injured' if player['health'] < 50 else 'Healthy'
            print(f"💥 The slime hits you for {actual_damage} damage (reduced by {player['defense']} defense)! Your health: {player['health']}")

        time.sleep(1)

    if player['health'] <= 0:
        game_over()
    else:
        print("\n🎉 You defeated the slime monster! 🎉")
        print("It dissolves into a puddle, leaving behind a GLOWING MUSHROOM.")
        player['inventory']['potion_ingredients'].append('Glowing Mushroom')
        player['inventory']['coins'] += 20
        player['location'] = 'Deep Forest' # Update character location
        time.sleep(2)
        display_status()
        deep_forest() # Move to the next area

def deep_forest():
    """Second location logic."""
    clear_screen()
    print("You stand in the DEEP FOREST. Sunlight barely penetrates the canopy.")

    if 'Glowing Mushroom' in player['inventory']['potion_ingredients'] and 'Sparkling Dew' not in player['inventory']['potion_ingredients']:
        print("You spot a strange plant covered in sparkling dew.")
        choice = input("Do you collect the dew? (yes/no): ").lower()
        if choice == 'yes':
            print("💧 You carefully collect the Sparkling Dew in a vial.")
            player['inventory']['potion_ingredients'].append('Sparkling Dew')
            time.sleep(2)
        else:
            print("You leave the dew alone for now.")

    if len(player['inventory']['potion_ingredients']) == 2:
        print("You have all the ingredients! You can head back to the cauldron.")
        choice = input("Go back to the Cauldron area? (yes/no): ").lower()
        if choice == 'yes':
            player['location'] = 'Cauldron Area'
            cauldron_area()
            return

    print("There is nothing more to do here.")
    time.sleep(2)
    # If they choose not to go back, the game loop handles the next step

def cauldron_area():
    """Third location logic: Potion making."""
    clear_screen()
    player['location'] = 'Cauldron Area'
    print("You arrive at the ancient CAULDRON AREA.")
    
    if len(player['inventory']['potion_ingredients']) == 2:
        print("You have the Glowing Mushroom and Sparkling Dew.")
        print("You combine the ingredients in the simmering cauldron.")
        time.sleep(3)
        print("✨ The potion glows a brilliant blue! ✨")
        player['has_potion'] = True # Update character status
        print("You have successfully brewed the Potion of Vigor!")
        time.sleep(2)
        end_game_win()
    else:
        print("The cauldron bubbles menacingly. You are missing ingredients.")
        print(f"You need two ingredients, you currently have {len(player['inventory']['potion_ingredients'])}.")
        time.sleep(3)


def end_game_win():
    """The successful end condition."""
    clear_screen()
    print("🏆 CONGRATULATIONS! YOU WIN! 🏆")
    print(f"{player['name']} delivered the Potion of Vigor to the Master Wizard.")
    display_status()
    sys.exit()


def main_game_loop():
    """
    The main function that runs the game loop.
    This function orchestrates the entire game from start to finish.
    """
    print("Welcome to 'The Wizard's Apprentice' Text Adventure!")
    print("Your goal: Collect ingredients and brew the Potion of Vigor.")
    time.sleep(2)

    # Character creation: allows user to create character with custom attributes
    create_character()

    # Display initial character status
    display_status()

    # Start the adventure sequence
    # The game progresses through functions calling other functions (fight_slime -> deep_forest -> cauldron_area)
    fight_slime()

# Entry point of the script
if __name__ == "__main__":
    # The main function is called here, which runs the entire game
    try:
        main_game_loop()
    except SystemExit:
        pass # Gracefully handle sys.exit() calls
    except Exception as e:
        print(f"An unexpected error occurred: {e}")