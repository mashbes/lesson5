from random import randint


class Strategy:
    def weakest(self, target_squad):
        min_health = min([squad.health() for squad in target_squad.squads])
        weak_squad = target_squad.squads[0]
        for squad in target_squad.squads:
            if squad.health() <= min_health:
                if squad.health() > 0:
                    min_health = squad.health()
                    weak_squad = squad
        return weak_squad

    def strongest(self, target_squad):
        max_health = max([squad.health() for squad in target_squad.squads])
        strong_squad = target_squad.squads[0]
        for squad in target_squad.squads:
            if squad.health() >= max_health:
                max_health = squad.health()
                strong_squad = squad
        return strong_squad

    def random(self, target_squad):
        strategy = randint(0, 1)
        if strategy == 1:
            return self.strongest(target_squad)
        else:
            return self.weakest(target_squad)

