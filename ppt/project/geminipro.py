import google.ai.generativelanguage as glm
import google.generativeai as genai
import pathlib
import os
def geminipro(input,imgname):
    GOOGLE_API_KEY=('AIzaSyDaghkqsxDt3cw6OTr2txPi7kMcTTEFkcM')

    genai.configure(api_key=GOOGLE_API_KEY)
    
    img=imgname+".jpeg"
    
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(
    glm.Content(
        parts = [
            glm.Part(text=input),
            glm.Part(
                inline_data=glm.Blob(
                    mime_type='image/jpeg',
                    data=pathlib.Path('C:\\Users\\rikba\\Desktop\\imagegemini\\'+img).read_bytes()
                )
            ),
        ],
    ),
    stream=True)
    response.resolve()

    print(response.text)

if __name__ =="__main__":
    input=input("Enter a Input:")
    geminipro(input,"leo")