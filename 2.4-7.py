from collections import Counter

def get_max(l):
    max = -1
    maxindex = -1
    i = 0
    length = len(l)
    while(i < length):
        if(l[i] > max):
            max = l[i]
            maxindex = i
        i += 1
    
    return maxindex

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def is_english(s):
    pass # return boolean
    if(is_ascii(s) == False):
        return False
    
    print(s)
    for c in s:
        asc = ord(c)
        if((asc < 65) or (asc > 90 and asc < 98) or (asc > 122)):
            print("hola")
            s = s.replace(c,'')
    
    s = s.lower()
    letts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for c in s:
        pl = ord(c) - 97
        letts[pl] += 1
     
        
    final = []
    cnt = 0
    while(cnt < 3):
        index = get_max(letts)
        av = index + 97
        final.append(chr(av))
        letts[index] = -100
        cnt += 1
    
    cnt = 0
    print("final: ",final)
    
    while(cnt < 3):
        if((final[cnt] != 'e') and (final[cnt] != 't') and (final[cnt] != 'a') and 
           (final[cnt] != 'o') and (final[cnt] != 'i') and (final[cnt] != 'n')):
              return False
        cnt += 1    
    
    return True
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
