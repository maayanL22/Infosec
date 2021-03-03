from Crypto.Cipher import AES
from Crypto import Random




def aes_encrypt(plaintext, k):
    pass # return iv + ciphertext (in bytes)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(k,AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(plaintext))
    


def aes_decrypt(ciphertext, k):
    pass # return plaintext (in 'latin1')
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(k, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext[AES.block_size:]).decode('utf-8')
    
