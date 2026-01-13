# main.py - MULTILINGUAL INDIAN LANGUAGES VERSION
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import google.generativeai as genai
from config import *

class JarvisAssistant:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = ENERGY_THRESHOLD
        self.recognizer.dynamic_energy_threshold = True
        
        # Initialize current language
        self.current_language = DEFAULT_LANGUAGE
        
        # Initialize AI
        self.ai_enabled = False
        self.model = None
        self.initialize_ai()
        
        # Initialize text-to-speech
        self.tts_engine = pyttsx3.init()
        
        print("🎯 Multilingual Jarvis Assistant Initialized!")

    def initialize_ai(self):
        """Initialize Gemini AI"""
        print("\n" + "="*50)
        print("🔄 INITIALIZING GEMINI AI...")
        
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
            
            # Quick test
            test_response = self.model.generate_content("Say 'OK'")
            if test_response.text:
                self.ai_enabled = True
                print("✅ GEMINI AI CONNECTED!")
            else:
                print("❌ No response from Gemini")
                
        except Exception as e:
            print(f"❌ GEMINI AI FAILED: {e}")
        
        print(f"🤖 AI Status: {'ENABLED' if self.ai_enabled else 'DISABLED'}")
        print("="*50)

    def get_response_text(self, key):
        """Get localized response text"""
        lang_responses = LANGUAGE_RESPONSES.get(self.current_language, LANGUAGE_RESPONSES["en"])
        return lang_responses.get(key, LANGUAGE_RESPONSES["en"][key])

    def speak(self, text, language=None):
        """Convert text to speech in current language"""
        if language is None:
            language = self.current_language
            
        lang_code = SUPPORTED_LANGUAGES.get(language, {}).get("gtts_lang", "en")
        print(f"🗣️ [{language.upper()}] Jarvis: {text}")
        
        try:
            # Use gTTS for Indian languages
            tts = gTTS(text=text, lang=lang_code, slow=False)
            tts.save('temp_speech.mp3')
            
            pygame.mixer.init()
            pygame.mixer.music.load('temp_speech.mp3')
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            pygame.mixer.music.unload()
            
            if os.path.exists("temp_speech.mp3"):
                os.remove("temp_speech.mp3")
                
        except Exception as e:
            print(f"❌ TTS Error, using fallback: {e}")
            # Fallback to pyttsx3 (English only)
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()

    def detect_language_from_speech(self, text):
        """Detect language from spoken text"""
        text_lower = text.lower()
        
        # Check for language change commands
        for keyword, lang_code in LANGUAGE_KEYWORDS.items():
            if keyword in text_lower:
                return lang_code
                
        return self.current_language

    def change_language(self, language_code):
        """Change the current language"""
        if language_code in SUPPORTED_LANGUAGES:
            old_language = self.current_language
            self.current_language = language_code
            language_name = SUPPORTED_LANGUAGES[language_code]["name"]
            
            # Speak confirmation in new language
            confirmation = f"{self.get_response_text('language_changed')} {language_name}"
            self.speak(confirmation, language_code)
            
            print(f"🌐 Language changed: {old_language} -> {language_code} ({language_name})")
            return True
        return False

    def ask_gemini(self, prompt):
        """Get response from Gemini AI"""
        if not self.ai_enabled:
            return self.get_response_text("ai_unavailable")
        
        try:
            # Tell Gemini to respond in the current language
            language_name = SUPPORTED_LANGUAGES.get(self.current_language, {}).get("name", "English")
            prompt_with_language = f"Please respond in {language_name} language: {prompt}"
            
            response = self.model.generate_content(prompt_with_language)
            return response.text if response.text else "No response from AI."
        except Exception as e:
            return self.get_response_text("ai_unavailable")

    def get_news(self):
        """Fetch and read news headlines"""
        try:
            self.speak(self.get_response_text("news_fetching"))
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"  # India news
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                articles = response.json().get('articles', [])
                if articles:
                    for i, article in enumerate(articles[:2]):
                        title = article.get('title', '')
                        if title and title != "[Removed]":
                            self.speak(f"{self.get_response_text('news')} {i+1}: {title}")
                    return self.get_response_text("news_finished")
                else:
                    return self.get_response_text("no_news")
            else:
                return self.get_response_text("news_unavailable")
                
        except Exception as e:
            return self.get_response_text("news_unavailable")

    def process_command(self, command):
        """Process voice commands in multiple languages"""
        command_lower = command.lower()
        print(f"🎯 Processing [{self.current_language}]: {command}")
        
        # Detect and handle language change
        detected_lang = self.detect_language_from_speech(command_lower)
        if detected_lang != self.current_language:
            if self.change_language(detected_lang):
                return
        
        # Website commands (work in all languages)
        if any(word in command_lower for word in ["open google", "गूगल खोलो", "गूगल ओपन", "கூகுள் திற"]):
            webbrowser.open("https://google.com")
            return f"{self.get_response_text('opening')} Google"
            
        elif any(word in command_lower for word in ["open youtube", "यूट्यूब खोलो", "யூடியூப் திற", "యూట్యూబ్ తెరవండి"]):
            webbrowser.open("https://youtube.com")
            return f"{self.get_response_text('opening')} YouTube"
            
        elif any(word in command_lower for word in ["open facebook", "फेसबुक खोलो", "ֆեյսբուկ திற"]):
            webbrowser.open("https://facebook.com")
            return f"{self.get_response_text('opening')} Facebook"
            
        # Music commands
        elif "play" in command_lower or "चलाओ" in command_lower or "பாடல்" in command_lower or "ప్లే" in command_lower:
            song_link = musicLibrary.find_song(command_lower)
            if song_link:
                webbrowser.open(song_link)
                for song in musicLibrary.music:
                    if song in command_lower:
                        return f"{self.get_response_text('playing')} {song}"
                return f"{self.get_response_text('playing')} music"
            else:
                return self.get_response_text("song_not_found")
                
        # News command
        elif any(word in command_lower for word in ["news", "खबर", "செய்தி", "వార్తలు"]):
            return self.get_news()
            
        # Time command
        elif any(word in command_lower for word in ["time", "समय", "நேரம்", "సమయం"]):
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            return f"{self.get_response_text('time')} {current_time}"
            
        # Language command
        elif any(word in command_lower for word in ["language", "भाषा", "மொழி", "భాష"]):
            return self.get_response_text("available_languages")
            
        # Greetings
        elif any(word in command_lower for word in ["hello", "hi", "नमस्ते", "हैलो", "வணக்கம்", "హలో", "হ্যালো"]):
            return self.get_response_text("hello")
            
        # Default: Use AI
        else:
            return self.ask_gemini(command)

    def listen_for_wake_word(self):
        """Listen for the wake word 'Jarvis' in any language"""
        try:
            with sr.Microphone() as source:
                print("🔊 Listening for 'Jarvis'...")
                self.recognizer.adjust_for_ambient_noise(source, duration=2)
                audio = self.recognizer.listen(source, timeout=LISTEN_TIMEOUT, phrase_time_limit=3)
                
            text = self.recognizer.recognize_google(audio, language=self.current_language)
            print(f"👂 Heard: {text}")
            return "jarvis" in text.lower()
            
        except sr.WaitTimeoutError:
            return False
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return False
        except Exception as e:
            print(f"❌ Listen error: {e}")
            return False

    def listen_for_command(self):
        """Listen for a command after wake word"""
        try:
            with sr.Microphone() as source:
                print("🎤 Listening for command...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=COMMAND_TIMEOUT)
                
            # Try with auto-detect language first, then fallback to current language
            try:
                command = self.recognizer.recognize_google(audio, show_all=False)
            except:
                command = self.recognizer.recognize_google(audio, language=self.current_language)
                
            print(f"💬 Command: {command}")
            return command
            
        except sr.WaitTimeoutError:
            return "timeout"
        except sr.UnknownValueError:
            return "unclear"
        except Exception as e:
            print(f"❌ Command error: {e}")
            return "error"

    def run(self):
        """Main loop for the voice assistant"""
        self.speak(self.get_response_text("welcome"))
        
        print("\n" + "="*60)
        print("🎯 MULTILINGUAL JARVIS - INDIAN LANGUAGES")
        print("="*60)
        print(f"🤖 AI: {'✅ ENABLED' if self.ai_enabled else '❌ DISABLED'}")
        print(f"🌐 Current Language: {SUPPORTED_LANGUAGES[self.current_language]['name']}")
        print("🗣️ Supported Languages: Hindi, Tamil, Telugu, Bengali, Marathi,")
        print("                       Gujarati, Kannada, Malayalam, Punjabi, English")
        print("💡 Say 'Jarvis' to activate")
        print("🌍 Say 'change to Hindi/Tamil/Telugu' to switch languages")
        print("⏹️  Press Ctrl+C to exit")
        print("="*60)
        
        while True:
            try:
                if self.listen_for_wake_word():
                    self.speak(self.get_response_text("listening"))
                    
                    command = self.listen_for_command()
                    
                    if command == "timeout":
                        self.speak(self.get_response_text("timeout"))
                    elif command == "unclear":
                        self.speak(self.get_response_text("unclear"))
                    elif command == "error":
                        self.speak("There was an error. Please try again.")
                    else:
                        response = self.process_command(command)
                        self.speak(response)
                        
            except KeyboardInterrupt:
                self.speak(self.get_response_text("goodbye"))
                print("\n👋 Jarvis stopped.")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                continue

def test_microphone():
    """Test if microphone is working"""
    recognizer = sr.Recognizer()
    
    print("🔍 Testing microphone...")
    try:
        with sr.Microphone() as source:
            print("🎤 Speak something in 3 seconds...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=3)
            
        text = recognizer.recognize_google(audio)
        print(f"✅ Microphone working! You said: '{text}'")
        return True
        
    except sr.WaitTimeoutError:
        print("❌ No speech detected")
        return False
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return False
    except Exception as e:
        print(f"❌ Microphone error: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Multilingual Jarvis Assistant...")
    
    if test_microphone():
        assistant = JarvisAssistant()
        assistant.run()
    else:
        print("❌ Please fix microphone issues first.")