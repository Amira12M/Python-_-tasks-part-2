# Make a temperature/measurement converter. Write a script that can convert Fahrenheit to Celcius and back,or inches to centimeters and back, etc.
 def calc (degree):
     return (degree*9/8)+ 32

deg = float (input (' Degree with c : ' ))
print (calc (deg))
