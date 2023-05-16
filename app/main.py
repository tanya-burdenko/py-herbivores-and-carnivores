from __future__ import annotations
from typing import Union


class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}, " \
               f"Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Union[Herbivore, Carnivore]) -> None:
        if not animal.hidden\
                and not isinstance(animal, Carnivore) \
                and animal.health > 0:
            animal.health -= 50
        if animal.health <= 0:
            cls.alive.remove(animal)
