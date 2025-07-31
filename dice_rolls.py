import random

def roll_d20():
    roll = random.randint(1, 20)
    print(f'd20 roll: {roll}')
    return roll

def roll_d20_with_adv():
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    higher_roll = max(roll1, roll2)
    print(f'd20 roll with advantage: {roll1}, {roll2} --- Higher roll: {higher_roll}')
    return higher_roll

def roll_d20_with_disadv():
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    lower_roll = min(roll1, roll2)
    print(f'd20 roll with disadvantage: {roll1}, {roll2} --- Lower roll: {lower_roll}')
    return lower_roll

def roll_d12():
    roll = random.randint(1, 12)
    print(f'd12 roll: {roll}')    
    return roll

def roll_d10():
    roll = random.randint(1, 10)
    print(f'd10 roll: {roll}')    
    return roll

def roll_d8():
    roll = random.randint(1, 8)
    print(f'd8 roll: {roll}')    
    return roll

def roll_d6():
    roll = random.randint(1, 6)
    print(f'd6 roll: {roll}')    
    return roll

def roll_d4():
    roll = random.randint(1, 4)
    print(f'd4 roll: {roll}')    
    return roll