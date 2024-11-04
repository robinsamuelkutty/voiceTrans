
import speech_recognition as sr  
import googletrans   

import pyttsx3 
engine=pyttsx3.init()

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("clearing the background noices.....")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    langoutput=input('type the language code of your language ')
    print("Speak Now")
    voice=recognizer.listen(source,timeout=2)
    print("Done recording")
try:
    print("Recognizing..")
    text=recognizer.recognize_google(voice,language=langoutput)
    print(text)
except Exception as ex:
    print(ex)

def trans():
    langinput=input("Type the language code you want to translate ")
    translator=googletrans.Translator()
    translation=translator.translate(text,dest=langinput)
    print(translation.text)
    engine.say(translation.text)
    engine.runAndWait()

trans()
    