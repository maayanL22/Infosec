from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english, aes_encrypt
from itertools import product

def aes_encrypt1(plaintext, k, iv):
    pass # return iv + ciphertext (in bytes)
    cipher = AES.new(k,AES.MODE_CBC, iv)
    return (iv + cipher.encrypt(plaintext))


def brute_force_aes(ciphertext):
    pass # return plaintext (in 'latin1', from aes_decrypt()), k
    iv = ciphertext[:AES.block_size]
    l1 = [0,3,6]
    l3 = [0,0,0,0,0,0,0]
    for nums in product([0,1,2,3,4,5,6,7,8,9], repeat = 6):
        ln = list(nums)
        alltog = l1 + ln + l3
        fnl = ''.join(map(str, alltog))
        fnl1 = fnl.encode('utf-8')
        print(fnl1)
        txt = aes_decrypt(ciphertext, fnl1)
        if((len(txt) % 16 == 0) and (len(txt.encode('utf-8')) % 16 == 0)):
            if((aes_encrypt1(txt, fnl1, iv) == ciphertext) and (is_english(txt) == True)):
                return txt,fnl1
    return txt,fnl1
    
    
    
    
