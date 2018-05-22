from random import randint


class Strategy:
    def weakest(self, ):
    pass


    def strongest(self):
    pass


    def random(self, target_squad):
        strategy = randint(0, 1)
        if strategy == 1:
            return self.strongest(target_squad)
        else:
            return self.weakest(target_squad)

