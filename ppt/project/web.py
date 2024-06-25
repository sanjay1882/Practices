from project.ontimeprogram import responseinput
from project.ontimeprogram import conn
import os
import google.generativeai as genai
if __name__ =="__main__":
    genai.configure(api_key="AIzaSyDaghkqsxDt3cw6OTr2txPi7kMcTTEFkcM")



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
   
    file=open(conn,"w")
    prompt_parts2 = [
  "\n\n\n\n\n\nUserassume that you are the code generater.You need to generate only the program for the given question. dont use triple quotes inside a program.Dont explain about the code insidecode editer. \n\n "+ responseinput,
    ]
    dir="C:\\Users\\rikba\\Desktop\\ppt\\"
    print("Working on it..")
    responsea = model.generate_content(prompt_parts2)
    out=responsea.text
    file.write(out)
    file.close()
    os.startfile(os.path.join(dir,"index.html"))
    print("Executing...")
    
    



    
              
    
    