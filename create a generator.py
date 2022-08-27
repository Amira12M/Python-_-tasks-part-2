# Create a code generator . create 2 functions , the first one takes text as input , replaces each letter with another letter , and outputs the "encoded" message ., the second one "decoded" the message to the original text.

def encoder (password):
  key = "amira"
  l= 0 
  for ch in range (len(password)):
     if l== len(key)-1:
         l=0
    else:
        l+=1
    c= ord (password[ch] + ord(key [ch]))
    out.append (c)
new_ password = ''.join ([chr(ch) for ch in out])
return new_password 

def decoder (new_password):

  key = "amira"
  l= 0 
  for ch in range (len(password)):
     if l== len(key)-1:
         l=0
    else:
        l+=1
    c= ord (password[ch] - ord(key [ch]))
    out.append (c)
old_ password = ''.join ([chr(ch) for ch in out])
return old_password: 
 pas = input (" write ur password:  ")
 enc = encoder (pass)
 print (enc)
 dec= decoder (enc)
 print (dec)
