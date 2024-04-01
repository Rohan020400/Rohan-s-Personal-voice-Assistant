import pyttsx3
import speech_recognition 
import webbrowser
import os

engine = pyttsx3.init()
engine.setProperty('rate',150)
print("Welcome to Personal Voice assistant.")
engine.say("Welcome to Personal Voice assistant.")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def input_voice():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("LISTENING.....")
        speak("Listening")
        r.pause_threshold=1
        input_audio = r.listen(source)
    try:
        print("Recognizing")
        speak("Recognizing")
        query = r.recognize_google(input_audio, language = 'en-in')
        print("You said:"+ query)
    except Exception as e:
        print(e)
        print("I didn't understand")
    return query


if __name__== '__main__':
    f = True
    name = ''
    print("What is your name ?")
    speak("What is your name "+name)
    s = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        n = s.listen(source)
        name = s.recognize_google(n)
    print("Hello "+name)
    speak("Hello "+ name)
    
    print("How can I help you?")
    speak("How can I help you?")
    while f:
        command = input_voice().lower()
        if 'google' in command:
            speak("Opening google.com")
            webbrowser.open("www.google.com")
        elif 'chrome' in command:
            speak("Opening google chrome")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
        elif 'spotify' in command:
            webbrowser.open("www.spotify.com")
        elif 'github' in command:
            webbrowser.open("www.github.com")
        elif 'youtube' in command:
            webbrowser.open("www.Youtube.com")
        elif 'open whatsapp' in command:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'sleep':
            exit(0)
        
         





         






