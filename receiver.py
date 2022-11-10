from product import Product


class Receiver(Product):
    def __init__(self, name, color, numberChannels, size):
        super().__init__(name)
        self.power = color
        self.numberChannels = numberChannels
        self.size = size

    def __str__(self):
        return f'name = {self.name}, color = {self.color},numberChannels = {self.numberChannels}, size ={self.size}'

    def __repr__(self):
        return f'Receiver("{self.name}", "{self.color}","{self.numberChannels}","{self.size}")'
