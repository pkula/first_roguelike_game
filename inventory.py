import random
from prettytable import PrettyTable


def get_random_armor():
    armor_adjectives = ["Shining", "Torn", "Baggy", "Machine-Washable",
                        "Oversized", "Rainproof", "Slimming", "Sporty",
                        "Strapless", "Unfashionable", "Scanty", "Roomy",
                        "Revealing", "Modest", "Non-iron", "Itchy",
                        "Flame-retardant", "Conservative", "Brief"]

    armor = ["Jerkin", "Breeches", "Boots", "Breastplate", "Greaves", "Sabatons"]

    armor_type = ["Leather", "Plate"]

    armor_adjectives_choice = random.choice(armor_adjectives)
    armor_choice = random.choice(armor)
    if armor_choice in armor[0:3]:
        armor_type_choice = armor_type[0]
    else:
        armor_type_choice = armor_type[1]

    return [armor_adjectives_choice + " " + armor_choice, armor_type_choice]


def get_random_weapon():
    weapons_adjectives = ["Sharp", "Sparkly", "Twinkling", "Beautiful",
                          "Succulent", "Joyous", "Enchanted", "Naughty",
                          "Extraordinary", "Frisky", "Tantalizing", "Vibrant",
                          "Groovy", "Dazzling", "Faithful", "Glamorous",
                          "Magnificent", "Victorious", "Mysterious"]

    weapons_types = ["Common", "Rare", "Ancient", "Legendary"]

    weapons = ["Sword", "Greatsword", "Drill", "Axe", "Knife", "Dagger",
               "Club", "Spear", "Hammer", "Shield", "Bow", "Crossbow",
               "Whip", "Cannon", "Revolver", "Gun", "Nunchaku", "Chain", "Rope"]

    weapon_adjective_choice = random.choice(weapons_adjectives)
    weapon_choice = random.choice(weapons)
    weapon_type_choice = random.choice(weapons_types)

    return [weapon_adjective_choice + " " + weapon_choice, weapon_type_choice]


def get_weapon_or_armor():
    random_choice = random.randint(1, 2)
    if random_choice == 1:
        return get_random_armor()
    else:
        return get_random_weapon()


def add_item_to_table(random_item, inventory):
    inventory.append(random_item)
    return inventory


def print_table(inventory):
    table_for_display = PrettyTable()
    table_for_display.field_names = ["item", "type"]
    table_for_display.align["item"] = "l"
    table_for_display.align["type"] = "l"

    for item, category in inventory:
        table_for_display.add_row([item, category])
    return table_for_display.get_string(title="Inventory")
