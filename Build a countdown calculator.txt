# Build a countdown calculator.Write some code that can take two dates as input, and then calculate the amount of time between them.

from datetime import date
def calc (date1, date2):
    year , month , day = map (int , date1. split('_'))
    date1 = date (year, month,day)
    year, month, day = map (int , date2. split ('_"))
    date2 = date (year, month, day )
    c = abs (date1 - date2 )
return c. days 
 date1 = input ("Enter First date in YYY-MM-DD Format: ") 
 date2 = input ("Enter Second date in YYY-MM-DD Format: ")  
print (calc (date1 , date2 ))
