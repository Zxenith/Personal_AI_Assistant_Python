import datetime

import pyttsx3 as pt3
import speech_recognition as sr
import datetime as dt

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
def commander(phrase_time_limit=5):
    recognizer = sr.Recognizer() #For recognition of speech detection

    with sr.Microphone() as source: #Considering microphone as the source

        recognizer.pause_threshold = 1 #For generating pauses between sentences

        audio = recognizer.listen(source,timeout=1,phrase_time_limit=phrase_time_limit)

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
    name = commander(5)
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
