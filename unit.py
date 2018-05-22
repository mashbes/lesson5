from abc import ABCMeta, abstractmethod
from .clock import Clock
import random


import strategy
import json

class Unit (metaclass=ABCMeta):
    def __init__(self, health, recharge, experience=0):
        self.health = health
        self.recharge = recharge
        self.experience = experience
        self.alive = True


    @abstractmethod
    def attack_succeed(self, target):
        return 0.5 * (1 + self.health / 100) * random.randrange(50 + self.experience, 100) / 100

    @abstractmethod
    def make_damage(self, damage):
        damage = 0
        if self.attack_succeed():
            damage = 0.05 + self.experience / 100

    @abstractmethod
    def take_damage(self, damage):
        self.health -= damage


    @property
    @abstractmethod
    def alive(self):
        if self.health <= 0:
            self.alive = False

    @property
    @abstractmethod
    def health(self):
        pass

    @property
    @abstractmethod
    def attack_power(self):
        pass

    @property
    @abstractmethod
    def recharge(self):
        """ if recharge =0 we can attack
        if recharge not 0 attack is 0, or damage = 0

        """
        pass


