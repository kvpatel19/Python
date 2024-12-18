from abc import ABC
class vehicle(ABC):
    def no_of_wheels(self):
        pass
class bike(vehicle):
    def no_of_wheels(self):
        print("bike have 2 wheels")
class tempo(vehicle):
    def no_of_wheels(self):
        print("tempo have 3 wheels")
class truck(vehicle):
    def no_of_wheels(self):
        print("truck have 4 wheels")
bike=bike()
bike.no_of_wheels()
tempo=tempo()
tempo.no_of_wheels()
truck=truck()
truck.no_of_wheels()
