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
        self.CurrentHash = self.sha256(data)
        self.Nonce = 1
        if previousBlock is not None:
            self.previousHash = self.previousBlock.CurrentHash


    def sha256(self, message):
        return hashlib.sha256(message.encode('UTF-8')).hexdigest()

    def mine(self, leading_zeros):
        prefix = '0' * leading_zeros
        if self.previousBlock is not None:
            self.previousHash = self.previousBlock.CurrentHash
        for i in range(1000000):
            self.Nonce = i
            digest = str(self.data) + str(i)
            if self.previousBlock is not None:
                digest += str(self.previousHash)
            digest = self.sha256(digest)
            if digest.startswith(prefix):
                self.CurrentHash = digest
                return

    def is_valid_hash(self):
        digest = str(self.data) + str(self.Nonce)
        if self.previousBlock is not None:
            digest += str(self.previousHash)
        newHash = self.sha256(digest)
        if  newHash == self.CurrentHash:
            return True
        return False