from voice import speak
import datetime as dt

def wishme():
    hour =int(dt.datetime.now() .hour)
    if hour >=0 and hour <12 :
        speak("good morning sanjay.")
        speak("THis is teego ,i can assist you")
    elif hour >=12 and hour <17 :
        speak("good afternoon sanjay.")
        speak("THis is teego ,i can assist you")
    elif hour >=17:
        speak("good evening sanjay.")
        speak("THis is teego ,i can assist you")

