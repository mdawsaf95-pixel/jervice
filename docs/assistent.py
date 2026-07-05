import os
import speech_recognition as sr
import pyttsx3

# Use the newer `google.genai` client for Jervice access.
# If you want voice mode to work, install PyAudio/PyAudio-compatible drivers separately.
try:
    from google import genai
except Exception:
    genai = None

# ১. ভয়েস এবং স্পিচ ইঞ্জিন সেটআপ
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # voices[0] পুরুষ কণ্ঠ, voices[1] নারী কণ্ঠ
engine.setProperty('rate', 180) # কথা বলার গতি

def speak(text):
    """এই ফাংশনটি এআই-এর উত্তর মুখে বলবে"""
    print(f"Jervice: {text}")
    engine.say(text)
    engine.runAndWait()

# ২. Jervice AI সেটআপ
GOOGLE_API_KEY = os.environ.get("JERVICE_API_KEY")
MODEL_NAME = "models/gemini-2.5-flash"
client = None
if genai:
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY) if GOOGLE_API_KEY else genai.Client()
    except Exception:
        client = None


def ask_jervice(prompt):
    """Jervice থেকে উত্তর নেওয়ার ফাংশন"""
    if not client:
        return "Jervice client is not configured. Check google.genai installation and JERVICE_API_KEY."

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"Jervice: Respond in a very short, crisp and friendly manner: {prompt}",
        )
        if hasattr(response, 'text') and response.text:
            return response.text
        return str(response)
    except Exception as e:
        return f"Sorry, I am facing a connection issue with my brain: {e}"

# ৩. কথা শোনার মূল ফাংশন
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US') 
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Could not request results.")
        return ""

# অ্যাসিস্ট্যান্ট চালু করা
if __name__ == "__main__":
    speak("Hello sir!  i am Jervice . How can I help you?")
    
    while True:
        user_input = listen().lower()
        
        if not user_input:
            continue
            
        # বন্ধ করার কমান্ড
        if "exit" in user_input or "stop" in user_input or "goodbye" in user_input:
            speak("Goodbye! Have a great day ahead.")
            break
            
        # উত্তর নেওয়া এবং মুখে বলা
        ai_response = ask_jervice(user_input)
        speak(ai_response)
