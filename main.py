import speech_recognition as sr
import webbrowser
import pyttsx3
import string
# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   print(c)
   pass

if __name__ == "__main__":
    speak("Initializing jarvis")
    speak("test")
    

    while True:
        r=sr.Recognizer()
        
        print("Listening...")

        try:
            with sr.Microphone() as source:
                print("Recognizing...")
                audio = r.listen(source, timeout=2, phrase_time_limit=4)

                word = r.recognize_google(audio)
                print(f"Heard: {word}")  

            
                word_clean = word.lower().translate(str.maketrans('', '', string.punctuation))
                if "jarvis" in word_clean:
                    speak("ya")

                    with sr.Microphone() as source:
                        print("jarvis is active...")
                        audio = r.listen(source)
                        command= r.recognize_google(audio)

                        processCommand(command)
        except Exception as e:
            print(f"Error; {e}")

