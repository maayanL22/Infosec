import hashlib
import itertools


def weak_md5(s):
    return hashlib.md5(s).digest()[:5]


def find_collisions():
    #return # return (s1, s2) such that s1 != s2 and weak_md5(s1) == weak_md5(s2)
    length = 5
    colldict = {
        
    }
    
    i = 0
    opt = ''
    while(i < 128):
        opt = opt + chr(i)
        i += 1
    
    for som in itertools.product(opt, repeat = length):
        comb = ''.join(som)
        hashkey = weak_md5(comb)
        if hashkey in colldict:
            return colldict[hashkey],comb
        else:
            colldict[hashkey] = comb
    
    
    return 'not','found'
