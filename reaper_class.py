from character_class import Character

class Reaper(Character):
    def __init__(self, name):
        super().__init__(name)
        self.shadow_armor = {
            'name': 'shadow armor',
            'level': 1,
            'description': """At 1st level, you are protected by the Reaper's shadows. Shadows swirl around you whenever you are in danger, allowing you to mitigate some harm. When hit by an attack, you may use your reaction to give you resistance to the damage for the triggering attack. You may do this a number of times equal to your Charisma modifier before taking a long rest""",
            'action type': '1 reaction',
            'effect': 'resistance to damage for triggering attack',
            'number of uses': 'number up to Charisma modifier',
            'number of uses remaining': 0
        }
        self.reapers_blade = {
            'name': "reaper's blade",
            'level': 1,
            'description': """At 1st level, the Reaper gives you access to one of their weapons, the Reaper's Blade. As an action, you may summon the Reaper's blade to your side. It shares the same space as you, hovering near your back, and takes the appearance of your choice although typically a scythe. When in your space, the blade moves with you. The blade lasts for 1 minute before returning to your patron. You may use a bonus action to move the blade up to 20ft away, up to maximum of 50ft from you. As part of that same bonus action, you may have the Blade attack a target within 10ft of it. Make a melee spell attack against the target and on a hit, deal 1d8 Necrotic damage (increases at levels 6 and 14). If the scythe enters an anti-magic field, it falls to the ground and assumes the properties of the weapon you created it as until leaves the field. If targeted by dispel magic, it disappears back to your Patron and must be summoned again. You may summon the blade a number of times equal to your Charisma modifier between long rests.""",
            'higher levels': 'At 6th level, the damage increases to 2d8 and at 14th level it becomes 3d8',
            'action type': {'1 action': 'summons the blade to your side',
                            '1 bonus action': 'move up to 20ft and attack'},
            'number of uses': 'number up to Charisma modifier',
            'number of uses remaining': 0
        }
        self.dark_tear = {
            "name": 'dark tear',
            'level': 6,
            "description": "At 6th Level you may tear open a hole in time and space, allowing you safe passage to another location. As an action, you may use the Reaper's dark hold on time to carve a tear in time and space within 15 ft. of you. This tear will allow you to travel through it to another location you can see within 500 feet instantaneously, as reality folds to accommodate you. The tear remains open for 1 minute, or until you lose/drop concentration. Others may attempt to pass through the tear, making a Wisdom saving throw against your spell save DC. On a failed save, they take 2d6 Necrotic damage and are knocked prone on the other side of the tear. On a successful save, they teleport to an unoccupied space within 5 feet of your exit location. The tear can not teleport you into an anti-magic field and can be destroyed by dispel magic. Once you use this ability, you can not do so again until after a short or long rest.",
            'action type': '1 action',
            'concentration': True,
            'number of uses': 'once per short or long rest',
        }
        self.reapers_reach = {
            "name": "reaper's reach",
            "level": 10,
            "description": """At 10th Level, your connection to your patron allows you better use of their instrument. You may now cast spells through your Reaper's Blade when it is away from you, as if you were standing in the spot it is in. You may now also move the Blade up to a maximum of 80 ft. away from you now, and call it back to your side as an action."""

        }
        self.angel_of_death = {
            "name": "angel of death",
            "level": 14,
            "description": """At 14th level, your connection to the Reaper has reached its pinnacle. When you summon your Reaper's Blade, you may choose to summon the Reaper's Avatar, a spectral floating figure garbed in shadows, along with it. You spend an additional charge of your Reaper's Blade to summon the avatar. The Reaper's Avatar takes up the Reaper's Blade and acts on your turn. It can move 30 ft on your turn and make two weapon attacks using the Reaper's Blade and uses your melee spell attack. It does not have a limit to how far it can go, but still can only remain on this plane for 1 minute before returning. The Avatar has an AC of 17 and an HP of 5 times your charisma score. If targeted by dispel magic, it will not disappear but instead will be stunned for 1 round. It will not enter an anti-magic field even if commanded to and will use its reaction to teleport to a safe distance if one is generated near it. After you summon the Avatar and he is dismissed, destroyed, or expires, you cannot summon him again until you take a long rest.""",
            "number of uses": 'once per long rest',
            "action type": "1 action, 2 charges of Reaper's Blade",
            "avatar abilities": {"speed": 30,
                                 "attacks": 2,
                                 "armor class": 17,
                                 "HP": "5 x my Charisma score"}
        }
    def get_charisma_modifier(self):
        return self.ability_scores['charisma']['modifier']
    
    def set_charisma_charges(self):
        self.shadow_armor['number of uses remaining'] = self.get_charisma_modifier()
        self.reapers_blade['number of uses remaining'] = self.get_charisma_modifier()

    def use_shadow_armor(self):
        if self.shadow_armor['number of uses remaining'] == 0:
            print("You have no more uses left. Must take long rest.")
        else:
            self.shadow_armor['number of uses remaining'] -= 1

    def use_reapers_blade(self):
        if self.reapers_blade['number of uses remaining'] == 0:
            print("You have no more uses left. Must take long rest.")
        else:
            self.reapers_blade['number of uses remaining'] -= 1
