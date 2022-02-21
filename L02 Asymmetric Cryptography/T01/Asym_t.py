from Asym import *
# from Asym_E_01_S import *

if __name__ == '__main__':
    
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()

    alex_message = b'This is a message for Rose: Hi Rose'

    ciphertext = encrypt(alex_message, rose_pbc)


    received_message = decrypt(ciphertext, rose_prv)
    if received_message!= None and received_message == alex_message:
        print("Success: The received message is properly decrypted by Rose's Private Key.")
    else:
        print("Fail: The received message is not properly decrypted by Rose's Private Key.")


    received_message = decrypt(ciphertext, mike_prv)
    if received_message== None or received_message == alex_message:
        print("Fail: The received message is None or could be decrypted by Mike's Private Key!")
    else:
        print("Success: The received message could not be decrypted by Mike's Private Key.")


    received_message = decrypt(ciphertext, alex_pbc)
    if received_message== None or received_message == alex_message:
        print("Fail: The received message is None or could be decrypted by Alex's Public Key!")
    else:
        print("Success: The received message could not be decrypted by Alex's Public Key.")