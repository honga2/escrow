import unittest
from unittest.mock import patch
import sys
sys.path.append('/Users/andrewh/projects/escrow/src')
from parties.buyer import Buyer
from parties.seller import Seller


class TestEscrow(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_release(self, mock_input):
        buyer = Buyer(name="Bob", balance=1000)
        seller = Seller(name="Alice", balance=0)
        seller.add_item(name="Laptop", price=500)

        buyer.get_buyer_details()
        seller.get_seller_details()

        with patch.object(buyer, "choose_item", return_value=seller.storefront[0]):
            escrow = buyer.initiate_escrow(seller)
            escrow.get_escrow_details()
            if escrow:
                buyer.dispute_escrow(escrow.id)
                escrow.get_escrow_details()
                buyer.cancel_escrow(escrow.id)

        buyer.get_buyer_details()
        seller.get_seller_details()


if __name__ == '__main__':
    unittest.main()

