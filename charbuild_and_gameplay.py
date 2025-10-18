import json, pprint, random

from warlock_class import Warlock
from sage_class import Sage
from elf_class import Elf
from drow_class import Drow
from reaper_class import Reaper

from dice_rolls import *

# open master spell list and save as variable
with open('formatted-master-spell-list.json', 'r', encoding='utf-8') as master_spell_list:
    master_spell_list = json.load(master_spell_list)

# open invocations list and save as variable
with open('formatted-invocations-list.json', 'r', encoding='utf-8') as invocations_list:
    invocations_list = json.load(invocations_list)


# create master character class for unique character, incorporating classes from other modules
class Soveliss(Warlock, Reaper, Sage, Elf, Drow):
    def __init__(self, name):
        super().__init__(name)
        self.age = 25
        self.gender = 'male'
        self.alignment = 'lawful good'
        self.specialty = "Discredited Academic"
        self.ideal = "The path to power and self-improvement is through knowledge."
        self.flaw = "I am easily distracted by the promise of information."
        self.bond = "I've been searching my whole life for the answer to one question."
        self.appearance = {"skin color": 'purple',
                            'hair color': 'grayish black',
                            'height': '5 ft 2 in',
                            'eye color': 'green'}
    
    def choose_starting_equipment(self):
        self.equipment['weapons'] = {
            'light crossbow': {'quantity': 1, 
                               'damage': '1d8, piercing',
                               'properties': 'Two-Handed, Range, Loading, Ammunition'},
            'crossbow bolts': {'quantity': 20},
            'quarterstaff': {'quantity': 1, 
                             'damage': '1d6, (one-handed), 1d8 (two-handed)',
                             'properties': 'Versatile'},
            'dagger': {'quantity': 1, 
                       'damage': '1d4, piercing',
                       'properties': 'Finesse, Light, Range, Thrown'},
        }
        self.equipment['arcane focus'] = 'monkey paw'
        self.equipment["dungeoneer's pack"] = {
            "backpack": 1,
            "crowbar": 1, 
            "hammer": 1, 
            "piton": 10, 
            "torch": 10, 
            "tinderbox": 1, 
            "rations": 10, 
            "waterskin": 1, 
            "hempen rope (ft)": 50
        }
        self.equipment['armor'] = 'leather'
    
    def take_short_rest(self):
        self.spells["warlock"]['spell slots']['available'] = self.spells["warlock"]['spell slots']['maximum']
        print(f'Short rest successful. You now have {self.spells["warlock"]['spell slots']['available']} available Warlock spell slot(s) and {self.spells["sorcerer"]['spells']['spell slots']} Sorcerer spell slots')
        print("-------------------")

    def take_long_rest(self):
        self.spells["warlock"]['spell slots']['available'] = self.spells["warlock"]['spell slots']['maximum']
        self.spells["sorcerer"]['spells']['spell slots']['1st-level']['available'] = self.spells["sorcerer"]['spells']['spell slots']['1st-level']['maximum']
        self.HP['current'] = self.HP['max']
        self.HP['temp'] = 0
        self.shadow_armor["number of uses remaining"] = self.ability_scores['charisma']['modifier']
        self.reapers_blade["number of uses remaining"] = self.ability_scores['charisma']['modifier']
        print(f'Long rest successful. You now have {self.spells["warlock"]['spell slots']['available']} available Warlock spell slot(s) and {self.spells["sorcerer"]['spells']['spell slots']} Sorcerer spell slots and {self.HP['current']} HP')
        print("-------------------")

    def use_crossbow(self):
        if self.equipment["weapons"]['crossbow bolts'] == 0: 
            print("No crossbow bolts left")
            print("-------------------")
        elif "light crossbow" not in self.equipment["active"]["weapons"]:
            print("Weapon not active")
            print("-------------------")
        else:
            print("Crossbow fired")
            print("-------------------")
            self.equipment["weapons"]['crossbow bolts']["quantity"] -= 1

    def add_spell(self, spell_name, dnd_class):
        for spell in master_spell_list:
            if spell['name'].lower() == spell_name.lower() and dnd_class.lower() in spell['class'].lower():
                self.spells[dnd_class]['spells']['spell list'].append(spell)

    def add_cantrip(self, cantrip_name, dnd_class):
        for spell in master_spell_list:
            if spell['name'].lower() == cantrip_name.lower() and dnd_class.lower() in spell['class'].lower():
                self.spells[dnd_class]['cantrips']['cantrip list'].append(spell)

    def cast_spell(self, spell, spell_level="1st-level"):
        if self.spells['warlock'].get('slot level') < int(spell_level[0]) and self.spells['sorcerer']["spells"]["spell slots"].get(spell_level, None) == None:
            print("You do not have high enough Warlock slot level or Sorcerer spell slots to cast this spell")
        elif self.spells['warlock']['spell slots']['available'] == 0 and self.spells['sorcerer']["spells"]['spell slots'][spell_level]['available'] == 0:
            print("Cannot cast spell. No spell slots remaining of any class")
            print("-------------------")
        else:
            spell_list = []
            for warlock_spell in self.spells['warlock']['spells']['spell list']:
                spell_list.append(warlock_spell)
            for sorcerer_spell in self.spells['sorcerer']['spells']['spell list']:
                spell_list.append(sorcerer_spell)
            counter = 0
            for known_spell in spell_list:
                if spell.title() == known_spell['name']:
                    counter += 1
            if counter == 1:
                print(f'{spell.title()} successfully cast')
                if self.spells['warlock']['spell slots']['available'] > 0:
                    self.spells['warlock']['spell slots']['available'] -= 1
                else:
                    self.spells['sorcerer']["spells"]['spell slots'][spell_level]['available'] -= 1
                print(f"You have {self.spells['warlock']['spell slots']['available']} Warlock spell slot(s) remaining and {self.spells['sorcerer']["spells"]['spell slots'][spell_level]['available']} Sorcerer {spell_level} spell slot(s) remaining")
                for known_spell in self.__dict__['spells']['sorcerer']['spells']['spell list']:
                    if known_spell['name'].lower() == spell.lower():
                        print('This is a sorcerer spell. Make sure you roll on the Wild Magic Surge table!')
            else:
                print("Spell not found. Known spells: ")
                for spell in spell_list:
                    print(f'   {spell['name']}')
        print("-------------------")

    # method below is specific to sorcerer as new_class
    def multiclass(self, original_class, new_class):
        # separate spells by class: 
        original_class_spells = self.__dict__.pop("spells")
        self.spells = {}
        self.spells[original_class] = original_class_spells
        self.spells[new_class] =    {"cantrips": {"known": 4,
                                                            "cantrip list": []},
                                                "spells": {"known": 2,
                                                            "spell list": [],
                                                            "spell slots": {
                                                                "1st-level": {'available': 2,
                                                                              'maximum': 2}
                                                            }}
                                    }
        
        # separate levels and have a combined key:
        original_class_level = self.__dict__.pop("level")
        new_class_level = 1
        self.level = {original_class: original_class_level,
                                new_class: new_class_level}
        # calc prof bonus: 
        # self.proficiency_bonus = self.level[original_class] + self.level[new_class]
        level_bonus_table = {1 + 4*i: 2 + i for i in range(100)}
        for key, value in level_bonus_table.items():
            if original_class_level + new_class_level >= int(key):
                self.proficiency_bonus = value

        # separate proficiencies by class: 
        # new class proficiencies (armor, weapons, tools, saving throws, skills)
        warlock_proficiencies = self.__dict__.pop('proficiencies')
        self.proficiencies = {}
        self.proficiencies[original_class] = warlock_proficiencies
        self.proficiencies[new_class] = {}

        # figure out HP and hit dice (assume sorcerer)
        original_HP = self.HP["max"]
        new_HP = 6 + self.ability_scores["constitution"]["modifier"]   # Level 1 sorcerer HP
        total_HP = original_HP + new_HP
        self.set_HP(total_HP)

        # add new class to object and format as list
        self.DnDclass = [original_class, new_class]

    # Method below levels up Soveliss to Warlock 2 / Sorcerer 1
    def level_up_3(self, invocation1, invocation2, additional_spell, spell_class):
        self.spells['warlock']['spell slots']['maximum'] = 2
        self.add_spell(additional_spell, spell_class)
        self.add_warlock_invocations(invocation1, invocation2)
        self.HP['max'] += 5 + self.ability_scores['constitution']['modifier']
        self.level['warlock'] += 1
        self.spells['warlock']['spells']['known'] = 3

    # Method below levels up Soveliss to Warlock 3 / Sorcerer 1
    def level_up_4(self, additional_spell='darkness', spell_to_replace='expeditious retreat', replacement_spell='misty step', spell_class='warlock'):
        # additional Warlock spell learned (total of 4 up to 2nd level) --- learn Darkness
        # can replace one Warlock spell with another from Warlock list - replace Exp Retreat with Misty Step
        # gain Pact Boon - pact of the Talisman
        self.level['warlock'] += 1
        self.spells[spell_class]['spells']['known'] += 1
        self.spells[spell_class]['slot level'] += 1
        self.add_spell(additional_spell, spell_class)
        self.add_spell(replacement_spell, spell_class)
        self.HP['max'] += 5
        for spell in self.spells[spell_class]['spells']['spell list']:
            if spell['name'].lower() == spell_to_replace.lower():
                self.spells[spell_class]['spells']['spell list'].remove(spell)
                break
    
    def use_talisman(self):
        if self.boons["Pact of the Talisman"]["Number of Uses Remaining"] > 0:
            self.boons["Pact of the Talisman"]["Number of Uses Remaining"] -= 1
            print(f"You have {self.boons["Pact of the Talisman"]["Number of Uses Remaining"]} uses remaining.")
        else:
            print("You have no more uses of this feature.")

def isolate_sorcerer_spells_for_soveliss():
    spell_list = []
    for spell in master_spell_list:
        if "sorcerer" in spell["class"].lower():
            spell_list.append(spell)
    return spell_list

sorcerer_spell_list = isolate_sorcerer_spells_for_soveliss()
sorted_sorcerer_spell_list = sorted(sorcerer_spell_list, key=lambda x: x['level'])

with open('sorcerer_spell_list.json', 'w') as isolated_sorcerer_spell_list:
    json.dump(sorted_sorcerer_spell_list, isolated_sorcerer_spell_list, indent=4)




# class instantiation
soveliss = Soveliss("Soveliss Nailo")

# Level 1 character
# call Character methods — input ability scores, calculate modifiers/saves/init bonus/skills, choose starting equipment and equip armor and weapons 
soveliss.input_ability_scores(8, 10, 14, 13, 12, 15)
soveliss.calculate_modifiers()
soveliss.add_initiative_bonus()
soveliss.calculate_saving_throws()
soveliss.calculate_skills()
soveliss.choose_starting_equipment()
soveliss.don_armor('leather')
soveliss.equip_weapon('dagger')
soveliss.calculate_armor_class()

# call Warlock methods — HP, patron and choose skill proficiencies and starting spells, set spell save and spell attack mod
# 2 cantrips — Eldricth blast and Chill Touch
# 2 1st-level spells — False Life, Ice Knife
soveliss.calculate_HP()
soveliss.set_patron("The Reaper")
soveliss.choose_warlock_skill_proficiencies('Intimidation', 'Investigation')
soveliss.add_saving_throw_proficiencies()
soveliss.choose_starting_spells("Eldritch Blast", "Chill Touch", "Expeditious Retreat", "Ice Knife")
soveliss.set_spell_save_DC()
soveliss.set_spell_attack_modifier()


# call Elf methods — apply elf languages and elf proficiencies
soveliss.apply_elf_languages()
soveliss.apply_elf_proficiencies()

# call Drow methods — add dancing lights cantrip, apply superior darkvision and drow proficiencies
soveliss.add_dancing_lights()
soveliss.superior_darkvision()
soveliss.apply_drow_proficiencies()

# call Sage methods — choose sage languages, apply sage proficiencies and sage equipment
soveliss.choose_sage_languages('Infernal', 'Abyssal')
soveliss.apply_sage_skill_proficiencies()
soveliss.apply_sage_equipment()

# call Reaper methods - initiate Charimsa modifier
soveliss.set_charisma_charges()


# Multiclass Soveliss as SorLock (Sorcerer/Warlock) 
soveliss.multiclass('warlock', 'sorcerer')
soveliss.add_spell('magic missile', 'sorcerer')
soveliss.add_spell('chaos bolt', 'sorcerer')
soveliss.add_cantrip('fire bolt', 'sorcerer')
soveliss.add_cantrip('ray of frost', 'sorcerer')
soveliss.add_cantrip('acid splash', 'sorcerer')
soveliss.add_cantrip('mage hand', 'sorcerer')
soveliss.tides_of_chaos = """Starting at 1st level, you can manipulate the forces of chance and chaos to gain advantage on one attack roll, ability check, or saving throw. Once you do so, you must finish a long rest before you can use this feature again. Any time before you regain the use of this feature, the DM can have you roll on the Wild Magic Surge table immediately after you cast a sorcerer spell of 1st level or higher. You then regain the use of this feature."""


# Level up Soveliss to Warlock level 2 / Sorcerer 1
soveliss.level_up_3('fiendish vigor', 'eldritch mind', 'hex', 'warlock')




##########################################################################################
##########################################################################################
########################################################################################## 
# GAME PLAY
# 8/1/2025 Session:
  # soveliss.take_long_rest()   # long rest, cuddling my tome, in the inn near The Bloated Goat
  # soveliss.use_shadow_armor()   # instinctive use of shadow armor when Titus woke me up hungover
  # soveliss.take_damage(1)   # damage from gust of wind in the cavern
  # soveliss.use_reapers_blade()   # against the kobolds
  # soveliss.take_long_rest()   # after we got back to Oakdale

# 8/15/2025 Session:
soveliss.add_to_inventory('Potion of Draconic Sight', 1)
soveliss.add_to_inventory('Potion of Minor Healing', 2)
# soveliss.take_long_rest()
soveliss.add_to_inventory("Children's learning book (found on path to Greenest)", 1)
# During battle, Soveliss dove behind some rocks for half cover and gained +2 to AC and Dex saves
# soveliss.cast_spell('ice knife')
# soveliss.cast_spell('chaos bolt')
# soveliss.take_short_rest()

# 8/22/2025 Session
# Snuffy gave us all effect of long rest in the keep
soveliss.take_long_rest()
soveliss.cast_spell("ice knife")
soveliss.use_item('potion of Minor healing')  # gave 1 to Titus
# Level up to Level 3

# 8/29/2025 Session
soveliss.take_short_rest()  # DM gave us ability to use new spell slots immediately after level up
soveliss.take_damage(7)  # retain HP before level up
soveliss.set_temp_HP(5)  # Soveliss uses Fiendish Vigor invocation
soveliss.cast_spell('ice knife')
soveliss.cast_spell('chaos bolt')
soveliss.cast_spell('magic missile')
soveliss.add_to_inventory('potion of minor healing', 2)
soveliss.cast_spell('hex')
soveliss.__dict__['boons'] = {
            "Boon of the Fearless Heart": "<p>Once per long rest, the character can automatically succeed on a saving throw against being frightened.<p>"
            }
soveliss.take_long_rest()

# 9/19/2025 Session
soveliss.cast_spell('ice knife')
soveliss.cast_spell('hex')
soveliss.take_damage(1)

# 9/26/2025 Session
soveliss.set_temp_HP(8)  # Soveliss uses fiendish vigor for 8 temp HP
soveliss.use_item('potion of minor healing')  # gave Thalia healing potion

# 10/3/2025 Session
soveliss.take_long_rest()
soveliss.set_temp_HP(5)
soveliss.use_reapers_blade()
soveliss.use_reapers_blade()
soveliss.cast_spell('chaos bolt')
soveliss.cast_spell('magic missile')
soveliss.add_to_inventory('potion of minor healing', 2)    # already had potion from before, total 2
soveliss.cast_spell('magic missile')
soveliss.take_damage(6)
soveliss.take_damage(4)
soveliss.use_shadow_armor()
soveliss.take_damage(11)
soveliss.use_shadow_armor()
soveliss.take_damage(7)
# tides of chaos used

# 10/17/2025 Session
# USE FIENDISH VIGOR AND GET HEALED SOMEHOW (Titus or healing potions)
soveliss.set_temp_HP(6) # Soveliss uses fiendish vigor for 6 temp HP
soveliss.wealth = {"personal": {"gold": 10},
                   "group": {"gold": 210}
                   }
soveliss.gain_inspiration('1d4')
soveliss.use_item('potion of minor healing')
soveliss.heal(5)
soveliss.take_short_rest()
soveliss.heal(11) # uses all three hit dice
soveliss.use_item('potion of minor healing')
soveliss.heal(7)
soveliss.gain_inspiration('1d8')
soveliss.add_to_inventory('wand of wonder', 1)
soveliss.use_reapers_blade()
# tides of chaos used
# tides of chaos regained (Soveliss shed light for 1 minute)
soveliss.cast_spell('ice knife')
soveliss.cast_spell('hex')
soveliss.use_inspiration()
soveliss.cast_spell('magic missile')   # regain HP at start of each turn 


# 10/24/2025 Session
# Level up Soveliss to Warlock 3 / Sorcerer 1
# soveliss.level_up_4()
# pact_of_the_talisman = {
#    "Pact of the Talisman": {
#        "description": "<p>Your patron gives you an amulet, a talisman that can aid the wearer when the need is great. When the wearer fails an ability check, they can add a d4 to the roll, potentially turning the roll into a success. This benefit can be used a number of times equal to your proficiency bonus, and all expended uses are restored when you finish a long rest. If you lose the talisman, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous amulet. The talisman turns to ash when you die.<p>", 
#        "Number of Uses Remaining": soveliss.__dict__["proficiency_bonus"]}}
# soveliss.__dict__["boons"].update(pact_of_the_talisman)
# soveliss.use_talisman()













##########################################################################################
##########################################################################################
########################################################################################## 

# create json file holding all character stats after code runs
with open('soveliss-stats.json', 'w') as soveliss_stats:
    json.dump(soveliss.__dict__, soveliss_stats, indent=4)







