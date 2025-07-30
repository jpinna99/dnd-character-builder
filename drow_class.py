from character_class import Character
import json

with open('formatted-spell-list.json', 'r', encoding='utf-8') as master_spell_list:
    master_spell_list = json.load(master_spell_list)


class Drow(Character):
    def __init__(self, name):
        super().__init__(name)
        self.subrace = 'drow'
        self.ability_scores['charisma']['base score'] += 1
        self.drow_features = {
            'darkvision': 120,
            'sunlight sensivity': 'disadvanatage on attack rolls and perception checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.',
            'drow magic': ['dancing lights', 'faerie fire', 'darkness']
        }
        self.drow_proficiencies = {
            "weapons": ['rapiers', 'shortswords', 'hand crossbows']
        }
        self.size = 'medium'

    def get_darkvision(self):
        return self.darkvision
    def get_drow_proficiencies(self):
        return self.drow_proficiencies
    def get_drow_features(self):
        return self.drow_features

    def add_dancing_lights(self):
        for spell in master_spell_list:
            if spell['name'].lower() == 'dancing lights':
                self.spells['cantrips']['cantrip list'].append(spell)
    def add_faerie_fire(self):
        for spell in master_spell_list:
            if spell['name'].lower() == 'faerie fire':
                self.spells['spells']['spell list'].update(spell)  
    def superior_darkvision(self):
        self.darkvision = 120
    def apply_drow_proficiencies(self):
        self.proficiencies['weapons'].extend(self.drow_proficiencies['weapons'])