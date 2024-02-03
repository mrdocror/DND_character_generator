# 2/3/2024 - This code will help easily generate a simple D&D 5e character sheet.

import random

# Defining stats
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
character_speed = 0

# Defining stat bonuses
str_modifier = 0
dex_modifier = 0
con_modifier = 0
int_modifier = 0
wis_modifier = 0
cha_modifier = 0

# Define races
race_list = ["human", "halfling", "elf", "dwarf"]
halfling_subrace_list = ["lightfoot", "stout"]
elf_subrace_list = ["high", "wood"]
dwarf_subrace_list = ["hill", "mountain"]

# Define background
background_list = ["criminal", "soldier", "sage", "acolyte"]

# Define class
class_list = ["cleric", "rogue", "fighter", "wizard"]

# Defining languages
language_list = ["dwarvish", "elvish", "giant", "gnomish", "goblin", "halfling", "orc"]
language = "common" # By default, all characters have this language
language2 = "none" # This is changed later

# Define enpty stat spots
favorite1 = 0
favorite2 = 0
favorite3 = 0
random1 = 0
random2 = 0
random3 = 0

# Giving the player a choice for a combat, roleplaying, or balanced build. This comes in with the stats rolls.
player_build = input("Would you like a combat, roleplaying, or balanced character? ")
print()

# Display race information
race = random.choice(race_list)
subrace = "none"

print("We have chosen the", race, "race for you...")

if race == "human":
    print("Humans are the squishiest race option. Luckily, they are also the most flexible, giving an extra +1 to all of your stats.")
    print()
    strength += 1
    dexterity += 1
    constitution += 1
    intelligence += 1
    wisdom += 1
    charisma += 1
elif race == "halfling":
    print("Halflings are half people, because they're very smol beings. Due to this, they get a +2 in dexterity.")
    print()
    dexterity += 2

elif race == "elf":
    print("Elves are elegant people, but also dangerous. They get a +2 in dexterity.")
    print()
    dexterity += 2

elif race == "dwarf":
    print("Dwarves are small people, but they are very hard workers. Just look at Thorin Oakenshield! Dwarves get a +2 in constitution.")
    print()
    constitution += 2


# The only race to not have subraces is human, so we choose that for the user here
if race == "halfling" or race == "elf" or race == "dwarf":
    print("This race also has subraces. We have also chosen that for you.")
    if race == "halfling":
        subrace = random.choice(halfling_subrace_list)
        if subrace == "lightfoot":
            print("Your character is a Lightfoot Halfling. As implied, they are light on their feet and very charming. They give you a +1 to charisma.")
            print()
            charisma += 1
        else:
            print("Your character is a Stout Halfling. Like implied, they are short and stout. They get a +1 to constitution.")
            print()
            constitution += 1
    elif race == "elf":
        subrace = random.choice(elf_subrace_list)
        if subrace == "high":
            print("You character is a High Elf. They are very intelligent and scholarly, with a +1 to intelligence.")
            print()
            intelligence += 1
        else:
            print("Your character is a Wood Elf. They have an innate connection to nature and wildlife. They get a +1 to wisdom.")
            print()
            wisdom += 1
    elif race == "dwarf":
        subrace = random.choice(dwarf_subrace_list)
        if subrace == "hill":
            print("Your character is a Hill Dwarf. They are an intelligent bunch, giving your character a +1 to wisdom.")
            print()
            intelligence += 1
        else:
            print("Your character is a Mountain Elf. To handle the brisk winters, they have grown to be hardy. They get a +2 to strength.")
            print()
            strength += 2
else:
    print("Your character does not get a subrace, sadly.")
    print()


# Defining what races have which languages
if race == "halfling":
    language2 = "Halfling"
elif race == "elf":
    language2 = "Elvish"
elif race == "dwarf":
    language2 = "dwarvish"


# Some races have random languages
if race == "human":
    print("Humans can speak common, but they also get a second, random language. We have chosen this for you as well.")
    language2 = random.choice(language_list)
    print("Your character's second language will be " + language2 + ".")
elif subrace == "high":
    print("High elves get an extra random language, We have chosen this for you as well.")
    language3 = random.choice(language_list)
    print("Your character's third language will be " + language3 + ".")


# Character speeds vary too
if race == "human":
    speed = 30
elif race == "halfling" or race == "dwarf":
    speed = 25
elif race == "elf":
    if subrace == "wood":
        speed = 35
    else:
        speed = 30

print("Your character will have a speed of", speed, "due to their race classifications.")
print()

# Assigning the character a background
background = "none"



# Defining stats, 3-18
#if strength == 3: