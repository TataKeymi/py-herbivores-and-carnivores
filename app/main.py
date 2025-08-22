class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hiddden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hiddden
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}, Health: {self.health},"
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Herbivore) -> None:
        if not isinstance(herbivore, Carnivore) and not herbivore.hidden:
            herbivore.health -= 50
        if herbivore.health <= 0:
            Animal.alive.remove(herbivore)
