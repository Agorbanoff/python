import random

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def healing(self):
        number = random.randint(1, 4)
        self.health = min(self.health + number, 20)  # Cap health at 20
        print(f"{self.name} gained {number} health points! (Health: {self.health})")

    def attack(self, opponent):
        number = random.randint(2, 5)
        chance = random.randint(1, 5)
        if chance > 1:
            opponent.health -= number
            opponent.health = max(opponent.health, 0)  # Ensure health is non-negative
            print(f"{self.name} dealt {number} damage to {opponent.name}!")
        else:
            print(f"{opponent.name} blocked the attack!")

    def display_health(self):
        print(f"{self.name} has {self.health} health points remaining.")

# Input player names
player1_name = input("Enter name for your first character \n")
player2_name = input("Enter name for your second character \n")

character1 = Player(player1_name, 20)
character2 = Player(player2_name, 20)

# Game loop
while character1.health > 0 or character2.health > 0:
    print("Choose an option for player 1")
    print("1 => Heal yourself")
    print("2 => Deal damage")

    try:
        choice1 = int(input())
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice1 == 1:
        if character1.health >= 20:
            print("Your health is already full. Do you want to attack instead? (yes/no)")
            if input().lower() == "yes":
                character1.attack(character2)
        else:
            character1.healing()
    elif choice1 == 2:
        character1.attack(character2)
    else:
        print("Invalid option!")

    if character2.health <= 0:
        print(f"{character2.name} has been defeated!")
        break

    print("Choose an option for player 2")
    print("1 => Heal yourself")
    print("2 => Deal damage")

    try:
        choice2 = int(input())
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice2 == 1:
        if character2.health >= 20:
            print("Your health is already full. Do you want to attack instead? (yes/no)")
            if input().lower() == "yes":
                character2.attack(character1)
        else:
            character2.healing()
    elif choice2 == 2:
        character2.attack(character1)
    else:
        print("Invalid option!")

    if character1.health <= 0:
        print(f"{character1.name} has been defeated!")