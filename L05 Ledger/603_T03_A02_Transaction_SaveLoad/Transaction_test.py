from Signature import generate_keys
from Transaction import Tx
import pickle

if __name__ == "__main__":

    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(mike_pbc, 1)
    Tx1.sign(alex_prv)

    if Tx1.is_valid():
        print("Success! Tx is valid")

    savefile = open("tx.dat", "wb")
    pickle.dump(Tx1, savefile)
    savefile.close()

    loadfile = open("tx.dat", "rb")
    newTx = pickle.load(loadfile)

    if newTx.is_valid():
        print("Sucess! Loaded tx is valid")
    loadfile.close()
