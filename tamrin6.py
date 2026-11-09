import random

class GameCharacter:
    def __init__(self, name, health, defense, attack_power):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack_power = attack_power

    def attack(self, character):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} حمله کرد")

        character.defend(damage)

    def defend(self, damage):
        damage = max(0, damage - self.defense)
        self.health -= damage

        print(f"{self.name} آسیب دید: {damage}")

        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def show_status(self):
        print(f"نام: {self.name}")
        print(f"سلامتی: {self.health}")


character1 = GameCharacter("Warrior", 100, 10, 25)
character2 = GameCharacter("Knight", 120, 15, 20)

while character1.is_alive() and character2.is_alive():

    character1.attack(character2)
    character2.show_status()

    if character2.is_alive():
        character2.attack(character1)
        character1.show_status()


with open("game_result.txt", "w", encoding="utf-8") as file:

    if character1.is_alive():
        result = f"برنده: {character1.name}"
    else:
        result = f"برنده: {character2.name}"

    file.write(result)

print(result)