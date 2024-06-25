import google.generativeai as genai

def gemini(promptint):

  genai.configure(api_key="AIzaSyDaghkqsxDt3cw6OTr2txPi7kMcTTEFkcM")  # Replace with your actual API key

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
      # ... other safety settings
  ]

  model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
  convo = model.start_chat(history=[])

  convo.send_message(promptint)
  print(convo.last.text)
