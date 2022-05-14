from BlockChain import CBlock
from Signature import generate_keys, sign, verify
import pickle
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import time


from Transaction import Tx
from TxBlock import *       

if __name__ == "__main__":
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

    # Valid Blocks
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(rose_pbc, 1)
    Tx1.sign(alex_prv)

    Tx2 = Tx()
    Tx2.add_input(mike_pbc,1.1)
    Tx2.add_output(rose_pbc, 1)
    Tx2.sign(mike_prv)

    root = TxBlock(None)
    root.addTx(Tx1)
    root.addTx(Tx2)

    Tx3 = Tx()
    Tx3.add_input(rose_pbc,1.1)
    Tx3.add_output(alex_pbc, 1)
    Tx3.sign(rose_prv)
    
    Tx4 = Tx()
    Tx4.add_input(mike_pbc,1)
    Tx4.add_output(mara_pbc, 1)
    Tx4.add_reqd(rose_pbc)
    Tx4.sign(mike_prv)
    Tx4.sign(rose_prv)

    B1 = TxBlock(root)
    B1.addTx(Tx3)
    B1.addTx(Tx4)

# -------------------------------------------------
    start = time.time()
    print(B1.find_nonce())
    elapsed = time.time() - start
    print("elapsed time: " + str(elapsed) + " s.")
    if elapsed < 60:
        print("ERROR! Mining is too fast")
    if B1.good_nonce():
        print("Success! Nonce is good!")
    else:
        print("ERROR! Bad nonce")
# -------------------------------------------------


    savefile = open("block.dat", "wb")
    pickle.dump(B1, savefile)
    savefile.close()

    loadfile = open("block.dat" ,"rb")
    load_B1 = pickle.load(loadfile)
    loadfile.close()

    for b in [root, B1, load_B1, load_B1.previousBlock]:
        if b.is_valid():
            print ("Success! Valid block is verified.")
        else:
            print ("Error! Valid block is not verified.")


# ----------------------------------------------------------------------
    if B1.good_nonce():                                         # ------
        print("Success! Nonce is good after save and load!")    # ------
    else:                                                       # ------
        print("ERROR! Bad nonce after load")                    # ------
# ----------------------------------------------------------------------


    Tx5 = Tx()
    Tx5.add_input(rose_pbc, 1)
    Tx5.add_output(mike_pbc, 100)
    Tx5.sign(rose_prv)

    B2 = TxBlock(B1)
    B2.addTx(Tx5)

    load_B1.previousBlock.addTx(Tx4)

    for b in [B2, load_B1]:
        if b.is_valid():
            print ("Error! Invalid block is verified.")
        else:
            print ("Success! Invalid blocks is detected.")


    # Test mining rewards and tx fees
    B3 = TxBlock(B2)
    B3.addTx(Tx2)
    B3.addTx(Tx3)
    B3.addTx(Tx4)

    Tx6 = Tx()
    Tx6.add_output(mara_pbc, 25)
    B3.addTx(Tx6)
    
    if B3.is_valid():
        print("Success! Block reward succeeded.")
    else:
        print("Error! Block reward failed.")

    B4 = TxBlock(B3)
    B4.addTx(Tx2)
    B4.addTx(Tx3)
    B4.addTx(Tx4)

    Tx7 = Tx()
    Tx7.add_output(mara_pbc, 25.2)
    B4.addTx(Tx7)

    if B4.is_valid():
        print("Success! Transaction fees succeeded.")
    else:
        print("Error! Transaction fees failed.")

    #Greedy miner
    B5 = TxBlock(B4)
    B5.addTx(Tx2)
    B5.addTx(Tx3)
    B5.addTx(Tx4)
    Tx8 = Tx()
    Tx8.add_output(mara_pbc, 26.2)
    B5.addTx(Tx8)
    if not B5.is_valid():
        print("Success! Greedy miner is detected.")
    else:
        print("Error! Greedy miner is not detected")
