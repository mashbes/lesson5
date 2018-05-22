from squads import Squad
from unit import Unit

class Army(Unit):
    def __init__(self, name, clock, strategy, squads):
        self.name = name
        self._clock = clock
        self.strategy = strategy
        self.alive = True
        self.squads = []
        for squad in squads:
            self.add_unit(squad)

    def add_unit(self, squad):
        self.squads.append(Squad(self._clock, squad['name'], self.strategy, squad['units']))

    def select_strategy(self, strategy, target):
        if self.strategy == 'weakest':
            return strategy.weakest_strategy(target)
        elif self.strategy == 'strongest':
            return strategy.strongest_strategy(target)
        elif self.strategy == 'random':
            return strategy.random_strategy(target)

    @property
    def health(self):
        return sum([squad.health for squad in self.squads])

    @property
    def alive(self):
        return sum([squad.alive for squad in self.squads]) > 0
