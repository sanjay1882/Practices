from voice import speak
import wikipedia
def wikipedia1(query):
    
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=10)
    print(results)
    speak(results)