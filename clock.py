import time


class Clock:
    """
    Simulator of real time. Will be used for calculation of recharge
    """

    def __init__(self, speed=0.001):
        self.i = 0
        self.speed = speed

    def tick(self):
        self.i += 1
        time.sleep(self.speed)

    def time(self):
        return self.i
