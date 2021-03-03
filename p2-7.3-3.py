from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    pass # return ciphertext and key
    m = str(m)
    m = str.encode(m)
    rsa_public_key = RSA.importKey(public_key)
    encryptor = PKCS1_OAEP.new(rsa_public_key)
    encrypted = encryptor.encrypt(m)
    return encrypted, key

def decrypt(c, private_key):
    pass # TODO
    print(c)
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decoded_m = rsa_private_key.decrypt(c).decode('utf-8')
    number_m = int(decoded_m)
    return number_m, private_key

encrypt_result = encrypt(1234567890, public_key)
encrypted_m = encrypt_result[0]
print('ENCRYPT RESULT: ', encrypt_result, '\n')
decrypt_result = decrypt(encrypted_m, private_key)
print('DECRYPT RESULT: ', decrypt_result)
