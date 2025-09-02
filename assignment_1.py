# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery   # encapsulated (private) attribute

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def check_battery(self):
        return f"Battery level: {self.__battery}%"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged to {self.__battery}%"

# Inherited class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu):
        super().__init__(brand, model, battery)
        self.gpu = gpu

    # Polymorphism: redefining behavior
    def call(self, number):
        return f"Gaming phone {self.model} is video calling {number} with GPU boost 🎮"

    def play_game(self, game):
        return f"Playing {game} on {self.model} with {self.gpu} GPU!"
    

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 80)
phone2 = GamingPhone("Asus", "ROG 7", 50, "Adreno 740")

print(phone1.call("0712345678"))
print(phone1.check_battery())
print(phone1.charge(15))

print(phone2.call("0798765432"))
print(phone2.play_game("PUBG"))
