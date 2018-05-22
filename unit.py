from abc import ABCMeta, abstractmethod


class Unit (metaclass=ABCMeta):

    @abstractmethod
    def attack_succeed(self):
        pass

    @abstractmethod
    def get_damage(self, damage):
        pass

    @abstractmethod
    def take_damage(self, input_damage):
        pass

    @property
    @abstractmethod
    def alive(self):
        pass

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
    def can_attack_recharge(self):
        pass

    @property
    @abstractmethod
    def new_exp(self):
        pass
