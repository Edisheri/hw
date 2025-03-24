from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption, started=False):
        # Используем сеттеры при инициализации
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._weight = value

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            raise ValueError("Топливо не может быть отрицательным")
        self._fuel = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value < 0:
            raise ValueError("Расход топлива не может быть отрицательным")
        self._fuel_consumption = value

    def start(self):
        if self.started:
            raise ValueError("Двигатель уже запущен")
        if self.fuel <= 0:
            raise LowFuelError(fuel=self.fuel)  # ← Передаем значение топлива
        self.started = True

    def move(self, distance):
        required_fuel = (self.fuel_consumption * distance) / 100
        if required_fuel > self.fuel:
            raise NotEnoughFuel(required=required_fuel, available=self.fuel)  # ← Передаем данные
        if not self.started:
            raise ValueError("Двигатель не запущен")
        self.fuel -= required_fuel