
import pyttsx3
import speech_recognition as sr
import datetime as dt
import wikipedia
import os
import webbrowser
import pywhatkit as whatsapp
import google.generativeai as palm
from colorama import Fore


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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
if __name__ == "__main__":
    wishme()
    while True:
       
        query =input(Fore.RED+ "Enter Promt Here..")# type: ignore
#wikipedia
        if 'wikipedia' in query:
            speak("searching in wikpedia")
            query=query.replace("wikipedia ","")
            results=wikipedia.summary(query,sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
       
#whatsapp
        elif "message" and "whatsapp" in query:
            hour= int(dt.datetime.now() .hour)
            min = int(dt.datetime.now().minute)
            minf = min+1
            speak("enter an mobile number here")
            a = input(Fore.GREEN+"Enter a Mobile number here:")
            b="91+"
            c=b+a
            speak("enter a message that you need o send")
            b = input("Type a message that you need to send:")
            
            speak("your message will be sent shotly stay here..")
            whatsapp.sendwhatmsg(c, b, hour, minf, 15)
    
        elif "what is your name" in query:
            speak("my name is teego ")
            print(Fore.BLUE+"my name is teego ")
            
        
        elif "open" in query and "youtube" in query and "search" or "youtube" in query:
            
                query = query.replace("open youtube search", "")
                print(Fore.YELLOW+query)
                link = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(link)
                speak("here some results")
        elif "insta" in query or "instagram" in query:
            webbrowser.open("https://www.instagram.com/")
            speak("here some results")






        elif "play music" in query:
        
            musicdir="D:\\music"
            songs=os.listdir(musicdir)
            len=len(songs)
            for s in songs:
                print(s)
                query=None
                os.startfile(os.path.join(musicdir,songs[len-1]))
                
                
        elif "create"and  "a" and "program" in query:
            query=query.replace("create program","")
            extension=query
            speak("enter a file name")
            file_name=input("Filename\t:")
           
            palm.configure(api_key='AIzaSyBK67qhRGxJIb-JmSGFlSeYMqjqXxJOZtU')


            if "python" in extension:

                conn=file_name+".py"
                speak("your python file is created")  
                file=open(conn,"w")
                speak("tell me a program question")
                query =input("enter")
                response =palm.chat(messages=query)
                ans=response.last
                file.write(ans)
                speak("done")
                file.close()


              
            if "html" in extension:
                conn=file_name+".html"
                speak("your html file is created")   
                
                file=open(conn,"w")
                speak("tell me a program question")
                query =input("Enter")
                response =palm.chat(messages=query)
                ans=response.last
                file.write(ans)
                speak("Done")
                file.close()
                break
            if "css" in extension:
                conn=file_name+".css"
                speak("your css file is created")   
                
                file=open(conn,"w")
                speak("tell me a program question")
                query =command()
                response =palm.chat(messages=query)
                ans=response.last
                file.write(ans)
                speak("Done")
                file.close()
                break

            if "java" in extension:
                conn=file_name+".java"
                speak("your java file is created")   
                
                file=open(conn,"w")
                speak("tell me a program question")
                query =input("Enter")
                response =palm.chat(messages=query)
                ans=response.last
                file.write(ans)
                speak("Done")
                file.close()
                break
            if "text" in extension:
                conn=file_name+".txt"
                speak("your text file is created")   
                
                file=open(conn,"w")
                speak("tell me a program question")
                query =input("enter")
                response =palm.chat(messages=query)
                ans=response.last
                file.write(ans)
                speak("Done")
                file.close()
                break
            if "c" in extension:
                conn=file_name+".c"
                speak("your c file is created")   
                
                file=open(conn,"w")
                speak("tell me a program question")
                query =input("enter")
                response =palm.chat(messages=query)
                ans=response.last
                file.write(ans)
                speak("Done")
                file.close()
                break
           
        elif "close " in query:
            speak("thankyou ")
            quit()
        else:
            palm.configure(api_key=' AIzaSyBK67qhRGxJIb-JmSGFlSeYMqjqXxJOZtU')

            if True:
                response =palm.chat(messages=query)
                print(Fore.GREEN+response.last)
                speak(response.last)
                    

                    