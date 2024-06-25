from voice import speak
import datetime as dt

import pywhatkit as whatsapp
def sendmsg():
    hour= int(dt.datetime.now() .hour)
    min = int(dt.datetime.now().minute)
    minf = min+1
    speak("Yes you can")
    speak("Enter an mobile number here:")
    a = input("Enter a Mobile number here:")
    b="91+"
    c=b+a
    speak("enter a message that you need o send")
    b = input("Type a message that you need to send:")  
    speak("your message will be sent shortly stay here..")
    whatsapp.sendwhatmsg(c, b, hour, minf, 0)