def simple_hash(s):
    #return # do stuff and return the hash
    r = 7
    hash = r % pow(2,16)
    for chr in s:
        r *= 31
        r += ord(chr)
        hash = r % pow(2,16)
        
    return hash
