from villans import Villans
import hashlib
from random import randint, choice
print('Welcome to Avengers')

# authentication
username = input('Enter a username: ')
password = input('Enter a password: ')
confirm_pass = input('Confirm the password above: ')

# password validation
while password != confirm_pass:
    print('Passwords do not match, enter passwords again')
    # Enter passwords
    password = input('Enter a password: ')
    confirm_pass = input('Confirm the password above: ')
    if password == confirm_pass:
        break
encoded_pass = hashlib.md5(password.encode())


# Profile creation
class Player:
    def __init__(self, item, attack, defense, health, agility):
        self.item = item
        self.attack = attack
        self.defense = defense
        self.health = health
        self.agility = agility
    
    def print_player(self):
        player = print(f'''
        Profile has been successfully created
        Item chosen by system is {self.item}
        name = {username}
        attack = {self.attack}
        defense = {self.defense}
        health = {self.health}
        agility = {self.agility}
        ''')
        return player
items = ['axe', 'gun', 'rocket_launcher', 'shovel']
chosen_item = choice(items)
created_player = Player(chosen_item, randint(10, 20), randint(15, 25), randint(300, 500), randint(30, 60))
created_player.print_player()

print('Do you want to go to arena or Forest')
path = input('Choose a path: ').upper()
if path == 'ARENA':
    wolf = Villans('wolf', randint(30, 50), randint(10, 20), randint(2000, 3000), randint(10, 30))
    wolf.print_animal()
    while wolf.health > 0:
        wolf.health -= choice(range(1, created_player.attack))
        print(f' Wolf {wolf.health}')
        created_player.health -= choice(range(1, wolf.attack))
        print(f'Player {created_player.health}')
        if created_player.health <= 0:
            print('Sorry you died, End of game')
            break
        else:
            print('You defeated the wolf and some items got dropped')
            print('Wolf dropped paladin\'s helmet and goblin boots')
    Exp = 250
    paladins_helmet = 10
    goblin_boots = 15
    created_player.defense += paladins_helmet
    created_player.agility += goblin_boots
    created_player.health += goblin_boots
    print(created_player.print_player())

elif path == 'Forest':
    print("Pls join a clan to continue")