from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
class Tx:
    inputs = None
    outputs = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        pass


    def add_input(self, from_addr, amount):
        self.inputs.append(encrypt(str(amount).encode(), from_addr))
        pass

    def add_output(self, to_addr, amount):
        self.outputs.append(encrypt(str(amount).encode(), to_addr))
        pass


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
