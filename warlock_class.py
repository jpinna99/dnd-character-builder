from character_class import Character
import json


with open('formatted-master-spell-list.json', 'r', encoding='utf-8') as master_spell_list:
    master_spell_list = json.load(master_spell_list)

with open('formatted-invocations-list.json', 'r', encoding='utf-8') as invocations_list:
    invocations_list = json.load(invocations_list)


class Warlock(Character):
    # constructor
    def __init__(self, name):
        super().__init__(name)
        self.DnDclass = 'warlock'
        self.proficiency_bonus = 2
        self.level = 1
        self.patron = ''
        self.spells = {
            'cantrips': {
                'known': 2,
                'cantrip list': []
            },
            'spells': {
                'known': 2,
                'spell list': []
            },
            'spell slots': {'available': 1,
                            'maximum': 1},
            'slot level': 1
        }
        self.invocations = {}
        self.proficiencies = {
            "armor": "light armor",
            "weapons": [
                "simple weapons",
            ],
            "tools": None,
            "saving throws": [
                "wisdom",
                "charisma"
            ],
            "skills": []
        }

    # getters
    def get_patron(self):
        return self.patron
    def get_invocations(self):
        return self.invocations
    def get_spell_save_DC(self):
        return self.spell_save_DC
    def get_spell_attack_modifier(self):
        return self.spell_attack_modifier

    # setters
    def set_patron(self, patron):
        if isinstance(patron, str):
            self.patron = patron
        else:
            print("Patron must be string")
    def set_spell_save_DC(self):
        self.spell_save_DC = 8 + self.proficiency_bonus + self.ability_scores['charisma']['modifier']
    def set_spell_attack_modifier(self):
        self.spell_attack_modifier = self.proficiency_bonus + self.ability_scores['charisma']['modifier']

    # choose proficiencies, invocations, spells, etc.
    def choose_warlock_skill_proficiencies(self, skill1, skill2):
        skill1 = skill1.lower()
        skill2 = skill2.lower()
        valid_skills = ['arcana', 'deception', 'history', 'intimidation', 'investigation', 'nature', 'religion']
        if skill1 in valid_skills and skill2 in valid_skills:
            self.proficiencies['skills'].append(skill1)
            self.skills[skill1] += self.proficiency_bonus
            self.proficiencies['skills'].append(skill2)
            self.skills[skill2] += self.proficiency_bonus
        else:
            print("Skill proficiencies must be a strings from following list:")
            print("  Arcana")
            print("  Deception")
            print("  History")
            print("  Intimidation")
            print("  Investigation")
            print("  Nature")
            print("  Religion")
    def calculate_HP(self):
        self.HP['max'] = 8 + self.ability_scores['constitution']['modifier']
        self.HP['current'] = self.HP['max']
    def add_invocation(self, invocation):
        if isinstance(invocation, dict):
            self.invocations.update(invocation)
        else:
            print("Invocation must be dictionary")
    def add_initiative_bonus(self):
        self.initiative_bonus += self.ability_scores['dexterity']['modifier']
    def add_saving_throw_proficiencies(self):
        save_proficiencies = self.proficiencies['saving throws']
        for save in self.saving_throws:
            if save in save_proficiencies:
                self.saving_throws[save] += self.proficiency_bonus
    def choose_starting_spells(self, cantrip1, cantrip2, spell1, spell2):
        for spell in master_spell_list:
            if spell['name'].lower() == cantrip1.lower():
                self.spells['cantrips']['cantrip list'].append(spell)
        for spell in master_spell_list:
            if spell['name'].lower() == cantrip2.lower():
                self.spells['cantrips']['cantrip list'].append(spell)
        for spell in master_spell_list:
            if spell['name'].lower() == spell1.lower():
                self.spells['spells']['spell list'].append(spell) 
        for spell in master_spell_list:
            if spell['name'].lower() == spell2.lower():
                self.spells['spells']['spell list'].append(spell) 
    def add_spell(self, spell_name):
        for spell in master_spell_list:
            if spell['name'].lower() == spell_name.lower() and 'warlock' in spell['class'].lower():
                self.spells['spells']['spell list'].append(spell)
    def cast_spell(self, spell):
        if self.spells['spell slots']['available'] == 0:
            print("Cannot cast spell. No spell slots remaining")
        else:
            spell_list = self.spells['spells']['spell list']
            counter = 0
            for known_spell in spell_list:
                if spell.title() == known_spell['name']:
                    counter += 1
            if counter == 1:
                print(f'{spell.title()} successfully cast')
                self.spells['spell slots']['available'] -= 1
                print(f"You have {self.spells['spell slots']['available']} spell slots remaining")
            else:
                print("Spell not found. Known spells: ")
                for spell in spell_list:
                    print(f'   {spell['name']}')
    def add_warlock_invocations(self, *invocations):
        for invocation in invocations:
            for list_item in invocations_list:
                if list_item['name'].lower() == invocation.lower():
                    self.invocations['invocations list'].append(list_item)
