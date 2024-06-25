
try:
    from speak import speak
    import pyttsx3
    import speech_recognition as sr
    import datetime as dt
    import wikipedia
    import os
    import webbrowser
    import pywhatkit as whatsapp
    import google.generativeai as palm
    from colorama import Fore




    def wishme():
        hour =int(dt.datetime.now() .hour)
        if hour >=0 and hour <12 :
            speak("good morning sanjay")
            speak("THis is teego  ")
            speak(" i can assist you")
        elif hour >=12 and hour <17 :
            speak("good afternoon sanjay")
            speak("THis is teego ")
            speak(" i can assist you")
        elif hour >=17:
            speak("good evening sanjay")
            speak("THis is teego ")
            speak(" i can assist you")

    def wikipedia():
        speak("searching in wikpedia")
        query=query.replace("wikipedia ","")
        results=wikipedia.summary(query,sentences=10)
        speak("According to wikipedia")
        print(results)
        speak(results)

    def whatsapp():
        hour= int(dt.datetime.now() .hour)
        min = int(dt.datetime.now().minute)
        minf = min+1
        speak("yeah sure")
        speak("enter an mobile number here")
        a = int(input(Fore.GREEN+"Enter a Mobile number here:"))
        hour= int(dt.datetime.now() .hour)
        min = int(dt.datetime.now().minute)
        minf = min+1
        b="91+"
        c=b+a
        speak("enter a message that you need o send")
        b = input("Type a message that you need to send:")
        speak("your message will be sent shotly ")
        speak("stay here..")
        whatsapp.sendwhatmsg(c, b, hour, minf, 15)
    def youtube():
        query = query.replace("open youtube search", "")
        print(Fore.YELLOW+query)
        link = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(link)
        speak("here some results")
    def createprogram():
            query=query.replace("create program","")
            extension=query
            speak("enter a file name")
            file_name=input("Filename\t:")
           
            palm.configure(api_key='')


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
        

    def generateresult():
        palm.configure(api_key='')

        if True:
            response =palm.chat(messages=query)
            speak("here some results from Google's palm ")
            print(Fore.GREEN+response.last)
            if "speak" in query:
                speak(response.last)
    def website():
         
            query=query.replace("open","")
            webbrowser.open("https://www.instagram.com/")
            speak("here some results")
    def music():
        musicdir="D:\\mp3\\"
        songs=os.listdir(musicdir)
        len=len(songs)
        sum=0
        for s in songs:
            sum=sum+1
            print(Fore.WHITE+"",sum,'\t',s)
        while True:
            speak("enter video track number:")
            a=int(input(Fore.YELLOW+"Enter a Song Track NO:"))
            os.startfile(os.path.join(musicdir,songs[a-1]))
            print(Fore.BLUE+"Now playing....",Fore.GREEN+songs[a-1])
            print('\n')
        else:
            print(Fore.MAGENTA+"NO Songs Found!!")
    def songs():
        viddir="D:\\songs\\"
        videos=os.listdir(viddir)
        len=len(videos)
        sum=0
        for v in videos:
            sum=sum+1
            print(Fore.WHITE+"",sum,'\t',v)
      
        while True:
            speak("enter video track number:")
            a=int(input(Fore.YELLOW+"Enter a Video Track NO:"))
            os.startfile(os.path.join(viddir,videos[a-1]))
    
            print(Fore.BLUE+"Now playing....",Fore.GREEN+videos[a-1])
            print('\n')

        else:
            print(Fore.MAGENTA+"NO Videos Found!!")
    def movie():
        viddir="D:\\movies\\"
        videos=os.listdir(viddir)
        len=len(videos)
        sum=0
        for v in videos:
            sum=sum+1
            print(Fore.WHITE+"",sum,'\t',v)
        while True:
            speak("enter track number:")
            a=int(input(Fore.YELLOW+"Enter a Movie Track NO:"))
            os.startfile(os.path.join(viddir,videos[a-1]))
            speak("playing")
            print(Fore.BLUE+"Now playing....",Fore.GREEN+videos[a-1])
            print('\n')
        else:
            print(Fore.LIGHTRED_EX+"Input is Wrong Try Again")
                


    
    
except:
    print("Network issue,Connect to Network and Try again")
    speak("hello this is Teego")
    speak("Please check your network is connected,and try again")
  
    

if __name__=="__main__":
    try:
        wishme()

        
        while True:
       
            query =input("Enter Promt Here..")
    
        
            if 'wikipedia' in query:
                wikipedia()
                
            elif "message" and "whatsapp" in query:
                whatsapp()
            elif "~" in query:
                speak("Thankyou ")
                speak("see you again")
                break
            elif "open" in query and "youtube" in query and "search" or "youtube" or "play " in query and "song" in query:
                youtube()
            elif "create"and  "a" and "program" in query:
                createprogram()
            elif "play music" in query:
                music()
            elif "open" in query:
                website()
            
            else:
                generateresult()
            
        

    except:
        while True:
            break     
        