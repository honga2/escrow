import uuid

class Escrow:
    def __init__(self, buyer, seller, item):
        self.id = str(uuid.uuid4())
        self.buyer = buyer
        self.seller = seller
        self.item = item
        self.is_active = True
        self.is_disputed = False


    def get_escrow_details(self):
        escrow_details = (
            f"Escrow details:\n"
            f"   ID: {self.id}\n"
            f"   Buyer: {self.buyer.name}\n"
            f"   Seller: {self.seller.name}\n"
            f"   Item: {self.item.name}\n"
            f"   Disputed?: {self.is_disputed}\n"
            f"   Active?: {self.is_active}\n"
        )

        print(escrow_details)


    def dispute(self):
        if not self.is_disputed and self.is_active:
            self.is_disputed = True
        return True


    def resolve(self):
        self.is_disputed = False
        return True


    def cancel(self):
        if self.is_active:
            self.buyer.balance += self.item.price
            self.seller.storefront.append(self.item)
            self.is_active = False
            self.buyer.escrow_accounts.pop(self.id)
        return True


    def validate_transaction(self):
        valid = [not self.is_disputed,
                 self.is_active,
                 self.buyer.balance >= self.item.price,
                 (self.item.id == seller_item.item.id for seller_item in self.seller.storefront)]

        return all(valid)


    def release(self):
        if self.validate_transaction():
            self.is_active = False
            self.buyer.finalize_purchase(self)
            self.seller.receive_payment(self.item.price)
        else:
            print("Escrow cannot be released. Verify that the transaction is valid.\n")
            return None

