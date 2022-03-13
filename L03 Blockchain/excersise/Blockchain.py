from cryptography.hazmat.primitives import hashes
import inspect

class CBlock:
    previousHash = None
    previousBlock = None
    data = None
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock is not None:
            self.previousHash = previousBlock.computeHash()

    def computeHash(self):
        global hash1
        try:
            hash1 = (str(self.data.string) + str(self.data.num))
        except:
            hash1 = str(self.data)
        if self.previousHash is not None:
            hash1 = hash1 + str(self.previousBlock.computeHash())
        return hash(hash1)