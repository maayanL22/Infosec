def encrypt(plaintext, k):
    pass # Do stuff and return ciphertext
    length = len(k)
    cnt = 0
    klist = list(k)
    txtlist = list(plaintext)
    k1 = []
    txt1 = []
    while(cnt < length):
        k1.append(ord(klist[cnt]))
        txt1.append(ord(txtlist[cnt]))
        cnt += 1
    finalas = []
    cnt = 0
    while(cnt < length):
        finalas.append(k1[cnt]^txt1[cnt])
        cnt += 1
    cnt = 0
    final = []
    while(cnt < length):
        final.append(chr(finalas[cnt]))
        cnt += 1
    cyphertxt = ''.join(final)
    return cyphertxt
