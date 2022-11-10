from json import JSONEncoder, JSONDecoder, dump, loads

# define the Encoder class used in serialization
class Encoder(JSONEncoder):
    """ from a Python object we need to obtain a json representation"""

    def default(self, o: str) -> str:
        return o.__dict__


class Decoder(JSONDecoder):
    """ We have to transform the serialized string into Python objects"""

    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Order(*vals)
        return cat


class Order:
    """ define the order class which holds the orders of orders """

    def __init__(self, address, products) -> object:
        self.address = address
        self.products = products

    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        if type(other) == type(self):
            return self.address == other.address
        else:
            return False

    def __hash__(self):
        return hash(self.address)

    def __str__(self):
        return f'address = {self.address} products = {self.products}'

    def __repr__(self):
        return f'Order("{self.address}","{self.products}")'