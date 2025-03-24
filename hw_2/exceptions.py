class LowFuelError(Exception):
    def __init__(self, fuel=0, message="Недостаточный уровень топлива"):
        self.fuel = fuel
        self.message = f"{message} (Топливо: {fuel} л)"
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    def __init__(self, required=0, available=0):
        self.required = required
        self.available = available
        self.message = f"Недостаточно топлива! Требуется: {required} л, доступно: {available} л"
        super().__init__(self.message)

class CargoOverload(Exception):
    def __init__(self, current=0, max_cargo=0):
        self.current = current
        self.max_cargo = max_cargo
        self.message = f"Перегруз! Текущий груз: {current} кг, максимум: {max_cargo} кг"
        super().__init__(self.message)