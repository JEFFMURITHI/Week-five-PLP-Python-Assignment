class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚤"

class Animal:
    def move(self):
        return "Walking 🐾"

# Polymorphism in action
vehicles_and_animals = [Car(), Plane(), Boat(), Animal()]

for obj in vehicles_and_animals:
    print(obj.move())
