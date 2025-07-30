from character_class import Character

class Elf(Character):
    def __init__(self, name):
        super().__init__(name)
        self.race = 'elf'
        self.ability_scores['dexterity']['base score'] += 2
        self.speed = 30
        self.elf_features = {
            'darkvision': 60,
            'keen senses': 'proficiency in perception',
            'fey ancestry': ['advantage on saving throws against being charmed', 'magic cannot put you to sleep'],
            'trance': 'deeply meditate in semiconscious state for 4 hours per day',
            'languages': ['common', 'elvish']
        }
        self.saving_throw_advantages = ['charmed']
        self.immunities = ['sleep']

    def get_elf_features(self):
        return self.elf_features
    def get_saving_throw_advantages(self):
        return self.saving_throw_advantages
    
    def apply_elf_languages(self):
        self.languages.extend(self.elf_features['languages'])
    def apply_elf_proficiencies(self):
        self.proficiencies['skills'].append('perception')
        self.skills['perception'] += self.proficiency_bonus