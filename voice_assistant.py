import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pyjokes
import shutil
from ecapture import ecapture as ec
# make sure that each library is installed,
# if you don't know, in terminal or command prompt type:>pip install <name of the library>

engine = pyttsx3.init()
rate = engine.setProperty('rate', 200)  # this sets the rate of the responsive voice, how fast the program will talk
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)  # the most important one is the index [X] of the narrator
# see the voice_index code and configuration file to have the needed narrator and correct index


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Bună dimineața !")
# the program will respond with Good morning if it's between that interval

    elif hour >= 12 and hour < 18:
        speak("Bună ziua !")
# the program will respond with Good Day or Good Afternoon if it's between that interval

    else:
        speak("Bună seara !")
# the program will respond with Good Evening

    assname = ("Alex")
    speak("Sunt asistentul dumneavoastră"+assname)
# The assistant is introducing himself


def username():
    speak("Cum vă numiți ?")
# The assistant ask your name

    uname = takecommand()
# The assistant will take your said name

    speak("Bine ai venit"+uname)
# The assistant will welcome you with your name
    columns = shutil.get_terminal_size().columns

    print("...".center(columns))
    print("Bine ai venit", uname.center(columns))
# The assistant will show in terminal

    speak("Cum te pot ajuta ?")
# The assistant will ask how can it help you


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Ascult...")
        r.pause_threshold = 1
        audio = r.listen(source)
# This defines the 'Hearing...' function, the listening

    try:
        print("Recunoastere...")
# The assistant is recognizing your speech

        query = r.recognize_google(audio, language='ro-Ro')
# This is another important step, the language tag, for romanian is ro-Ro and english en-GB(english UK)
# For other supported languages check https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages

        print(f"Ati spus: {query}\n")
# The assistant will show in terminal the recognized speech also you will see the precision rate

    except Exception as e:
        print(e)
        speak('Nu înțeleg.')
        print("Nu înțeleg.")
        return "None"
# The exception if the assistant doesn't understand or cannot perform the task

    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishme()
    username()
# this formula clears everything that took the command up in the code
# now it is going only on serving the functionalities

    while True:

        query = takecommand().lower()
# as you can see the structure of the functionalities is simple without defining each command as a different function
# just by adding and elif of deleting it, you can remove or add a functionality

        if 'youtube' in query:
            speak("Acuma voi deschide youtubu-ul")
            url = 'https://www.youtube.com/'
            path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# this is for where my chrome.exe application can be found, you can choose and replace
# otherwise the program will open the default browser
            webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('mybrowser').open(url)
# if you say anything containing youtube word,the assistant will open the youtube URL
# this gives a high confidence rate and specific target functionality

        elif 'google' in query:
            speak("Acuma voi deschide gugălul")
            url = 'https://www.google.com/'
            path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('mybrowser').open(url)
# if you say anything containing google word,the assistant will open the google URL

        elif 'ce mai faci' in query:
            speak("Sunt foarte  bine, mulțumesc de întrebare")
            speak("Tu ce mai faci ?")
# simple chat with the assistant

        elif 'bine' in query or "sunt ok" in query:
            speak("E bine să știu că totul e bine.")
# simple chat with the assistant

        elif "cine te a creat" in query or "cine este creatorul" in query:
            speak("Am fost creat de Andrei Ciuca.")
# simple chat with the assistant

        elif 'glumă' in query:
            rate = engine.setProperty('rate', 160)
            engine.setProperty('voice', voices[4].id)
            speak(pyjokes.get_joke())
            rate = engine.setProperty('rate', 200)
            engine.setProperty('voice', voices[3].id)
# here the program by hearing the word gluma-joke, it will start telling a joke from the library
# because the library is only in english, we call the voice index again first time for an english narrator
# and then call it again in our language to be like before

        elif 'caută' in query:

            query = query.replace("caută", "")
            url = f'https://google.com/search?q={query}'
            path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('mybrowser').open(url)
# this is a search tool, whatever comes after the word cauta-search, the program will open the browser with searches

        elif "sunt eu" in query:
            speak("Dacă vorbești, în mod sigur ești un om.")
# simple chat with the assistant

        elif 'word' in query:

            speak("Deschid fișierul word")
            power = r"C:\Users\Andrei\Documents\CV\CV.docx"
            os.startfile(power)
# This functionality can be used to automatically open by voice documents in your computer

        elif "unde este" in query:

            query = query.replace("unde este", "")
            location = query
            speak("Utilizatorul a cerut să Localizeze")
            speak(location)
            url = f'https://www.google.com/maps/place/{query}'
            path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('mybrowser').open(url)
# this is almost the same like searching on google functionality, but this time is searches the address on google maps
# the assistant will also say back the location you wanted to localize

        elif "fotografie" in query:
            speak('Voi face o fotografie imediat')
            ec.capture(0, "Alex Camera ", "img.jpg")
# by hearing the word fotografie-photograph, the program will open and make a photo
# with the default camera on your device

        elif "notițe" in query:
            speak("Deschid notițele")
            file = open("Alex.txt", "r")
            print(file.read())
# this is related to the Alex.txt file in github, by saying notite-notes it will open in the terminal the text written

        elif "wikipedia" in query:

            speak("Acuma voi deschide wikipedia")
            url = 'https://www.wikipedia.com/'
            path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            webbrowser.register('mybrowser', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('mybrowser').open(url)
# if you say anything containing wikipedia word,the assistant will open the wikipedia URL

        elif 'mulțumesc' in query:
            speak('Cu plăcere, ce altceva pot face pentru tine')
# simple chat with the assistant

        elif 'la revedere' in query:
            speak("Mulțumesc că mi-ai acordat timpul tău")
            exit()
# by saying la revedere-goodbye, the program stops