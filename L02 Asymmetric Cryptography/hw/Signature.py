import pickle

from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def sign(message, private_key):
    sig = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return sig

def verify(message, signature, public_key):
    try:
        verification = public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

def save_keys(keys_file_name, keys, pw):
    keys_ser_list = []
    private_key = keys[0]
    public_key = keys[1]

    prv_ser = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(pw)
    )
    pbc_ser = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    keys_ser_list.append((prv_ser, pbc_ser))

    savefile = open(keys_file_name, "wb")
    pickle.dump(keys_ser_list, savefile)
    savefile.close()

def load_keys(keys_file_name, pw):
    loadfile = open(keys_file_name, "rb")
    keys_list_ser = pickle.load(loadfile)
    loadfile.close()

    keys_list = []
    for item in keys_list_ser:
        key_name, private_key_ser, public_key_ser = item
        private_key = serialization.load_pem_private_key(private_key_ser, password=pw)
        public_key = serialization.load_pem_public_key(public_key_ser)

        keys_list.append((key_name, private_key, public_key))
    return keys_list