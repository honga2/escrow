from parties.user import User
from parties.escrow import Escrow

class Buyer(User):
    def __init__(self, name, balance):
        User.__init__(self, name, balance)
        self.purchased_items = []


    def get_buyer_details(self):
        items = [item.name for item in self.purchased_items]

        buyer_details = (
            f"Buyer details:\n"
            f"   Buyer: {self.name}\n"
            f"   Balance: {self.balance}\n"
            f"   Purchased items: {items}\n"
        )

        print(buyer_details)


    def choose_item(self, seller):
        if not seller.storefront:
            print("No items found in storefront.")
            return None

        for i, item in enumerate(seller.storefront, start=1):
            print(f"{i}) {item} - ${item.price} (ID: {item.id})")

        choice = int(input("Please select the item you wish to purchase by number.\n")) - 1

        if 0 < choice < len(seller.storefront):
            return seller.storefront[choice]
        else:
            return None


    def initiate_escrow(self, seller):
        item = self.choose_item(seller)

        if item:
            if self.balance < item.price:
                print("Insufficient funds.")
                return None

            escrow = Escrow(buyer=self, seller=seller, item=item)
            escrow.buyer_approved = True
            escrow.status = "Pending"
            self.balance -= item.price
            self.escrow_accounts[escrow.id] = escrow

            print(f"{self.name} has requested an escrow service (ID: {escrow.id}) for {seller.name}'s {item.name} (ID: {item.id})\n")
            return escrow

        print(f"Item not found in {seller}'s storefront.")


    def finalize_purchase(self, escrow):
        self.purchased_items.append(escrow.item)
        print(f"Purchase finalized: {escrow.item.name} (ID: {escrow.item.id}) has been added to {self.name}'s purchased items.\n")
        self.escrow_accounts.pop(escrow.id)
