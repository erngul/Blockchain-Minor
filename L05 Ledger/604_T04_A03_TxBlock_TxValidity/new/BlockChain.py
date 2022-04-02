import pickle



class CBlock:
    previousHash = None
    currentHash = None
    previousBlock = None
    data = None

    def computeHash(self):
        hash1 = str(pickle.dumps(self.data))
        if self.previousHash is not None:
            hash1 = hash1 + str(self.previousHash)
        return hash(hash1)