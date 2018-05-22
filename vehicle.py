from .unit import Unit
import random
from statistics import mean
from soldier import Soldier


class Vehicle(Unit):
    def __init__(self, clock, name, operators, recharge=random.randint(1000, 2000), veh_health):
        self.name = name
        self.clock = clock
        self.veh_health = veh_health
        self.recharge = recharge
        self.operators = []
        for operator in operators:
            self.add_operator(operator)
        self.veh_health = self.get_health()
        # self.veh_health = veh_health
        self.alive = True

    def add_operator(self, operator):
        if operator['unit type'] == Soldier:
            self.operators.append(Soldier(self.clock, operator['name'], operator['health']))

    def get_health(self):
        """sum of health operators and vehicle"""
        health = self.get_health()
        for n in self.operators:
            if n.alive:
                health += self.operators.health
                n += 1
        return health / n

    def get_damage(self):
        damage = 0
        sum_exp = 0
        for operator in self.operators:
            if operator.alive:
                sum_exp += self.operators.experience
            damage = 0.1 + sum_exp/100
        return damage

    def gavg(self):
        geo_avg = 1
        i = 0
        for operator in self.operators:
            if operator.alive:
                geo_avg *= operator.attack_succeed()
                i += 1
        return geo_avg ** (1 / i)

    def attack_succeed(self):
        return 0.5 * (1 + self.health / 100) * self.gavg()

    def take_damage(self, input_damage):
        self.veh_health -= self.veh_health * 0.6
        i = 0
        for operator in self.operators:
            if operator.alive:
                i += 1
            return i
        unlucky = random.randint(0,i)

        """
        for operator in self.operators:
            if operator != self.operators[unlucky]:
                damage_part = 0.1
            else:
                damage_part = 0.2
            return  operator.take_damage(input_damage * damage_part)
        """

        for operator in self.operators:
            if operator != self.operators[unlucky]:
                operator.health = operator.health - 0.1 * input_damage
            else:
                operator.health = operator.health - 0.2 * input_damage

    def nex_exp(self, damage_inflicted):
        for operator in self.operators:
            operator.new_exp(damage_inflicted * len(self.operators))

    @property
    def alive(self):
        if self.veh_health <= 0:
            return False

    @property
    def health(self):
        if len(self.operators) > 0:
            return mean([self.self_health] + [operator.health
                for operator in self.operators
            ])
        return 0
