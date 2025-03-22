"""
создайте класс `Car`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.engine import Engine

class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, started = False, engine = None):
        super().__init__(weight, fuel, fuel_consumption, started)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine



