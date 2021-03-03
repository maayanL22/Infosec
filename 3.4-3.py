import itertools

def simple_hash(s):
    r = 7
    for c in s:
        r = (r * 31 + ord(c)) % 2**16
    return r


def crack(s):
    #return # return s2 such that s != s2 and simple_hash(s) == simple_hash(s2)
    length = len(s)
    if(len(s) == 0):
        length = 4
    '''
    nums = '0123456789'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    symb = '!@#$%^&*()_+-=[]{}.,/?\|:;<>'
    alphnumssymb = alph + nums + symb
    print(alphnumssymb)
    '''
    i = 0
    opt = ''
    while(i < 128):
        #print(chr(i))
        opt = opt + chr(i)
        i += 1
    for l1 in itertools.product(opt, repeat = length):
        fhash = ''.join(l1)
        if((s != fhash) and (simple_hash(s) == simple_hash(fhash))):
            return fhash
    
    return 'couldnt crack'
