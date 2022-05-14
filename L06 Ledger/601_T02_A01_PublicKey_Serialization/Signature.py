from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_der_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import *
def generate_keys():
    privateIn = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = privateIn.private_bytes(
        encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    publicIn = privateIn.public_key()
    public_key = publicIn.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return private_key, public_key

def sign(message, private):
    private_key = load_pem_private_key(private, password=None)
    signature = private_key.sign(
    bytes(str(message), 'UTF-8'),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256())
    return signature

def verify(message, sig, public):
    try:
        public_key = load_pem_public_key(public)
        output = public_key.verify(
            sig,
            bytes(str(message), 'UTF-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256())
        return True
    except:
        return False
def deserialize_public_key(public_key):
    public_key_final = serialization.load_pem_public_key(public_key)
    return public_key_final

def deserialize_private_key(private_key, pw=None):
    private_key_final = serialization.load_pem_private_key(private_key,password=str.encode(pw), backend=default_backend())
    return private_key_final