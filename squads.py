from unit import Unit
from soldier import Soldier
from vehicle import Vehicle


class Squad(Unit):
    def __init__(self, name, clock, units):
        self.name = name
        self._clock = clock
        self.units = []
        for unit in units:
            self.add_unit(unit)

    def add_unit(self, unit):
        if unit['unit_type'] == 'Soldier':
            self.units.append(Soldier(self._clock, unit['name'], unit['health']))
        elif unit['unit_type'] == 'Vehicle':
            self.units.append(Vehicle(self._clock, unit['name'], unit['health'], unit['operators']))

    def take_damage(self, input_damage):
        for unit in self.units:
            unit.take_damage((input_damage / len(self.units)))

    def get_damage(self, damage):
        damage = 0
        for unit in self.units:
            if unit.alive:
                damage += unit.get_damage()
        return damage

    @property
    def health(self):
        if len(self.units) > 0:
            return sum([unit.health for unit in self.units])
        return 0

    @property
    def alive(self):
        return sum([unit.alive for unit in self.units]) > 0
