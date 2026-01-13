# test_gemini.py - TEST YOUR API KEY FIRST
import google.generativeai as genai
from config import GEMINI_API_KEY

print("🧪 Testing Gemini API Key...")
print(f"API Key: {GEMINI_API_KEY[:20]}...")

try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    
    print("✅ API configuration successful!")
    print("🔄 Testing with simple question...")
    
    response = model.generate_content("What is 2+2?")
    
    if response.text:
        print("✅ SUCCESS! Gemini is working!")
        print(f"Response: {response.text}")
    else:
        print("❌ No response received from Gemini")
        
except Exception as e:
    print(f"❌ FAILED: {e}")
    print("\n💡 Troubleshooting tips:")
    print("1. Check if Gemini is available in your region")
    print("2. Try using a VPN if you're in a restricted region")
    print("3. Make sure your API key is valid at https://aistudio.google.com/")
    print("4. Check your internet connection")