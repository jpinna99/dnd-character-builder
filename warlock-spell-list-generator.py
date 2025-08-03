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
    warlock_spells_level_2 = []
    for spell in warlock_spell_data:
        if "2" in spell['level']:
            warlock_spells_level_2.append(spell)
    warlock_spells_level_3 = []
    for spell in warlock_spell_data:
        if "3" in spell['level']:
            warlock_spells_level_3.append(spell)   
    warlock_spells_level_4 = []
    for spell in warlock_spell_data:
        if "4" in spell['level']:
            warlock_spells_level_4.append(spell)  
    warlock_spells_level_5 = []
    for spell in warlock_spell_data:
        if "5" in spell['level']:
            warlock_spells_level_5.append(spell)  
    warlock_spells_level_6 = []
    for spell in warlock_spell_data:
        if "6" in spell['level']:
            warlock_spells_level_6.append(spell)  
    warlock_spells_level_7 = []
    for spell in warlock_spell_data:
        if "7" in spell['level']:
            warlock_spells_level_7.append(spell)  
    warlock_spells_level_8 = []
    for spell in warlock_spell_data:
        if "8" in spell['level']:
            warlock_spells_level_8.append(spell)  
    warlock_spells_level_9 = []
    for spell in warlock_spell_data:
        if "9" in spell['level']:
            warlock_spells_level_9.append(spell)  


with open('formatted-warlock-spell-list---level-1.json', 'w') as warlock_spell_list_level_1:
    json.dump(warlock_spells_level_1, warlock_spell_list_level_1, indent=4)

with open('formatted-warlock-spell-list---level-2.json', 'w') as warlock_spell_list_level_2:
    json.dump(warlock_spells_level_2, warlock_spell_list_level_2, indent=4)

with open('formatted-warlock-spell-list---level-3.json', 'w') as warlock_spell_list_level_3:
    json.dump(warlock_spells_level_3, warlock_spell_list_level_3, indent=4)

with open('formatted-warlock-spell-list---level-4.json', 'w') as warlock_spell_list_level_4:
    json.dump(warlock_spells_level_4, warlock_spell_list_level_4, indent=4)

with open('formatted-warlock-spell-list---level-5.json', 'w') as warlock_spell_list_level_5:
    json.dump(warlock_spells_level_5, warlock_spell_list_level_5, indent=4)

with open('formatted-warlock-spell-list---level-6.json', 'w') as warlock_spell_list_level_6:
    json.dump(warlock_spells_level_6, warlock_spell_list_level_6, indent=4)

with open('formatted-warlock-spell-list---level-7.json', 'w') as warlock_spell_list_level_7:
    json.dump(warlock_spells_level_7, warlock_spell_list_level_7, indent=4)

with open('formatted-warlock-spell-list---level-8.json', 'w') as warlock_spell_list_level_8:
    json.dump(warlock_spells_level_8, warlock_spell_list_level_8, indent=4)

with open('formatted-warlock-spell-list---level-9.json', 'w') as warlock_spell_list_level_9:
    json.dump(warlock_spells_level_9, warlock_spell_list_level_9, indent=4)