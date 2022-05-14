import hashlib


class CBlock:
    previousHash = None
    CurrentHash = None
    previousBlock = None
    data = None
    Nonce = None

    def __init__(self, data, previousBlock=None):
        self.data = data
        self.previousBlock = previousBlock
        self.CurrentHash = sha256(data)
        self.Nonce = 1
        if previousBlock is not None:
            self.previousHash = self.previousBlock.CurrentHash

    def mine(self, leading_zeros):
        prefix = '0' * leading_zeros
        if self.previousBlock is not None:
            self.previousHash = self.previousBlock.CurrentHash
        for i in range(1000000):
            self.Nonce = i
            digest = str(self.data) + str(i)
            if self.previousBlock is not None:
                digest += str(self.previousHash)
            digest = sha256(digest)
            if digest.startswith(prefix):
                self.CurrentHash = digest
                return

    def is_valid_hash(self):
        currentBlock = self
        check = True
        while currentBlock is not None:
            digest = str(currentBlock.data) + str(currentBlock.Nonce)
            if currentBlock.previousBlock is not None:
                digest += str(currentBlock.previousHash)
            newHash = sha256(digest)
            if newHash != currentBlock.CurrentHash:
                check = False
            currentBlock = currentBlock.previousBlock
        return check


def sha256(message):
    return hashlib.sha256(message.encode('UTF-8')).hexdigest()
