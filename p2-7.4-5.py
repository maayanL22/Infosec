from Crypto.PublicKey import RSA
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto.Signature import PKCS1_v1_5

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def sign(m, private_key):
    pass # TODO
    m = str(m)
    m = m.encode('utf-8')
    hasher = SHA256.new(m)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(hasher)
    return signature

def verify(m, s, public_key):
    pass # TODO
    m = str(m)
    m = m.encode('utf-8')
    hasher = SHA256.new(m)
    verifier = PKCS1_v1_5.new(key)
    if verifier.verify(hasher, s):
        return True
    else:
        return False
