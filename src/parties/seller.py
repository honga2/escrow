from parties.user import User
from parties.item import Item

class Seller(User):
    def __init__(self, name, balance):
        User.__init__(self, name, balance)
        self.storefront = []


    def get_seller_details(self):
        items = [item.name for item in self.storefront]

        seller_details = (
            f"Seller details:\n"
            f"   Seller: {self.name}\n"
            f"   Balance: {self.balance}\n"
            f"   Storefront: {items}\n"
        )

        print(seller_details)


    def approve_escrow(self, escrow):
        escrow.seller_approved = True
        escrow.status = "Active"
        for _ in self.storefront:
            if _.id == escrow.item.id:
                self.storefront.remove(_)

        print(f"{self.name} has approved the escrow service (ID: {escrow.id}) for {escrow.item.name} (ID: {escrow.item.id})\n")
        return None


    def receive_payment(self, amount):
        self.balance += amount
        print(f"${amount} was transferred to {self.name}'s balance.\n")


    def add_item(self, name, price):
        item = Item(name=name, price=price)
        self.storefront.append(item)
