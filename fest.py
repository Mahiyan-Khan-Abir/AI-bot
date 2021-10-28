# -*- co*9ding: utf-8 -*-
"""
Created on Sat Oct 16 20:52:43 2021

@author: Lite Computer
"""

import os
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import webbrowser
import wikipedia
import pandas as pd



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon,sir!")   

    else:
        speak("Good Evening,sir!")  

    speak("Please speak")
    
def TakeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query
def learning():

        speak("please state your question sir")
        uinp = TakeCommand().lower()
        inp = []
        inp.append(uinp)
        inputs = pd.DataFrame(data = inp, columns=['OUTS'])
        inputs.to_csv('test.csv', mode='a', header=False)
        
        speak("what can be the posible answer sir")
        uout = TakeCommand().lower()
        out = []
        out.append(uout)
        outputs = pd.DataFrame(data = out, columns=['OUTS'])
        outputs.to_csv('test.csv', mode ='a', header = False)
    
    
        # print(inp)
def res():
    try:
            df = pd.read_csv('test.csv')
            
            i= df[df['OUTS']== query ].index.values
            ii = i[0]
            
            iii = df.loc[(ii+1)].at["OUTS"]
                
            # print(iii)
            speak(iii)
    except Exception:
            speak("sorry sir, i do not know that. if you want to initiate the learning function please say yes otherwise say no")
            q = TakeCommand().lower()
            if 'yes' in q:
                learning()
            elif 'no' in q:
                speak("sorry for the inconvinient")
                res()
    
if __name__ == "__main__":
    Greetings()
    while True:

        query = TakeCommand().lower()
        res()
        try:
            # basic()
            if 'initiate learning' in query:
                learning()
                
        except Exception:
            speak("sorry sir, i do not know. i am still learning")
            # cm = TakeCommand().lower()
            # if 'yes' in cm:
            #     print("Learning phase started")
            #     learning()
            # else:
            #     speak("please try again sir")
        if 'information' in query:
            try:
                speak('obviously sir')
                #query = query.replace("information", "")
                #results = wikipedia.summary(query, sentences=2)
                #speak("pardon the delay sir")
                #print(results)
                #speak(results)
            except Exception:
                speak('There are too many results sir, for precise result you may want to do this manually! I am really Sorry that i could not be useful')
        # else: