import datetime
import pyttsx3 as pt3
import speech_recognition as sr
import datetime as dt
import os
import cv2

#Engine initialisation.
engine = pt3.init('sapi5')

#Getter property
voices = engine.getProperty('voices')

# print(voices[1].id)

#Defining voice ID and avoiding noices

#Setter property
engine.setProperty('voices', voices[0].id)

#Text to speech
def speak(audio):
    """Function used for converting text to audio"""
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#Speech to text
def commander():
    recognizer = sr.Recognizer() #For recognition of speech detection

    with sr.Microphone() as source: #Considering microphone as the source

        recognizer.pause_threshold = 1 #For generating pauses between sentences

        audio = recognizer.listen(source,timeout=1,phrase_time_limit=5)

    #Error handling must be further avoided.

    try:
        print("Listening...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f'You said: \n{query}')

    except:
        print("Sorry I did not hear you properly")
        speak("Please say that again.")
        return 'none'
    return query


#Wishing command execution
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
    # wishme()
    while True:

        query = commander()
        query = query.lower()

        #Taking tasks

        if 'open notepad' in query:
            path = "C:\\Windows\\System32\\notepad.exe"
            speak("Opening Notepad")
            os.startfile(path)
            break


        elif 'open counter strike' in query or 'open CS' in query:
            path = "C:\\Users\\akars\\OneDrive\\Desktop\\Counter-Strike Global Offensive.url"
            speak("Opening Counter Strike")
            os.startfile(path)
            break


        elif 'open command prompt' in query:
            speak('Opening Command Prompt')
            os.system('start cmd')
            break


        elif 'open camera' in query:
            cam = cv2.VideoCapture(0)

            while True:
                ret, img = cam.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if cv2.getWindowProperty('webcam', cv2.WND_PROP_VISIBLE) < 1:
                    break
                if k == 27:
                    break

            cam.release()
            cv2.destroyAllWindows()
            break

        elif 'play music' in query:
            music = "C:\\404\\VirtualAssistant\\Music"
            songs = os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))
            break
