"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """Не хватает топлива"""


class NotEnoughFuel(Exception):
    """топлива недостаточно для преодоления переданной дистанции ."""


class CargoOverload(Exception):
    """Перегруз"""
