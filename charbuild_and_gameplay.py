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
        self.spells['spell slots']['available'] = self.spells['spell slots']['maximum']
        print(f'Short rest successful. You now have {self.spells['spell slots']['available']} available spell slot(s)')

    def take_long_rest(self):
        self.spells['spell slots']['available'] = self.spells['spell slots']['maximum']
        self.HP['current'] = self.HP['max']
        self.HP['temp'] = 0
        self.shadow_armor["number of uses remaining"] = self.ability_scores['charisma']['modifier']
        self.reapers_blade["number of uses remaining"] = self.ability_scores['charisma']['modifier']
        print(f'Long rest successful. You now have {self.spells['spell slots']['available']} available spell slot(s) and {self.HP['current']} HP')

    def use_crossbow(self):
        if self.equipment["weapons"]['crossbow bolts'] == 0: 
            print("No crossbow bolts left")
        elif "light crossbow" not in self.equipment["active"]["weapons"]:
            print("Weapon not active")
        else:
            print("Crossbow fired")
            self.equipment["weapons"]['crossbow bolts']["quantity"] -= 1

    def level_up_2(self, invocation1, invocation2, additional_spell):
        self.level = 2
        self.spells['spells']['known'] = 3
        self.spells['spell slots'] = {
            "available": 2,
            "maximum": 2
        }
        self.invocations = {
            'known': 2,
            'invocations list': []
        }
        self.add_warlock_invocations(invocation1, invocation2)
        self.add_spell(additional_spell)
        self.set_HP(17)    # add 5 HP + 2 for con mod

    # method below is specific to sorcerer as new_class
    def multiclass(self, original_class, new_class):
        # separate spells by class: 
        original_class_spells = self.__dict__.pop("spells")
        self.__dict__["spells"] = {}
        self.__dict__["spells"][original_class] = original_class_spells
        self.__dict__["spells"][new_class] = {}
        # separate levels and have a combined key:
        original_class_level = self.__dict__.pop("level")
        new_class_level = 1
        self.__dict__["level"] = {original_class: original_class_level,
                                new_class: new_class_level}
        # calc prof bonus: 
        # self.__dict__.proficiency_bonus = self.level[original_class] + self.level[new_class]
        level_bonus_table = {1 + 4*i: 2 + i for i in range(100)}
        for key, value in level_bonus_table.items():
            if original_class_level + new_class_level >= int(key):
                self.__dict__["proficiency_bonus"] = value

        # separate proficiencies by class: 
        # new class proficiencies (armor, weapons, tools, saving throws, skills)
        warlock_proficiencies = self.__dict__.pop('proficiencies')
        self.__dict__["proficiencies"] = {}
        self.__dict__["proficiencies"][original_class] = warlock_proficiencies
        self.__dict__["proficiencies"][new_class] = {}

        # figure out HP and hit dice (assume sorcerer)
        original_HP = self.__dict__["HP"]["max"]
        new_HP = 6 + self.__dict__["ability_scores"]["constitution"]["modifier"]
        total_HP = original_HP + new_HP
        self.set_HP(total_HP)

        

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
soveliss.equip_armor('leather')
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



# Level up Soveliss to Level 2 --- increase number of known spells, spell slots, gain invocations
soveliss.level_up_2('eldritch mind', 'fiendish vigor', 'hex')



# Multiclass Soveliss as SorLock (Sorcerer/Warlock) 
# soveliss.multiclass('warlock', 'sorcerer')



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


















##########################################################################################
##########################################################################################
########################################################################################## 

# create json file holding all character stats after code runs
with open('soveliss-stats.json', 'w') as soveliss_stats:
    json.dump(soveliss.__dict__, soveliss_stats, indent=4)







