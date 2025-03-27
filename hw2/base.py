from abc import ABC

from hw2.exceptions import LowFuelError
from hw2.exceptions import NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption, started = False):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started:
            raise ValueError("Двигатель уже запущен")
        if self.fuel <= 0:
            raise LowFuelError("Нет топлива")
        self.started = True

    def move(self, distance):
        required_fuel = (self.fuel_consumption * distance) / 100
        if required_fuel > self.fuel:
            raise NotEnoughFuel("Недостаточно топлива")
        if not self.started:
            raise ValueError("Двигатель не запущен")
        self.fuel -= required_fuel

