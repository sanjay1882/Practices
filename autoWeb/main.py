from PROMPT import responseinput

import os
import google.generativeai as genai
from API import API_KEY
if __name__ =="__main__":
    genai.configure(api_key=API_KEY)



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
    conn="index.html"
    filea=open(conn,"w")
    prompt_parts2 = [
  "\n\n\n\n\n\nUserassume that you are the html code generater for food app.\n\n "+ responseinput,
    ]
    dir="C:\\Users\\rikba\\Desktop\\New folder\\autoWeb"
    print("Working on it ._. ")
    responsea = model.generate_content(prompt_parts2)
    out=responsea.text
    print("..Executing...")
    filea.write(out)
    print(out)
    filea.close()
    os.startfile(os.path.join(dir,"index.html"))
    print("Done")
   
    
    



    
              
    
    