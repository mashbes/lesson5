from .unit import Unit
import random

class Soldier(Unit):
    def __init__(self, experience=0, clock, name, health, recharge=random.randint(100, 2000)):
        self.name = name
        self.experience = experience
        self._clock = clock
        self._health = health
        self.recharge = recharge
        self._next_time_attack = self._clock.time

    @property
    def alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health

    @property
    def attack_succeed(self):
        return round(0.5 * (1 + self.health / 100) * random.uniform(50 + self.experience, 100) / 100, 2)

    @property
    def can_attack_recharge(self):
        return self._next_time_attack <= self._clock.time

    def new_exp(self):
        if self.experience < 50:
            self.experience += 0.1
        return  self.experience

    def get_damage(self):
        if self.can_attack_recharge and self.alive:
            damage = 0.05 + self.experience / 100
            self._next_time_attack = self._clock.time + self.recharge
        return damage

    def take_damage(self, input_damage):
        self._health -= input_damage

