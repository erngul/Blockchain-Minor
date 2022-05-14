from BlockChain import CBlock
from Signature import generate_keys, sign, verify

reward = 25.0


class TxBlock (CBlock):
    transactions = []

    def __init__(self, previousBlock):
        self.previousBlock = previousBlock
        self.data = None
        if self.previousBlock is not None:
            self.previousHash = self.previousBlock.computeHash()

    def addTx(self, Tx_in):
        self.transactions.append(Tx_in)
        if self.data is None:
            self.data = []
        self.data.append(Tx_in)
        self.currentHash = self.computeHash()

    def is_valid(self):
        if self.currentHash != self.computeHash():
            return False
        if self.previousHash is not None:
            if self.previousHash != self.previousBlock.computeHash():
                return False
        for t in self.data:
            v = t.is_valid()
            if v is False:
                return False
        return True


    def good_nonce(self):
        pass

    def find_nonce(self):
        pass
