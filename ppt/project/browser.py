
import webbrowser

import google.generativeai as genai
def browser(query):
    genai.configure(api_key="AIzaSyDaghkqsxDt3cw6OTr2txPi7kMcTTEFkcM")

# Set up the model
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

    prompt_parts = [
  "assume that intelligent.when input say to open a website you nee response a correct website address.You response should be oly a website link like open insta open face book sampleoutput='www.fackbook.com' /n"+query,
]
    response = model.generate_content(prompt_parts)
    link=response.text
    webbrowser.open(link)
