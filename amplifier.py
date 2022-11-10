from product import Product


class Amplifier(Product):
    def __init__(self, name, power, numberChannels, size):
        super().__init__(name)
        self.power = power
        self.numberChannels = numberChannels
        self.size = size
    def __str__(self):
        return f'name = {self.name}, power = {self.power},numberChannels = {self.numberChannels}, size ={self.size}'

    def __repr__(self):
        return f'Receiver("{self.name}", "{self.power}","{self.numberChannels}","{self.size}")'
