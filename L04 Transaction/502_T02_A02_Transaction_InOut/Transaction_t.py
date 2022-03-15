from Signature import *
from Transaction import *

def print_transaction(tx_name, tx):
    for key in keys_list:
        decryptedMessage = decrypt(tx, key[0])
        for tx.inputs
        if decryptedMessage is not None:
            print(key[2])
            print(decryptedMessage)
    # print(tx_name + ' ' + str(tx))
    pass

if __name__ == '__main__':
    
    keys_list =[]

    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

    keys_list.append([alex_prv, alex_pbc, 'Alex'])
    keys_list.append([mike_prv, mike_pbc, 'Mike'])
    keys_list.append([rose_prv, rose_pbc, 'Rose'])
    keys_list.append([mara_prv, mara_pbc, 'Mara'])

    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 0.9)
    Tx1.add_output(mike_pbc, 0.8)
    print_transaction('Tx1', Tx1)

    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2.1)
    Tx2.add_output(mike_pbc, 0.9)
    Tx2.add_output(rose_pbc, 1.0)
    print_transaction('Tx2', Tx2)

    Tx2.add_input(mara_pbc, 0.7)
    Tx2.add_input(mara_pbc, 1.1)
    Tx2.add_input(mara_pbc, 1.5)
    Tx2.add_output(mike_pbc, 1.9)
    Tx2.add_output(rose_pbc, 0.2)
    print_transaction('Tx2', Tx2)
