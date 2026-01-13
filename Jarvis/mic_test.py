# mic_test.py - Simple microphone test
import speech_recognition as sr

def simple_test():
    r = sr.Recognizer()
    
    print("🎤 SIMPLE MICROPHONE TEST")
    print("Speak something when you see 'Listening...'")
    print("Press Ctrl+C to stop\n")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...", end=" ", flush=True)
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5)
                
            text = r.recognize_google(audio)
            print(f"✅ You said: '{text}'")
            
        except sr.WaitTimeoutError:
            print("❌ No speech - try again")
        except sr.UnknownValueError:
            print("❌ Unclear - speak clearly")
        except KeyboardInterrupt:
            print("\n👋 Test stopped")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    simple_test()