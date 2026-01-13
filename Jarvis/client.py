import google.generativeai as genai

genai.configure(api_key="API")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is coding?")
print(response.text)

