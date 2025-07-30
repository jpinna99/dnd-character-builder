import json

with open('formatted-spell-list.json', 'r', encoding='utf-8') as master_spell_list:
    master_spell_list = json.load(master_spell_list)

cantrips = []
for spell in master_spell_list:
    if spell['level'] == 'Cantrip':
        cantrips.append(spell)

with open('formatted-cantrips-list.json', 'w') as cantrip_list:
    json.dump(cantrips, cantrip_list, indent=4)
