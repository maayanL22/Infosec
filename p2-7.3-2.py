n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def encrypt(m, public_key):
    pass # TODO
    return pow(m,public_key[1]) % n

def decrypt(c, private_key):
    pass # TODO
    return pow(c,private_key[1]) % n
