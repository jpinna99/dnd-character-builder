import math
import random

# class definitions
class Character:
# constructor
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.age = 0
        self.gender = ''
        self.alignment = ''
        self.size = ''
        self.speed = 0
        self.languages = []
        self.race = ''
        self.subrace = ''
        self.DnDclass = ''
        self.background = ''
        self.HP = {
            "current": 0,
            "max": 0,
            'temp': 0
        }
        self.armor_class = ''
        self.proficiency_bonus = ''
        self.initiative_bonus = 0
        self.ability_scores = {
            "strength": {
                "base score": 0,
                "modifier": 0
            },
            "dexterity": {
                "base score": 0,
                "modifier": 0
            },
            "constitution": {
                "base score": 0,
                "modifier": 0
            },
            "intelligence": {
                "base score": 0,
                "modifier": 0
            },
            "wisdom": {
                "base score": 0,
                "modifier": 0
            },
            "charisma": {
                "base score": 0,
                "modifier": 0
            }
        }
        self.saving_throws = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0,
        }
        self.skills = {
            "acrobatics": 0,
            "animal handling": 0,
            "arcana": 0,
            "athletics": 0,
            "deception": 0,
            "history": 0,
            "insight": 0,
            "intimidation": 0,
            "investigation": 0,
            "medicine": 0,
            "nature": 0,
            "perception": 0,
            "performance": 0,
            "persuasion": 0,
            "religion": 0,
            "sleight of hand": 0,
            "stealth": 0,
            "survival": 0
        }
        self.proficiencies = {
            "armor": [],
            "weapons": [],
            "tools": [],
            "saving throws": [],
            "skills": []
        }
        self.equipment = {
            "weapons": {},
            "armor": "",
            "tools": [],
            "active": {
                "weapons": [],
                "armor": "",
                "shield": False,
                "tools": [],
            }
        }
        self.wealth = {'gold': 0}
        self.spells = {},
        self.vulnerabilities = []
        self.immunities = []
        self.resistances = []
        self.has_inspiration = False
        self.inspiration_die = ""
        self.death_saves = {
            "successes": [],
            "failures": []
        }
    
# string repr
    def __repr__(self):
        return "DnD Character"
    
# getters
    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_alignment(self):
        return self.alignment
    def get_size(self):
        return self.speed
    def get_speed(self):
        return self.speed
    def get_languages(self):
        return self.languages
    def get_race(self):
        return self.race
    def get_subrace(self):
        return self.subrace
    def get_class(self):
        return self.DnDclass
    def get_background(self):
        return self.background
    def get_HP(self):
        return self.HP
    def get_armor_class(self):
        return self.armor_class        
    def get_proficiency_bonus(self):
        return self.proficiency_bonus
    def get_initiative_bonus(self):
        return self.initiative_bonus
    def get_ability_scores(self):
        return self.ability_scores
    def get_saving_throws(self):
        return self.saving_throws
    def get_skills(self):
        return self.skills
    def get_proficiencies(self):
        return self.proficiencies
    def get_equipment(self):
        return self.equipment
    def get_weapons(self):
        return self.equipment['weapons']
    def get_active_weapons(self):
        return self.equipment['active']['weapons']
    def get_wealth(self):
        return self.wealth
    def get_spells(self):
        return self.spells
    def get_vulnerabilities(self):
        return self.vulnerabilities
    def get_immunities(self):
        return self.immunities
    def get_resistances(self):
        return self.resistances
    def get_has_inspiration(self):
        return self.has_inspiration
    
# setters
    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else: 
            print('Name must be a string')
    def set_level(self, level):
        if isinstance(level, int):
            self.level = level
        else:
            print("Level must be integer")
    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            print("Age must be integer")
    def set_gender(self, gender):
        if isinstance(gender, str):
            self.gender = gender
        else:
            print("Gender must be a string (ex: 'male' or 'female')")
    def set_alignment(self, alignment):
        if isinstance(alignment, str):
            self.alignment = alignment
        else:
            print("Alignment must be a string")
            print("Please choose from the following:")
            print("  Lawful Good")
            print("  Neutral Good")
            print("  Chaotic Good")
            print("  Lawful Neutral")
            print("  True Neutral")
            print("  Chaotic Neutral")
            print("  Lawful Evil")
            print("  Neutral Evil")
            print("  Chaotic Evil")
    def set_size(self, size):
        if isinstance(size, str):
            self.size = size
        else:
            print("Size must be string (ex: Small, Medium, Large)")
    def set_speed(self, speed):
        if isinstance(speed, int):
            self.speed = speed
        else:
            print("Speed must be integer")
    def set_languages(self, languages):
        all_strings = map(lambda item: isinstance(item, str), languages)
        if all(all_strings):
            self.languages = languages
        else:
            print("Languages must be strings (ex. Common, Elven, Infernal, etc.)")
    def set_race(self, race):
        if isinstance(race, str):
            self.race = race
        else: 
            print('Race must be a string') 
    def set_subrace(self, subrace):
        if isinstance(subrace, str):
            self.subrace = subrace
        else: 
            print('Subrace must be a string')
    def set_class(self, DndClass):
        if isinstance(DndClass, str):
            self.DnDclass = DndClass
        else: 
            print('Class must be a string')
    def set_background(self, background):
        if isinstance(background, str):
            self.background = background
        else: 
            print('Background must be a string')
    def set_HP(self, HP):
        if isinstance(HP, int):
            self.HP['max'] = HP
            self.HP['current'] = self.HP['max']
        else:
            print("HP must be integer")
    def set_temp_HP(self, temp_HP):
        if isinstance(temp_HP, int):
            self.HP['temp'] = temp_HP
        else:
            print("Temp HP must be integer")
    def set_armor_class(self, armor_class):
        if isinstance(armor_class, int):
            self.armor_class = armor_class
        else:
            print("Armor class must be integer")
    def set_proficiency_bonus(self, proficiency_bonus):
        if isinstance(proficiency_bonus, int):
            self.proficiency_bonus = proficiency_bonus
        else:
            print("Proficiency bonus must be integer")
    def set_initiative_bonus(self, initiative_bonus):
        if isinstance(initiative_bonus, int):
            self.initiative_bonus = initiative_bonus
        else:
            print("Initiative bonus must be integer")
    def set_ability_scores(self, ability_scores):
        char_abilities = self.ability_scores.keys()
        for ability in ability_scores.keys():
            if ability not in char_abilities:
                print("Invalid ability found")
                return None
            for stat in ability_scores.values():
                if isinstance(stat['base score'], int) and isinstance(stat['modifier'], int):
                    continue
                else:
                    print("Base score and modifier must be integers")
                    return None
        self.ability_scores = ability_scores
    def set_saving_throws(self, saving_throws):
        char_saves = self.saving_throws.keys()
        for save in saving_throws.keys():
            if save not in char_saves:
                print("Invalid saving throw found")
                return None
            for stat in saving_throws.values():
                if isinstance(stat, int):
                    continue
                else:
                    print("Saving throw stats must be integers")
                    return None
        self.saving_throws = saving_throws
    def set_skills(self, skills):
        char_skills = self.skills.keys()
        for skill in skills.keys():
            if skill not in char_skills:
                print("Invalid skill found")
                return None
            for stat in skills.values():
                if isinstance(stat, int):
                    continue
                else:
                    print("Skill stats must be integers")
                    return None
    def set_proficiencies(self, proficiencies):
        self.proficiencies = proficiencies
    def set_equipment(self, equipment):
        self.equipment = equipment
    def set_wealth(self, wealth):
        self.wealth = wealth
    def set_vulnerabilities(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities
    def set_immunities(self, immunities):
        self.immunities = immunities
    def set_resistances(self, resistances):
        self.resistances = resistances
    def set_has_inspiration(self, has_inspiration):
        if isinstance(has_inspiration, bool):
            self.has_inspiration = has_inspiration
        else:
            print("Inspiration must be either True or False")


# calculations
    def calculate_armor_class(self):
        active_armor = self.equipment['active']['armor']
        base_AC = 10
        dex_mod = self.ability_scores['dexterity']['modifier']
        total = base_AC + dex_mod
        armor_addition = 0
        match active_armor:
            case 'padded':
                    armor_addition += 1
                    total = base_AC + dex_mod + armor_addition
            case 'leather':
                    armor_addition += 1
                    total = base_AC + dex_mod + armor_addition
            case 'studded leather':
                    armor_addition += 2
                    total = base_AC + dex_mod + armor_addition
            case 'hide':
                    if dex_mod > 2:
                        dex_mod = 2
                    armor_addition += 2
                    total = base_AC + dex_mod + armor_addition
            case 'chain shirt':
                    if dex_mod > 2:
                        dex_mod = 2
                    armor_addition += 3
                    total = base_AC + dex_mod + armor_addition
            case 'scale mail':
                    if dex_mod > 2:
                        dex_mod = 2
                    armor_addition += 4
                    total = base_AC + dex_mod + armor_addition
            case 'breastplate':
                    if dex_mod > 2:
                        dex_mod = 2
                    armor_addition += 4
                    total = base_AC + dex_mod + armor_addition
            case 'half plate':
                    if dex_mod > 2:
                        dex_mod = 2
                    armor_addition += 5
                    total = base_AC + dex_mod + armor_addition
            case 'ring mail':
                    total = 14
            case 'chain mail':
                    total = 16
            case 'splint':
                    total = 17
            case 'plate':
                    total = 18
        is_shield_active = self.equipment['active']['shield']
        if is_shield_active:
            total +=2
        self.armor_class = total
    def input_ability_scores(self, str, dex, con, intel, wis, cha):
        all_ints = map(lambda item: isinstance(item, int), [str, dex, con, intel, wis, cha])
        if all(all_ints):
            self.ability_scores['strength']['base score'] += str
            self.ability_scores['dexterity']['base score'] += dex
            self.ability_scores['constitution']['base score'] += con
            self.ability_scores['intelligence']['base score'] += intel
            self.ability_scores['wisdom']['base score'] += wis
            self.ability_scores['charisma']['base score'] += cha
    def calculate_modifiers(self):
        for score in self.ability_scores:
            base_score = self.ability_scores[score]['base score']
            self.ability_scores[score]['modifier'] = math.floor((base_score - 10) / 2)
    def calculate_saving_throws(self):
        for save in self.saving_throws:
            self.saving_throws[save] += self.ability_scores[save]['modifier']
    def calculate_skills(self):
        str_mod = self.ability_scores['strength']['modifier']
        dex_mod = self.ability_scores['dexterity']['modifier']
        con_mod = self.ability_scores['constitution']['modifier']
        int_mod = self.ability_scores['intelligence']['modifier']
        wis_mod = self.ability_scores['wisdom']['modifier']
        cha_mod = self.ability_scores['charisma']['modifier']
        self.skills['acrobatics'] += dex_mod
        self.skills['animal handling'] += wis_mod
        self.skills['arcana'] += int_mod
        self.skills['athletics'] += str_mod
        self.skills['deception'] += cha_mod
        self.skills['history'] += int_mod
        self.skills['insight'] += wis_mod
        self.skills['intimidation'] += cha_mod
        self.skills['investigation'] += int_mod
        self.skills['medicine'] += wis_mod
        self.skills['nature'] += int_mod
        self.skills['perception'] += wis_mod
        self.skills['performance'] += cha_mod
        self.skills['persuasion'] += cha_mod
        self.skills['religion'] += int_mod
        self.skills['sleight of hand'] += dex_mod
        self.skills['stealth'] += dex_mod
        self.skills['survival'] += wis_mod


# toggles and counters
    def gain_inspiration(self, inspiration_die):
        if type(inspiration_die) != str:
            print("Inspiration die must be in following format: '1d4', '1d6', '1d8'")
        elif len(inspiration_die) != 3 or inspiration_die[1] != 'd':
            print("Inspiration die must be in following format: '1d4', '1d6', '1d8'")
        else:
            self.has_inspiration = True
            self.inspiration_die = inspiration_die
    def use_inspiration(self):
        if self.has_inspiration == False:
            print("You do not have inspiration")
        else:
            self.has_inspiration = False
            print(f"Inspiration gains additional {self.inspiration_die}")
            self.inspiration_die = ""
    def take_damage(self, damage):
        HP_remaining = (self.HP['current'] + self.HP['temp']) - damage
        if HP_remaining <= 0:
            self.HP['current'] = 0
            self.HP['temp'] = 0
            if abs(HP_remaining) >= self.HP['max']:
                print('You are instantly dead')
        else:
            if damage <= self.HP['temp']:
                self.HP['temp'] -= damage
            else:
                damage_minus_temp = damage - self.HP['temp']
                self.HP['current'] -= damage_minus_temp
                self.HP['temp'] = 0
    def heal(self, HP):
        self.HP['current'] += HP
        if self.HP['current'] > self.HP['max']:
            self.HP['current'] = self.HP['max']
    def equip_armor(self, armor):
        if armor != self.equipment['armor']:
            print('You do not have this type of armor')
        else:
            self.equipment['active']['armor'] = armor
    def equip_weapon(self, weapon):
        if weapon not in self.equipment['weapons'].keys():
            print('You do not have this weapon')
        else:
            self.equipment['active']['weapons'].append(weapon)
    def unequip_weapon(self, weapon):
        if weapon not in self.equipment['active']['weapons']:
            print('Weapon not equipped')
        else:
            self.equipment['active']['weapons'].remove(weapon)
    def spend_money(self, wealth_type, money):
        if type(money) != int and type(wealth_type) != str:
            print('Input must be integer')
            print('Type must be string (ex. gold, silver, etc)')
        elif wealth_type not in self.wealth:
            print(f'You do not have any {wealth_type}')
        elif self.wealth[wealth_type] - money < 0:
            print(f'You do not have enough {wealth_type}')
        else:
            self.wealth[wealth_type] -= money
    def make_money(self, wealth_type, money):
        if type(money) != int and type(wealth_type) != str:
            print('Input must be integer')
            print('Type must be string (ex. gold, silver, etc)')
        elif wealth_type not in self.wealth:
            self.wealth[wealth_type] = 0
            self.wealth[wealth_type] += money
        else:
            self.wealth[wealth_type] += money
    def roll_death_save(self, roll):
        if roll == 20:
            self.death_saves['successes'].append('success')
            self.death_saves['successes'].append('success')
        elif roll == 0:
            self.death_saves['failures'].append('failure')
            self.death_saves['failures'].append('failure')
        elif roll >= 10:
            self.death_saves['successes'].append('success')
        else:
            self.death_saves['failures'].append('failure')
        if len(self.death_saves['successes']) == 3:
            print('Creature stabilized')
            self.death_saves['successes'] = []
            self.death_saves['failures'] = []
        if len(self.death_saves['failures']) == 3:
            print('You are dead')
            self.death_saves['successes'] = []
            self.death_saves['failures'] = []
        