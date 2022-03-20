from Signature import *

from Transaction import *

def print_transaction(tx_name, tx):
    print('---------------')
    print('-- ' + tx_name)
    counterIn = 0
    counterOut = 0
    for i in tx.inputs:
        for key in keys_list:
            decryptedMessage = decrypt(i, key[1])
            if decryptedMessage is not None:
                counterIn += 1
                print(f'In[{counterIn}]: {key[0]} sends {decryptedMessage} coin')
                pass
    for o in tx.outputs:
        for key in keys_list:
            decryptedMessage = decrypt(o, key[1])
            if decryptedMessage is not None:
                counterOut += 1
                print(f'Out[{counterOut}]: {key[0]} receives {decryptedMessage} coin')
                pass
    for key in keys_list:
        verification = verify(repr(tx).encode(), tx.sigs, key[2])
        if verification == True:
            print(f'{tx_name} is signed by {key[0]}')
    print()

if __name__ == "__main__":
    
    keys_list =[]

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', mara_prv, mara_pbc))

    # --------------------------------------
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(mike_pbc, 1)
    Tx1.sign(alex_prv)

    # --------------------------------------
    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2)
    Tx2.add_output(mike_pbc, 1)
    Tx2.add_output(rose_pbc, 1)
    Tx2.sign(alex_prv)

    # --------------------------------------
    Tx3 = Tx()
    Tx3.add_input(rose_pbc, 1.2)
    Tx3.add_output(alex_pbc, 1.1)
    Tx3.sign(rose_prv)
    Tx3.sign(mara_prv)

    # --------------------------------------
    for tx in [Tx1, Tx2, Tx3]: 
        tx_name = [k for k,v in locals().items() if v == tx][0]
        print_transaction(tx_name, tx)
        