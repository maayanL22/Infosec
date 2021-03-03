from Crypto.Cipher import ARC4

def rc4(plaintext, key):
    pass # return ciphertext
    keystream = ARC4.new(key)
   

    cyphertext = keystream.encrypt(plaintext)
    return cyphertext
