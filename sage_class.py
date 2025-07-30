from character_class import Character


class Sage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.background = 'sage'
        self.sage_skill_proficiencies = ['arcana', 'history']
        self.sage_equipment = {
            "bottle of black ink": 1,
            "quill": 1,
            "small knife": 1,
            "letter from dead colleague posing question I have been unable to answer": 1,
            "set of common clothes": 1,
            "pouch containing 10 gp": 1
        }
        
    def choose_sage_languages(self, lang1, lang2):
        lang1 = lang1.lower()
        lang2 = lang2.lower()
        if isinstance(lang1, str) and isinstance(lang2, str):
            self.languages.append(lang1)
            self.languages.append(lang2)
        else:
            print("Languages must be strings (ex. Common, Elven, Infernal, etc.)")
    def apply_sage_skill_proficiencies(self):
        self.proficiencies['skills'].extend(self.sage_skill_proficiencies)
        self.skills['arcana'] += self.proficiency_bonus
        self.skills['history'] += self.proficiency_bonus
    def apply_sage_equipment(self):
        self.equipment.update(self.sage_equipment)
        self.wealth['gold'] += 10