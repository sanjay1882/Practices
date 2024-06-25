
import google.generativeai as genai

   
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

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": [""]
  },
  {
    "role": "model",
    "parts": ["```python\ndef is_prime(number): \n    \"\"\"\n    Check if the given number is prime.\n\n    Args:\n        number (int): The number to check.\n\n    Returns:\n        bool: True if the number is prime, False otherwise.\n    \"\"\"\n\n    if number <= 1:\n        return False\n\n    for i in range(2, int(number**0.5) + 1):\n        if number % i == 0:\n            return False\n\n    return True\n\n\n\n\nn = int(input(\"Enter a number: \"))\n\nif is_prime(n):\n    print(f\"{n} is a prime number.\")\nelse:\n    print(f\"{n} is not a prime number.\")\n```"]
  },
])
def chat():
    ui=input("Enter")
    convo.send_message(ui)
    print(convo.last.text)