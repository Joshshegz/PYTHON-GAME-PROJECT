from villans import Clan
from villans import Monster
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
# ... (your existing code)

elif path == 'FOREST':
    print("Welcome to the Forest! Choose a clan to join:")
    print("1. Warriors")
    print("2. Sorcerers")
    print("3. Rangers")
    clan_choice = input('Enter the numerical value of the clan you want to join: ')

    if clan_choice == '1':
        chosen_clan = Clan('Warriors', 5, 3, 10, 5)
    elif clan_choice == '2':
        chosen_clan = Clan('Sorcerers', 8, 1, 5, 15)
    elif clan_choice == '3':
        chosen_clan = Clan('Rangers', 7, 5, 8, 10)
    else:
        print('Invalid choice. You enter the forest without joining a clan.')
        chosen_clan = None

    if chosen_clan:
        created_player.clan = chosen_clan
        # Apply clan bonuses to the player
        created_player.attack += chosen_clan.bonus_attack
        created_player.defense += chosen_clan.bonus_defense
        created_player.health += chosen_clan.bonus_health
        created_player.agility += chosen_clan.bonus_agility

        print(f"You have joined the {chosen_clan.name} clan!")
        print(created_player.print_player())
    else:
        print("You decide to venture into the forest without joining a clan")
print("insdie the forst, you see a dungeon and a narrow path")
path2 = input("where do u want to go?")
if path2 == 'dungeon':
    print(f'{username} you have decided to enter the dungeon')
    Goblin_1 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
    Goblin_2 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
    Goblin_3 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
    Goblin_4 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
    Goblin_5 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
    Goblin_6 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
    Goblin_1.print_monster_goblin()

    while Goblin_1.health and Goblin_2.health and Goblin_3.health and Goblin_4.health and Goblin_5.health and Goblin_6.health > 0:
        Goblin_1.health -= choice(range(1, created_player.attack))
        print(f'{Goblin_1.health}')
        created_player.health -= choice(range(1, Goblin_1.attack))
        Goblin_2.health -= choice(range(1, created_player.attack))
        print(f'{Goblin_2.health}')
        created_player.health -= choice(range(1, Goblin_2.attack))
        Goblin_3.health -= choice(range(1, created_player.attack))
        print(f'{Goblin_3.health}')
        created_player.health -= choice(range(1, Goblin_3.attack))
        Goblin_4.health -= choice(range(1, created_player.attack))
        print(f'{Goblin_4.health}')
        created_player.health -= choice(range(1, Goblin_4.attack))
        Goblin_5.health -= choice(range(1, created_player.attack))
        print(f'{Goblin_5.health}')
        created_player.health -= choice(range(1, Goblin_5.attack))
        Goblin_6.health -= choice(range(1, created_player.attack))
        print(f'{Goblin_6.health}')
        created_player.health -= choice(range(1, Goblin_6.attack))
        if created_player.health < Goblin_1.health + Goblin_2.health + Goblin_3.health + Goblin_4.health + Goblin_5.health + Goblin_6.health:
            created_player.health += health_potion
            print(f'Player {created_player.health}')
        if created_player.health <= 0:
            print('Sorry you died, End of game')
            break
    print('You defeated the Goblins and no   items got dropped')
else:
    print("You passed  the normal way and you fell while all your way")
    print('You tried', username, 'Try again next time')
    print('Re-run this program to try again>>>>')
