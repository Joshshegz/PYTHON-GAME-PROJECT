 ## Avengers Game

This is a simple text-based game where users can create a profile, choose a path, and battle against a wolf. The game is written in Python and uses the `villans` module to create a wolf object.

### Prerequisites

To run this game, you will need to have Python 3 installed on your computer. You will also need to install the `villans` module using the following command:

```
pip install villans
```

### Running the Game

To run the game, simply open a terminal window and navigate to the directory where the game files are located. Then, type the following command:

```
python avengers.py
```

### Gameplay

The game begins by prompting the user to enter a username and password. The password is then confirmed to ensure that it is entered correctly. Once the password is confirmed, a player profile is created. The profile includes the following information:

* **Item:** This is the item that the player will use in battle. The item is chosen randomly from a list of four items: axe, gun, rocket launcher, and shovel.
* **Attack:** This is the player's attack strength. The attack strength is a random number between 10 and 20.
* **Defense:** This is the player's defense strength. The defense strength is a random number between 15 and 25.
* **Health:** This is the player's health points. The health points are a random number between 300 and 500.
* **Agility:** This is the player's agility. The agility is a random number between 30 and 60.

After the player profile is created, the player is prompted to choose a path: arena or forest. If the player chooses the arena, they will battle against a wolf. If the player chooses the forest, they will be prompted to join a clan.

### Battle

If the player chooses the arena, they will battle against a wolf. The wolf has the following attributes:

* **Name:** Wolf
* **Attack:** A random number between 30 and 50
* **Defense:** A random number between 10 and 20
* **Health:** A random number between 2000 and 3000
* **Agility:** A random number between 10 and 30

The battle is turn-based. On each turn,
