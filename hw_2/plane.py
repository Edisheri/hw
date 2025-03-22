"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_2 import exceptions
from hw_2.base import Vehicle


class Plane(Vehicle):

    def __init__(self, weight, max_cargo, fuel, fuel_consumption, started = False, cargo = 0):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        expected_cargo = self.cargo + cargo
        if expected_cargo > self.max_cargo:
            raise exceptions.CargoOverload(expected_cargo, self.max_cargo)
        self.cargo += cargo
        return self

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo
