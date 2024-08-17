from parties.escrow import Escrow

class Buyer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.purchased_items = []
        self.escrow_accounts = {}


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
            self.balance -= item.price
            self.escrow_accounts[escrow.id] = escrow
            for _ in seller.storefront:
                if _.id == item.id:
                    seller.storefront.remove(_)

            print(f"A transaction has been initiated between {self.name} and {seller.name} for {item.name} (ID: {item.id})\n")
            return escrow

        print(f"Item not found in {seller}'s storefront.")


    def dispute_escrow(self, escrow_id):
        escrow = self.escrow_accounts.get(escrow_id)
        if escrow:
            if escrow.is_disputed:
                print("Escrow is already in dispute.\n")
                return None

            dispute = escrow.dispute()
            if dispute:
                print(f"Escrow {escrow_id} has been disputed.\n")
                return None
            else:
                print("Failed to dispute the escrow.\n")
                return None

        print("Escrow not found in active accounts.\n")


    def resolve_escrow(self, escrow_id):
        escrow = self.escrow_accounts.get(escrow_id)
        if escrow:
            resolve = escrow.resolve()
            if resolve:
                print(f"Escrow {escrow_id} has been resolved.\n")
                return None
            else:
                print("Failed to resolve the escrow.\n")
                return None


    def cancel_escrow(self, escrow_id):
        escrow = self.escrow_accounts.get(escrow_id)
        if escrow:
            cancel = escrow.cancel()
            if cancel:
                print(f"Escrow {escrow_id} has been cancelled.\n")
                return None
            else:
                print("Failed to cancel the escrow.\n")
                return None


    def finalize_purchase(self, escrow):
        self.purchased_items.append(escrow.item)
        print(f"Purchase finalized: {escrow.item.name} (ID: {escrow.item.id}) has been added to {self.name}'s purchased items.\n")
        self.escrow_accounts.pop(escrow.id)
