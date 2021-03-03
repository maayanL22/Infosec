n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def sign(m, private_key):
    pass # TODO
    return pow(m, private_key[1]) % private_key[0]

def verify(m, s, public_key):
    pass # TODO
    return (pow(s, public_key[1]) % public_key[0]) == m
