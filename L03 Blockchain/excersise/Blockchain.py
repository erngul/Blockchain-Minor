from cryptography.hazmat.primitives import hashes
import inspect
from Blockchain_t import anotherClass

class CBlock:
    previousHash = None
    previousBlock = None
    data = None
    
    def __init__(self, data, previousBlock):
        print(inspect.isclass(anotherClass))
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock is not None:
            self.previousHash = previousBlock.computeHash()

    def computeHash(self):
        print(self.data)
        if isinstance(self.data, int):
            data = str(self.data).encode()
        elif isinstance(self.data, str):
            data = self.data.encode()
        elif isinstance(self.data, (bytes, bytearray)):
            data = self.data
        elif isinstance(self.data, anotherClass):
            data = self.data.string.encode()
        digest = hashes.Hash(hashes.SHA256())
        digest.update(data)
        final = digest.finalize()
        return final