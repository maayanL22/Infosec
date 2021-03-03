from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'

def xor_strings(str1,str2):
    r1 = [ord(a) ^ ord(b) for a,b in zip(str1,str2)]
    r2 = []
    for asc in r1:
        r2.append(chr(asc))
    return ''.join(r2)

def weak_hmac(m, k, ipad, opad):
    pass # TODO
    ipad1 = ipad.decode('utf-8')
    k1 = k.decode('utf-8')
    r1 = xor_strings(k1, ipad1)
    print(r1)
    m1 = m.decode('utf-8')
    r11 = r1 + m1
    r11 = r11.encode('utf-8')
    first = sha1(r11).hexdigest()
    opad1 = opad.decode('utf-8')
    k2 = k.decode('utf-8')
    sopad = xor_strings(k2, opad1)
    print(sopad)
    final = sopad + first
    final = final.encode('utf-8')
    print(sha1(final).hexdigest())
    return sha1(final).hexdigest()
