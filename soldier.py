from .unit import Unit
import random

class Soldier(Unit):
    def __init__(self, experience=0, clock, name, health, recharge=random.randint(100, 2000)):
        self.name = name
        self.experience = experience
        self._clock = clock
        self._health = health
        self.recharge = recharge

    @property
    def alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health

    @property
    def attack_succeed(self):
        return round(0.5 * (1 + self.health / 100) * random.uniform(50 + self.experience, 100) / 100, 2)