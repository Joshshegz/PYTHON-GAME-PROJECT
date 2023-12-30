class Villans:
    def __init__(self, type, attack, defense, health, agility):
        self.type = type
        self.attack = attack
        self.defense = defense
        self.health = health
        self.agility = agility
        
    def print_animal(self):
        animal = print(f'You met a {self.type} with attack {self.attack}, defense {self.defense}, health {self.health}, agility {self.agility}')
        return animal

class Monster:
    def __init__(self, type, attack, defense, health, agility, magic):
        self. type = type
        self.attack = attack
        self.defense = defense
        self.health = health
        self.agility = agility
        self.magic = magic

    def print_monster(self):
        monster = print(f'You met a {self.type} with attack {self.attack}, defense {self.defense}, health {self.health}, agility {self.agility}, magic {self.magic}')
    
    def print_monster_goblin(self):
        goblin = print(f'You met {self.type} each with attack {self.attack}, defense {self.defense}, health {self.health}, agility {self.agility}, magic {self.magic}')
        
        return Monster


class Clan:
    def __init__(self, name, bonus_attack, bonus_defense, bonus_health, bonus_agility):
        self.name = name
        self.bonus_attack = bonus_attack
        self.bonus_defense = bonus_defense
        self.bonus_health = bonus_health
        self.bonus_agility = bonus_agility



