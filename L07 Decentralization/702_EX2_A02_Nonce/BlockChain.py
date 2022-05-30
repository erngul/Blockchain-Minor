import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class CBlock:

    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        self.currentHash = None
        pass

    def computeHash(self):
        prefixZeros = 6
        prefix = '0' * prefixZeros
        if self.previousBlock is not None:
            self.previousHash = self.previousBlock.currentHash
        for i in range(100000000):
            self.Nonce = i
            digest = str(self.data) + str(i)
            if self.previousBlock is not None:
                digest += str(self.previousHash)
            digest = sha256(digest)
            if digest is not None and digest.startswith(prefix) and ord(digest[prefixZeros]) > 48 and  ord(digest[prefixZeros]) < 60:
                print(digest)
                self.currentHash = digest
                return self.Nonce

    def is_valid(self):
        currentBlock = self
        check = True
        while currentBlock is not None:
            digest = str(currentBlock.data) + str(currentBlock.Nonce)
            if currentBlock.previousBlock is not None:
                digest += str(currentBlock.previousHash)
            newHash = sha256(digest)
            if newHash != currentBlock.currentHash:
                check = False
            currentBlock = currentBlock.previousBlock
        return check


def sha256(message):
    return hashlib.sha256(message.encode('UTF-8')).hexdigest()
