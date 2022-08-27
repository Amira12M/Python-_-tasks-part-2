#create a function that generates a random password, the password must be +7 letters, should contain numbers, upper case letter, small letter and _ only.

import string 
import random 

def create _ pass(length):
characterlist = ""
characterlist+= string . ascii_ letters
characterlist += string . digits
characterlist += string. punctuations

 
password = []
for i in range(length):
      randomchar = random. choice ( characterlist)
      password.append (randomchar)
return ''.join (password)

 
length = int (input("Enter password length: "))
print ("The random password  is " + create _ pass (length)) 
