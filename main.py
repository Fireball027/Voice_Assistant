import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
def sp_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Error in recognizing")

def speech_tx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()
    speech_tx("Hello!")


if __name__ == '__main__':

    if "Jarvis" in sp_text().lower():
        while True:
            data1 = sp_text().lower()

            if "your name" in data1:
                name = "My name is Jarvis"
                print(name)
                speech_tx(name)
            elif "old are you" in data1:
                age = "I am two years old"
                print(age)
                speech_tx(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%P")
                print(time)
                speech_tx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com")
            elif "joke" in data1:
                joke1 = pyjokes.get_joke(language="en")
                '''category="neutral"'''
                print(joke1)
                speech_tx(joke1)
            elif "exit" in data1:
                print("Goodbye")
                speech_tx("Goodbye")
                break
            time.sleep(10)
else:
    print("Thanks")
