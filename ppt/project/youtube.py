from voice import speak
import webbrowser
def youtubesearch(query):
    list=["open","youtube","search"]
    for i in list:
        query = query.replace(i, "")
    print(query)
    link = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(link)
    speak("here some results")


    