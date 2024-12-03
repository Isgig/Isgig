from simpy import *
import numpy as np
import matplotlib.animation as anim
import matplotlib.pyplot as plt

class Car(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print(f"Start parking and charging at {self.env.now()}")
            charging_duration = 5
            yield self.env.timeout(charging_duration)
            print(f"Start driving at {self.env.now()}")
            driving_duration = 2
            yield self.env.timeout(driving_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

def main():
    env = Environment()
    car = Car(env)
    car.run()
    return

main()
