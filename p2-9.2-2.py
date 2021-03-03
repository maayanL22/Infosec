from hashlib import sha1

def sign(line):
    pass
    statsign = sha1(line).hexdigest()
    return statsign[0:20]

def scan(paths, signature):
    pass
    print("sign: ",signature)
    final = []
    is_in = False
    for path in paths:
        path1 = open(path,'r')
        lines = path1.readlines()
        for line in lines:
            line1 = line.rstrip().encode('utf-8')
            statline = sha1(line1).hexdigest()
            statline1 = statline[0:20]
            print(statline1)
            if((statline1 == signature) and (is_in == False)):
                final.append(path)
                is_in = True
        is_in = False
        path1.close()
    
    return final
    
