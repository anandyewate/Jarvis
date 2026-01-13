import google.generativeai as genai

genai.configure(api_key="AIzaSyAwHM-6NiUM9_yC4n7AmbGIxJZxmF2CxyQ")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is coding?")
print(response.text)
