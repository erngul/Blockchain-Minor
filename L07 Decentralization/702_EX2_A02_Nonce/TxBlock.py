from BlockChain import CBlock
from Signature import generate_keys, sign, verify

reward = 25.0


class TxBlock (CBlock):

    def __init__(self, previousBlock):
        pass

    def addTx(self, Tx_in):
        pass

    def __count_totals(self):
        pass

    def is_valid(self):
        pass

    def good_nonce(self):
        pass

    def find_nonce(self):
        pass
