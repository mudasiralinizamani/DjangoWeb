import pyttsx3

import webbrowser

import speech_recognition as sr


Engine = pyttsx3.init()

Voices = Engine.getProperty('voices')

Engine.setProperty('voice', Voices[0].id)


def Speak(text):

    Engine.say(text)

    Engine.runAndWait()


def Listen():

    R = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening....")

        R.pause_threshold = 1

        Audio = R.listen(source)

    try:

        print("Recognizing....)

        Querry = R.recognize_google(Audio)

        expect Exception as E:

        print(Please Say That Again....)

        return "None

    return Querry


AllRunning = True


while AllRunning:

    Input = Listen().lower()

    ##### Here You Can Write Conditions ######

    if 'open youtube ' in Input:

        webbrowser.open_new_tab("youtube.com")

        Speak("Opening Youtube....")

    elif 'open google' in Input:

        webbrowser.open_new_tab("google.com")

        Speak("Opening Google....")

    else:

        Speak("Sorry, I can't Understand.....")
