from voice import speak
import google.generativeai as genai

def extension(query1):
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
      # ... other safety settings
  ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                safety_settings=safety_settings)


    
    prompt_parts = [
  "\n\n\n\n\n\n\n\n\"\\n\\n\\n\\nin a following given sentence there contain programming language name or .html or .css or  other .txt .here you need to response only the extension of given programming language.or ther htm. or .css or othe file(.extension) format you need to response only extension of those files which is based upon\nsampleoutput:\n\t(\".extension\")\n\n\n user input\\n\\n\""+query1+"\n\n",
  ]

    response = model.generate_content(prompt_parts)
    ex1 = response.text.strip()
    
    speak("enter a file name")
    file_name=input("Filename\t:")
    conn=file_name+ ex1
    file=open(conn,"w")
    speak("created")
    prompt_parts2 = [
  "\n\n\n\n\n\nUserassume that you are the code generater.You need to generate only the program for the given question. dont use triple quotes inside a program.Dont explain about the code insidecode editer.ignore that output triple quotes \n\n "+ query1
    ]

    responsea = model.generate_content(prompt_parts2)
    out = responsea.text.strip()  # Remove leading/trailing whitespace
    
    file.write(out)
    




    