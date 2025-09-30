from abc import ABC, abstractmethod
from RentalService import Rental


class Vehicle(ABC):
    def __init__(self, make, model, price):
        self._make = make
        self._model = model
        self._price = price

    @abstractmethod
    def calculate_premium(self):
        pass
    def __str__(self):
        return f'Vehicle details: make: {self._make}, model: {self._model}, price: {self._price}'

# Car Class
class Car(Vehicle):
    def __init__(self, make, model, price, segment='standard'):
        super().__init__(make, model, price)
        self._segment = segment

    def calculate_premium(self):
        if self._segment == 'luxury':
            return self._price * 0.025
        else:
            return self._price * 0.020
    def __str__(self):
        return super().__str__() + f' segment: {self._segment}'

# Bike Class
class Bike(Vehicle):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)

    def calculate_premium(self):
        return self._price * 0.015
    
    def __str__(self):
        return f'Bike:  {self._make}, {self._model}'

# Taxi Class
class Taxi(Car, Rental):
    def __init__(self, make, model, price, rental_id, segment='standard'):
        Car.__init__(self, make, model, price, segment)
        Rental.__init__(self, rental_id)

    def calculate_rent(self, hrs):
        if hrs <= 8:
            return hrs * 1000
        else:
            return hrs * 1000 + (hrs - 8) * 500

    def __str__(self):
        return f'Taxi: {self._rental_id}, {self._make} {self._model}'


# Bus Class here
class Bus(Rental):
    def __init__(self, make, model, price, rental_id, segment='standard'):
        # Car.__init__(self, make, model, price, segment)
        self._make=make
        self._model=model
        self._price=price
        self._segment=segment

        Rental.__init__(self, rental_id)

    def calculate_rent(self, hrs):
        if hrs <= 8:
            return hrs * 1000
        else:
            return hrs * 1000 + (hrs - 8) * 500

    def __str__(self):
        return f'Taxi: {self._rental_id}, {self._make} {self._model}'