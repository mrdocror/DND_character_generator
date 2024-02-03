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

# Defining modifiers and skills
str_modifier = athletics = 0
dex_modifier = acrobatics = sleight_of_hand = stealth = 0
int_modifier = arcana = history = investigation = nature = religion = 0
wis_modifier = animal_handling = insight = medicine = perception = survival = 0
cha_modifier = deception = intimidation = performance = persuasion = 0

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
language3 = "none" # This MAY be changed later depending on the subclass

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

print("We have chosen the race of", race, "for you...")

if race == "human":
    print("Humans are the squishiest race option. Luckily, they are also the most flexible, giving an extra +1 to all of your stats.")
    strength += 1
    dexterity += 1
    constitution += 1
    intelligence += 1
    wisdom += 1
    charisma += 1
elif race == "halfling":
    print("Halflings are half people, because they're very smol beings. Due to this, they get a +2 in dexterity.")
    dexterity += 2
elif race == "elf":
    print("Elves are elegant people, but also dangerous. They get a +2 in dexterity.")
    dexterity += 2
else:
    print("Dwarves are small people, but they are very hard workers. Dwarves get a +2 in constitution.")
    constitution += 2

print()

# The only race to not have subraces is human, so we choose that for the user here
if race == "halfling" or race == "elf" or race == "dwarf":
    print("This race also has subraces. We have also chosen that for you.")
    if race == "halfling":
        subrace = random.choice(halfling_subrace_list)
        if subrace == "lightfoot":
            print("Your character is a Lightfoot Halfling. As implied, they are light on their feet and very charming. They give you a +1 to charisma.")
            charisma += 1
        else:
            print("Your character is a Stout Halfling. Like implied, they are short and stout. They get a +1 to constitution.")
            constitution += 1
    elif race == "elf":
        subrace = random.choice(elf_subrace_list)
        if subrace == "high":
            print("You character is a High Elf. They are very intelligent and scholarly, with a +1 to intelligence.")
            intelligence += 1
        else:
            print("Your character is a Wood Elf. They have an innate connection to nature and wildlife. They get a +1 to wisdom.")
            wisdom += 1
    elif race == "dwarf":
        subrace = random.choice(dwarf_subrace_list)
        if subrace == "hill":
            print("Your character is a Hill Dwarf. They are an intelligent bunch, giving your character a +1 to wisdom.")
            intelligence += 1
        else:
            print("Your character is a Mountain Elf. To handle the brisk winters, they have grown to be hardy. They get a +2 to strength.")
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
def language_randomizer():
    lang = random.choice(language_list)
    print("Your character's additional language will be " + lang + ".")
    print()

if race == "human":
    print("Humans can speak common, but they also get a second, random language. We have chosen this for you as well.")
    language_randomizer()
    lang = language2
elif subrace == "high":
    print("High elves get an extra random language, We have chosen this for you as well.")
    language_randomizer()
    lang = language3


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

print("Your character will have a speed of", speed)
print()

# Assigning the character a background
background = random.choice(background_list)

def additional_languages():
    if language2 == "none":
        language2 = language_randomizer()
        language3 = language_randomizer()
        print("You additionally have these languages:", language2, "and", language3)
        print()
    elif language3 == "none":
        language3 = language_randomizer()
        language4 = language_randomizer()
        print("You additionally have these languages:", language3, "and", language4)
        print()
    else:
        language4 = language_randomizer()
        language5 = language_randomizer()
        print("You additionally have these languages:", language4, "and", language5)
        print()


print("Your character background has also been determined.")

if background == "criminal":
    print("Criminals are very aware of their surroundings and how they are perceived. They are proficient in deception and stealth.")
    deception += 1
    stealth += 1
    print("Criminals are good with their hands, so they also are proficient in a gaming set and the thieves' tools.")
    tool_proficiency = ["one type of gaming set", "thieves' tools"]
    print("You will also get a crowbar, a set of dark common clothes, and 15 gold pieces.")
    equipment = ["crowbar"]
    clothes = ["dark common clothing"]
    gold = 15
elif background == "soldier":
    print("Soldiers are mtough masters of combat. They are proficient in athletics and intimidation.")
    athletics += 1
    intimidation += 1
    print("Solders have learned how to operate machinery, but also need to spend time relaxing. They are proficient in a gaming set and land vehicles.")
    tool_proficiency = ["one type of gaming set", "land vehicles"]
    print("You also get an insignia of rank, a trophy taken from a fallen enemy, common clothes, and 10 gold pieces.")
    equipment = ["insignia of rank", "trophy taken from fallen enemy"]
    clothes = ["commom clothing"]
    gold = 10
    print()
    special_item = input("Soldiers also get either bone dice or a deck of cards. Which would you like you character to have? ")
    equipment.append(special_item)
elif background == "sage":
    print("Sages are masters of history and the arcane. They are proficient in arcana and history.")
    arcana += 1
    history += 1
    print("Sages need to know how to read in multiple languages to earn more knowledge, so they get 2 additional random languages.")
    additional_languages()
    print("You also get a bottle of black ink, a quill, a small knife, a letter from a dead colleague, common clothes, and 10 gold pieces.")
    equipment = ["bottle of black ink", "quill", "small knife", "letter from a dead colleague"]
    clothes = ["common clothing"]
    gold = 10
else:
    print("Acolytes are religious folk, so they are proficient in insight and religion.")
    insight += 1
    religion += 1
    print("Acolytes are scholars of their religion, so they need to read in multiple languages. They get 2 additional random languages.")
    additional_languages()
    print("You also get a holy symbol, prayer book, vestments, common clothes, and 15 gold pieces.")
    equipment = ["holy symbol", "prayer book"]
    clothes = ["vestments", "common clothing"]
    gold = 15

print()

# Defining stats, 3-18

# Defining strength modifiers for 
def modifier(stat):
    return (stat - 10) // 2

str_modifier = modifier(strength)
dex_modifier = modifier(dexterity)
con_modifier = modifier(constitution)
int_modifier = modifier(intelligence)
wis_modifier = modifier(wisdom)
cha_modifier = modifier(charisma)