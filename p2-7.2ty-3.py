import math

def reset_false(l1,x):
    i = 0
    while(i < (x - 1)):
        l1.append(False)
        i += 1

def reset_false1(l1,x):
    i = 0
    while(i < (x - 1)):
        l1[i] = False
        i += 1

def check_true(l1):
    length = len(l1)
    i = 0
    while(i < length):
        if(l1[i] == False):
            return False
        i += 1
    return True



def get_bases(x):
    bases = []
    pnums = []
    reset_false(pnums,x)
    num = 1
    i = 1
    while(num < x):m)
        while(i < x):
            n = pow(num,i) % x
            pnums[n-1] = True
            i += 1   
        if(check_true(pnums) == True):
            bases.append(num)
        i = 1
        reset_false1(pnums,x)
        num += 1
        
    print(bases)
        
    
    
    
    
get_bases(13)
    
