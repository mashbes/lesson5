import random
import numpy as np
from math import sqrt

class Strategy:

class Army:
    def __init__(self, name, strategy, ):


class Unit:
    def __init__(self, hp=100, recharge=0, active):
        self.hp = hp
        self.recharge = recharge
        self.active = True

    def recharge_time(self):
        self.recharge = random.randint(100, 2000)

class Soldier(Unit):
    def characteristic(self):
        self.experience = 0

    def get_hp(self):
        return self.hp

    def set_hp(self):
        """
        if we have some damage - set new value of hp
        """
        self.hp = self.hp - damage

    def health_tracker(self):
        if self.hp <= 0:
            self.active = False

    def attack_succeed(self):
        return 0.5 * (1 + self.hp / 100) * random.randrange(50 + self.experience, 100) / 100

    def make_damage(self, damage):
        damage = 0
        if self.attack_succeed():
            damage = 0.05 + self.experience / 100



class Vehicle(Unit):
    def characteristic(self, operators):
        self.operators = random.randint(1,3)
        self.

    def get_hp(self):
        """sum of health operators and vehicle"""

        for n in self.operators:
            if n.alive:
                vehicle_hp =


        return self.hp

    def gavg(self):
        start = 1
        i = 0
        for i in self.operators:
            if i.alive:
                start *= i.attack_succeed()
                i += 1
        return start ** (1 / i)

    def attack_succeed(self):
        return 0.5 * (1 + self.hp / 100) * self.gavg()

class Squards(Unit, Vehicle):
    def characteristic(self, soldier_number, vehicle_number):
        self.soldier_number = soldier_number
        self.vehicle_number = vehicle_number


