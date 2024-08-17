
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.escrow_accounts = {}


    def dispute_escrow(self, escrow_id):
        escrow = self.escrow_accounts.get(escrow_id)
        if escrow:
            escrow.status = "Disputed"
            print(f"Escrow with ID: {escrow_id} has been disputed.\n")
            return None

        print(f"Escrow with ID: {escrow_id} was not found in active accounts.\n")


    def resolve_escrow(self, escrow_id):
        escrow = self.escrow_accounts.get(escrow_id)
        if escrow:
            escrow.status = "Active"
            print(f"Escrow with ID: {escrow_id} has been resolved.\n")
            return None

        print(f"Escrow with ID: {escrow_id} was not found in active accounts.\n")


    def cancel_escrow(self, escrow_id):
        escrow = self.escrow_accounts.get(escrow_id)
        if escrow:
            escrow.status = "Cancelled"
            escrow.cancel()
            return None

        print(f"Escrow with ID: {escrow_id} was not found in active accounts.\n")
