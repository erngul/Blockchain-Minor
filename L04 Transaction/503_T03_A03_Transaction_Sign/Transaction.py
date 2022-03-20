from Signature import *
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
class Tx:
    inputs = None
    outputs =None

    def __init__(self, input = [], output = []):
        self.inputs = input
        self.outputs = output
        pass

    def __repr__(self):
        return repr([self.inputs, self.outputs])

    def add_input(self, from_addr, amount):
        self.inputs.append(encrypt(str(amount).encode(), from_addr))
        pass

    def add_output(self, to_addr, amount):
        self.outputs.append(encrypt(str(amount).encode(), to_addr))
        pass

    def add_signature(self, privateKey):
        print(repr(self.inputs))
        sign(repr(self.inputs))


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

def sign(message, private_key):
    encodedMessage = str.encode(message)
    sig = private_key.sign(
        encodedMessage,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return sig

def verify(message, signature, public_key):
    inputMessage = message.encode()
    try:
        public_key.verify(
            signature,
            inputMessage,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False