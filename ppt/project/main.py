from voice import speak
from greetings import wishme
import google.generativeai as genai
from colorama import Fore
from whatsapp import sendmsg
from youtube import youtubesearch
from wiki import wikipedia1
from file import extension

genai.configure(api_key="AIzaSyDaghkqsxDt3cw6OTr2txPi7kMcTTEFkcM")

from browser import browser
from gemini import gemini

    
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


if __name__ == "__main__":
    while True:
        
        query=input("Enter ")
        prompt_parts = [
        "Assume That You are the chatbot and a desktop assistant .Your name is \"Teego\".\n\ncreater: \"Sanjay\"student.\n\n  Teego:Created in Programming language \"python\".\n\n Teego : contains  lots of functionality.\n\n These are the functionality you have ,\nThey are,{\"function\" , \"Description\"}\n1.){\"Send WhatsApp message\", \"It can send only a WhatsApp message using Automation to the given number and  it doesn't contain information about WhatsApp\"}\n2.){\"Media player\" ,\"It can display the list of songs in the Local computer or directory and Play songs present the folder. it contains songs , video songs and movies . It cannot play a particular song when the user asks.\"}\n3.){\"Creating file\", \"It can create a file based upon their input .It mainly creates a programming file like Python ,Java etc..}\n4.){\"automate or Opening browser\", \"It  can open website what a user asks\"}\n5.){\"Search contents in YouTube\" , \"It can automate searching  the contents on YouTube and display content in YouTube\"}\n6.){\" integrated with Gemini \",\"It can Solve problems and Programs\"}\n7.){\"Search Contents in Wikipedia \",\"It can display details The historical moments, history ,stones, Countries, Places and etc..\"}\n8.){\"greeting\",\"hi,\"hey\",\"hello\"}\n if the user can  also ask to  do or perform a particular functionalities .\nyou should response only a keyword.\nthe keywords are given below:\n{ function:\"keyword\"}:\n\"\"\n{Send WhatsApp message:\"whatsapp-1\"}\n{Creating file:\"file-1\"}\n{automate or Opening browser:\"browser-1\"}\n{Search contents in YouTube:\"yt-1\"}\n{integrated with Gemini:\"genai-1\"}\n{Media player:\"media-1\"}\n{\"greetings:\"gretting-1}\n{Search Contents in Wikipedia:\"wiki-1\"}\"\"\noutput should be in one word when the input ask to perform a particular functionality. \n"+ query
        ]

        response = model.generate_content(prompt_parts)
        keyword=response.text

        if keyword == "gretting-1":
            wishme()
        elif keyword =="whatsapp-1":
            sendmsg()
        elif keyword =="genai-1":
            gemini(query)
        elif keyword =="yt-1":
            youtubesearch(query)
        elif keyword =="wiki-1":
            wikipedia1(query)
        elif keyword =="file-1":
            speak("enter a Program and what language You need")
            query1=input("Enter a Prompt Here:")
            
            extension(query1)
            
            speak("done")
        elif keyword=="browser-1":
            query=query.replace("open","")
            browser(query)
            
            
            
            
            
            
           
            