from Signature import *

class Tx:
    inputs = None
    outputs =None
    sigs = None

    def __init__(self):
        self.inputs = []
        self.outputs = []

    def __repr__(self):
        return repr([self.inputs, self.outputs])

    def add_input(self, from_addr, amount):
        self.inputs.append(encrypt(str(amount).encode(), from_addr))
        pass

    def add_output(self, to_addr, amount):
        self.outputs.append(encrypt(str(amount).encode(), to_addr))
        pass

    def sign(self, private):
        rep = repr(self).encode()
        # print(rep)
        self.sigs = sign(rep, private)

def encrypt(message, public_key):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt(ciphertext, private_key):
    try:
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext
    except:
        return None