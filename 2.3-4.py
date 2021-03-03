def get_prg(plaintext_size, k):
    pass # return keystream
    i = j = 0
    klist = list(k)
    keystream = list(k) 
    asclist = list(k)
    asclist2 = list(k)
    length = len(k)
    cnt = 0
    while(cnt < length):
        asclist[cnt] = ord(klist[cnt])
        asclist2[cnt] = ord(klist[cnt])
        cnt += 1
    
    prefin = []
    num = 0
    cnt = 0    
    while(cnt < plaintext_size):
        i = (i+1) % length
        j = (j + asclist[i]) % length
        asclist[i] = asclist2[j]
        asclist[j] = asclist2[i]
        asclist2[i] = asclist[i]
        asclist2[j] = asclist[j]
        num = (asclist[i] + asclist[j]) % length
        prefin.append(asclist[num])
        cnt += 1
        
    cnt = 0
    final = []
    while(cnt < plaintext_size):
        c = chr(prefin[cnt])
        final.append(c)
        cnt += 1
    
    return ''.join(final)
     
 
 
 
def fake_rc4(plaintext, keystream):
    pass # return ciphertext
    streamlist = list(keystream)
    textlist = list(plaintext)
    length = len(plaintext)
    cnt = 0
    strasc = []
    txtasc = []
    prefin = []
    
    while(cnt < length):
        strasc.append(ord(streamlist[cnt]))
        txtasc.append(ord(textlist[cnt]))
        cnt += 1
        
    
    cnt = 0    
    while(cnt < length):
        prefin.append(strasc[cnt] ^ txtasc[cnt])
        cnt += 1
    
    final = []
    cnt = 0
    while(cnt < length):
        final.append(chr(prefin[cnt]))
        cnt += 1
    
    return ''.join(final)
