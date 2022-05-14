import pickle

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class CBlock:
    previousHash = None
    previousBlock = None
    currentHash = None
    data = None
    def __init__(self, data, previousBlock):
        self.data = data
        self.currentHash = self.computeHash()
        self.previousBlock = previousBlock
        if previousBlock is not None:
            self.previousHash = previousBlock.computeHash()

    def computeHash(self):
        # hash1 = str(pickle.dumps(str(self.data))) + str(self.previousHash)
        # if self.previousBlock is not None:
        #     hash1 = hash1 + str(self.previousBlock.computeHash())
        # currentHash = hash(hash1)
        hash1 = str(pickle.dumps(str(self.data)))
        if self.previousBlock is not None:
            hash1 += str(pickle.dumps(str(self.previousBlock.data)))
        return hash(hash1)