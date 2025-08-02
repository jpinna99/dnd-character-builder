import json

with open('formatted-master-spell-list.json', 'r', encoding='utf-8') as master_spell_list:
    master_spell_data = json.load(master_spell_list)
    warlock_spells = []
    for spell in master_spell_data:
        available_classes = spell['class']
        if 'warlock' in available_classes.lower():
            warlock_spells.append(spell)

with open('formatted-warlock-spell-list.json', 'w') as warlock_spell_list:
    json.dump(warlock_spells, warlock_spell_list, indent=4)


with open('formatted-warlock-spell-list.json') as warlock_spell_list:
    warlock_spell_data = json.load(warlock_spell_list)
    warlock_spells_level_1 = []
    for spell in warlock_spell_data:
        if spell['level'] == '1st-level':
            warlock_spells_level_1.append(spell)

with open('formatted-warlock-spell-list---level-1.json', 'w') as warlock_spell_list_level_1:
    json.dump(warlock_spells_level_1, warlock_spell_list_level_1, indent=4)
