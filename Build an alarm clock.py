# Build an alarm clock: build an alarm clock for yourself , you can set multiple alarms , the alarm should show desktop notification.
 
from datetime import datetime 
import time
from plyer import  notification 
 
if __ name__ == "__ main __"
      date = input ("Hour:Minutes:Seconds in 24 format "). split ( ":")
      now = datetime .now ()
      now = now . strftime ("%H:%M:%S").split(":")
      while True :
            if date [0] == now[0] and date[1] == now[1] and date[2] == now[2]:
             notifications. notify(
                                               title = "ALERT!!!", 
                                              message = "Take a break ! It has been an hour !" ,
                                              timeout = 10 
                                           )
                                          time . sleep (3600)
                                         
