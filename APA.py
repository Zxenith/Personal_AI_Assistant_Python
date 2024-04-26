import datetime
import sys
import pyttsx3 as pt3  # Importing the text-to-speech library
import speech_recognition as sr  # Importing the speech recognition library
import datetime as dt
import os
import cv2  # Importing OpenCV for camera functionality
from requests import get
import wikipedia  # Importing Wikipedia module for searching
import webbrowser as wb
import time

# Engine initialization.
engine = pt3.init('sapi5')

# Getter property
voices = engine.getProperty('voices')

# print(voices[1].id)

# Defining voice ID and avoiding noises

# Setter property
engine.setProperty('voices', voices[0].id)

# Text to speech
def speak(audio):
    """Function used for converting text to audio"""
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Speech to text
def commander():
    recognizer = sr.Recognizer()  # For speech recognition

    with sr.Microphone() as source:  # Considering microphone as the source

        recognizer.pause_threshold = 1  # For generating pauses between sentences

        audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)

    # Error handling
    print("Listening...")

    try:
        query = recognizer.recognize_google(audio, language='en-in')
        print(f'You said: \n{query}')

    except:
        print("Sorry I did not hear you properly")
        speak("Please say that again.")
        return 'none'
    return query


# Wishing command execution
def wishme():
    speak("What is your name?")
    name = commander()
    hour = int(dt.datetime.now().hour)

    if hour >= 4 and hour < 12:
        speak(f'Good Morning {name}')

    elif hour >= 12 and hour <= 17:
        speak(f'Good Afternoon {name}')

    else:
        speak(f'Good Evening {name}')

    speak("My name is apa. How can I help you?")


if __name__ == "__main__":
    # commander()
    wishme()
    while True:

        query = commander()
        query = query.lower()

        # Taking tasks

        if 'open notepad' in query:
            # Open Notepad
            path = "C:\\Windows\\System32\\notepad.exe"
            speak("Opening Notepad")
            os.startfile(path)


        elif 'open counter strike' in query or 'open CS' in query:
            # Open Counter Strike
            path = "C:\\Users\\akars\\OneDrive\\Desktop\\Counter-Strike Global Offensive.url"
            speak("Opening Counter Strike")
            os.startfile(path)


        elif 'open command prompt' in query or 'open cmd' in query:
            # Open Command Prompt
            speak('Opening Command Prompt')
            os.system('start cmd')


        elif 'open camera' in query:
            # Open Camera
            cam = cv2.VideoCapture(0)

            while True:
                ret, img = cam.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if cv2.getWindowProperty('webcam', cv2.WND_PROP_VISIBLE) < 1:
                    break
                if k == 27:
                    break

            cam.release()
            cv2.destroyAllWindows()


        elif 'play music' in query:
            # Play Music
            music = "C:\\404\\VirtualAssistant\\Music"
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))


        elif 'ip address' in query:
            # Get IP Address
            ip = get('https://api.ipify.org').text  # Getting IP through API call
            speak(f'Your IP Address is {ip}')


        elif 'wikipedia' in query:
            # Search on Wikipedia
            speak('Searching in Wikipedia, please wait...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak(f'According to Wikipedia {results}')


        elif 'open youtube' in query:
            # Open YouTube
            speak('Opening YouTube')
            wb.open("www.youtube.com")


        elif 'open google' in query:
            # Open Google and search
            speak('Sir, What should I search on Google?')
            google_it = commander()
            wb.open(f'{google_it}')


        elif 'how are you' in query:
            # Respond to how are you
            speak('I am doing well. I hope you are also doing well.')
        

        if 'no thank' in query:
            speak('Thank you for trusting me. Have a good day!')
            sys.exit()
            break

        time.sleep(4)
        speak('Sir, can I do something else for you?')
