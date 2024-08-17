from parties.item import Item

class Seller:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.storefront = []
        # self.escrow_accounts = {}


    def get_seller_details(self):
        items = [item.name for item in self.storefront]

        seller_details = (
            f"Seller details:\n"
            f"   Seller: {self.name}\n"
            f"   Balance: {self.balance}\n"
            f"   Storefront: {items}\n"
        )

        print(seller_details)


    def receive_payment(self, amount):
        self.balance += amount
        print(f"${amount} was transferred to {self.name}'s balance.\n")


    def add_item(self, name, price):
        item = Item(name=name, price=price)
        self.storefront.append(item)


    def remove_item(self, item_id):
        self.storefront.pop(item_id)
