# Build an email slicer : create a function that takes an email as input  and retrieve the username and domain of the email.
 def retrieve (email):
      user , dom = email . split ("@")
      print ( f' Ur username is {user} \n Domain is {dom}' )
 
em = input (" Write ur email: " )
retrieve (em)
