
import speech_recognition as sr

import pyttsx3
import pyjokes
import wikipedia
import datetime
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print ('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command= command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, but siri loves me')
    elif 'are you single' in command:
        talk('no i am an artificial intelligence created by rupesh')
    elif 'cook' in command:
        talk('no i am busy')
    elif 'why am i lazy' in command:
        talk('because you dont bath')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again')
while True:
    run_alexa()

