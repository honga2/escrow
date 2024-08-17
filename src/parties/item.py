import uuid

class Item:
    def __init__(self, name, price):
        self.id=str(uuid.uuid4())
        self.name = name
        self.price = price
