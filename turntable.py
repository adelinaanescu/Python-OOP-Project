from product import Product


class Turntable(Product):
    def __init__(self, name, speed, connectionType, size):
        super().__init__(name)
        self.speed = speed
        self.connectionType = connectionType
        self.size = size
    def __str__(self):
        return f'name = {self.name}, speed = {self.speed},connectionType = {self.connectionType}, size ={self.size}'

    def __repr__(self):
        return f'Receiver("{self.name}", "{self.speed}","{self.connectionType}","{self.size}")'
