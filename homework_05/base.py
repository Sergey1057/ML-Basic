"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        needed_fuel = distance * self.fuel_consumption
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel
        else:
            raise NotEnoughFuel
