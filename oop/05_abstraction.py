from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    def description(self):
        return f"This is a {self.brand} vehicle"

class Car(Vehicle):
    def start(self):
        return "Car starting..."
    
    def stop(self):
        return "Car stopping..."

class Bike(Vehicle):
    def start(self):
        return "Bike starting..."
    
    def stop(self):
        return "Bike stopping..."