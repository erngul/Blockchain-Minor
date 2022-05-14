from Signature import *
from Transaction import *

def print_transaction(tx_name, tx):
    print('---------------')
    print('-- ' + tx_name)
    counterIn = 0
    counterOut = 0
    for i in tx.inputs:
        for key in keys_list:
            decryptedMessage = decrypt(i, key[0])
            if decryptedMessage is not None:
                counterIn += 1
                print(f'In[{counterIn}]: {key[2]} sends {decryptedMessage} coin')
                pass
    for o in tx.outputs:
        for key in keys_list:
            decryptedMessage = decrypt(o, key[0])
            if decryptedMessage is not None:
                counterOut+=1
                print(f'Out[{counterOut}]: {key[2]} receives {decryptedMessage} coin')
                pass
    print()


# print(tx_name + ' ' + str(tx))

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
