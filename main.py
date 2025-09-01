import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
   print(c)

if __name__ == "__main__":
    speak("Initializing jarvis")
    

    while True:
        r=sr.Recognizer()
        
        print("Listening...")

        try:
         with sr.Microphone() as source:
            print("Recognizing...")
            audio = r.listen(source, timeout=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
               speak("ya")
               with sr.Microphone() as source:
                print("Sam is active...")
                audio = r.listen(source, timeout=1)
                command= r.recognize_google(audio)

                processCommand()
        except Exception as e:
            print(f"Error; {e}")

