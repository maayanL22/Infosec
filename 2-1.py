alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
   pass # do stuff and return ciphertext
   alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
   alph = list(alphabet1)
   ptxt = list(plaintext)
   cnt = 0
   num = 0
   for letter in plaintext :
      num = alphabet1.index(letter)
      print(num)
      if(num - k >= 0):
        ptxt[cnt] = alph[num - k]
      else:
        ptxt[cnt] = alph[26 + num - k]
      cnt = cnt + 1    
      
   encriptedtext = ''.join(ptxt)
   print("encripted text:")
   print(encriptedtext)
   return encriptedtext
