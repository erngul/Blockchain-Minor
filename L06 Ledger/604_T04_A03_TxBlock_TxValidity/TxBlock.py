import hashlib

from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import Tx

class TxBlock (CBlock):
    transactions = []
    def __init__(self, previousBlock = None):
        if previousBlock is not None:
            self.transactions.append(previousBlock)
            self.previousHash = previousBlock.computeHash()

    def addTx(self, Tx_in):
        if len(self.transactions) > 0:
            newCblock = CBlock(Tx_in, self.transactions[len(self.transactions)-1])
        else:
            newCblock = CBlock(Tx_in, None)
        self.transactions.append(newCblock)

    def is_valid(self):
        currentBlock = self.transactions[len(self.transactions)-1]
        while currentBlock is not None:
            test = currentBlock.computeHash()
            if currentBlock.computeHash() != currentBlock.currentHash:
                return False
            if currentBlock.previousBlock is not None:
                if currentBlock.previousBlock.computeHash() != currentBlock.previousHash:
                    return False
            currentBlock = currentBlock.previousBlock

def sha256(message):
    return hashlib.sha256(message.encode('UTF-8')).hexdigest()
