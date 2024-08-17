import uuid

class Escrow:
    def __init__(self, buyer, seller, item):
        self.id = str(uuid.uuid4())
        self.buyer = buyer
        self.seller = seller
        self.item = item
        self.buyer_approved = False
        self.seller_approved = False
        self.status = ""


    def get_escrow_details(self):
        escrow_details = (
            f"Escrow details:\n"
            f"   ID: {self.id}\n"
            f"   Buyer: {self.buyer.name}\n"
            f"   Seller: {self.seller.name}\n"
            f"   Item: {self.item.name}\n"
            f"   Buyer approved?: {self.buyer_approved}\n"
            f"   Seller approved?: {self.seller_approved}\n"
            f"   Escrow status: {self.status}\n"
        )

        print(escrow_details)


    def cancel(self):
        self.buyer.balance += self.item.price
        self.seller.storefront.append(self.item)
        self.buyer.escrow_accounts.pop(self.id)
        print(f"Escrow with ID: {self.id} has been cancelled.\n")


    def validate_transaction(self):
        valid = [self.status == "Active",
                 self.buyer_approved,
                 self.seller_approved,
                 self.buyer.balance >= self.item.price,
                 (self.item.id == seller_item.item.id for seller_item in self.seller.storefront)]

        return all(valid)


    def release(self):
        if self.validate_transaction():
            self.status = "Released"
            self.buyer.finalize_purchase(self)
            self.seller.receive_payment(self.item.price)
        else:
            print("Escrow cannot be released. Verify that the transaction is valid.\n")
            return None

