from BlockChain import CBlock
from Signature import generate_keys, sign, verify

reward = 25.0


class TxBlock(CBlock):
    transactions = []

    def __init__(self, previousBlock):
        self.previousBlock = previousBlock
        self.data = None
        self.previousHash = None
        if self.previousBlock is not None:
            self.previousHash = self.previousBlock.currentHash

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
            if self.previousHash != self.previousBlock.currentHash:
                return False
        for t in self.data:
            v = t.is_valid()
            if v is False and not (t == self.data[len(self.data) - 1] and len(t.inputs) == 0 and len(t.outputs) == 1 and t.reqd is None and len(t.sigs) == 0 and round(t.outputs[0][1]) == reward):
                return False

        return True


    def good_nonce(self):
        valid = super(TxBlock, self).is_valid()
        return valid

    def find_nonce(self):
        self.nonce = self.computeHash()
        return self.nonce
