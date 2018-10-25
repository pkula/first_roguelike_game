import random
from prettytable import PrettyTable


def get_random_item():
    weapons_adjectives = ["Sharp", "Sparkly", "Twinkling", "Beautiful",
                          "Succulent", "Joyous", "Enchanted", "Naughty",
                          "Extraordinary", "Frisky", "Tantalizing", "Vibrant",
                          "Groovy", "Dazzling", "Faithful", "Glamorous",
                          "Magnificent", "Victorious", "Mysterious"]

    weapons_types = ["Common", "Rare", "Ancient", "Legendary"]

    weapons = ["Sword", "Greatsword", "Drill", "Axe", "Knife", "Dagger",
               "Club", "Spear", "Hammer", "Shield", "Bow", "Crossbow",
               "Whip", "Cannon", "Revolver", "Gun", "Nunchaku", "Chain", "Rope"]

    armor_adjectives = ["Shining", "Torn", "Baggy", "Machine-Washable",
                        "Oversized", "Rainproof", "Slimming", "Sporty",
                        "Strapless", "Unfashionable", "Scanty", "Roomy",
                        "Revealing", "Modest", "Non-iron", "Itchy",
                        "Flame-retardant", "Conservative", "Brief"]

    armor = ["Jerkin", "Breeches", "Boots", "Breastplate", "Greaves", "Sabatons"]

    armor_type = ["Leather", "Plate"]

    inventory = []

    weapon_adjective_choice = random.choice(weapons_adjectives)
    weapon_choice = random.choice(weapons)
    weapon_type_choice = random.choice(weapons_types)
    concatenate_weapon_name = weapon_adjective_choice + " " + weapon_choice
    #inventory.append([concatenate_weapon_name, weapon_type_choice])

    armor_adjectives_choice = random.choice(armor_adjectives)
    armor_choice = random.choice(armor)
    if armor_choice in armor[0:3]:
        armor_type_choice = armor_type[0]
    else:
        armor_type_choice = armor_type[1]

    concatenate_armor_name = armor_adjectives_choice + " " + armor_choice
    #inventory.append([concatenate_armor_name, armor_type_choice])

