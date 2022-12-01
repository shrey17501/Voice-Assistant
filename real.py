from click import open_file
import pyttsx3 
import speech_recognition as sr 
import datetime
import os
import smtplib
import spacy
import json
from googletrans import Translator

translator = Translator()

engine = pyttsx3.init('sapi5')
voices_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_HeeraM"
engine.setProperty('voice', voices_id)
voices = engine.getProperty('voices')

engine.setProperty('rate', 200)

nlp = spacy.load("en_core_web_sm")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("What kind of problem are you suffering from?")
    

nouns = []
out = 'abc'

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        doc = nlp(str(query))
        for token in doc:
            if (token.pos_ == "NOUN" and token.dep_ == "dobj") or (token.pos_ == "NOUN" and token.dep_ == "attr"):
                nouns.append(token)
        for token in doc:
            if token.pos_ == "VERB" and token.dep_ == "ROOT":
                nouns.append(token)
        for token in doc:
            if (token.pos_ == "ADJ" and token.dep_ == "acomp") or (token.pos_ == "ADJ" and token.dep_ == "amod"):
                nouns.append(token)
        for ent in doc.ents:
            if ent.label_ == "DATE":
                nouns.append(ent)
               
  
    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query

def takehindi():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "hi-IN")
        print('You said : {}'.format(query))
        out = translator.translate(str(query), dest="en")
        print(out)
        #speak(out.text)
        doc = nlp(out.text)
        for token in doc:
            if (token.pos_ == "NOUN" and token.dep_ == "dobj") or (token.pos_ == "NOUN" and token.dep_ == "attr"):
                nouns.append(token)
        for token in doc:
            if token.pos_ == "VERB" and token.dep_ == "ROOT":
                nouns.append(token)
        for token in doc:
            if (token.pos_ == "ADJ" and token.dep_ == "acomp") or (token.pos_ == "ADJ" and token.dep_ == "amod"):
                nouns.append(token)
        for ent in doc.ents:
            if ent.label_ == "DATE":
                nouns.append(ent)
        print(nouns)

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    
#10.16.5.177
 
    while True:
            query = takeCommand().lower()
            for t in nouns:
                if str(t) == 'cough':
                    myjsonfile = open('head.json','r')
                    jsondata = myjsonfile.read()
                    obj = json.loads(jsondata)
                    speak(str(obj['second']))
                    while True:
                        query = takeCommand().lower()
                        myjsonfile = open('head.json','r')
                        jsondata = myjsonfile.read()
                        obj = json.loads(jsondata)
                        speak(str(obj['first']))
                        while True:
                            query = takeCommand().lower()
                            for t in nouns:
                                if str(t) == 'dry':
                                    myjsonfile = open('head.json','r')
                                    jsondata = myjsonfile.read()
                                    obj = json.loads(jsondata)
                                    speak(str(obj['third']))
                                    exit()
                                elif str(t) == 'wet':
                                    myjsonfile = open('head.json','r')
                                    jsondata = myjsonfile.read()
                                    obj = json.loads(jsondata)
                                    speak(str(obj['four']))
                                    exit()
                                elif str(t) == 'asthma':
                                    myjsonfile = open('head.json','r')
                                    jsondata = myjsonfile.read()
                                    obj = json.loads(jsondata)
                                    speak(str(obj['five']))
                                    exit()
                    
                elif (str(t) == 'joint pain') or (str(t) == 'jointpain'):
                    myjsonfile = open('head.json','r')
                    jsondata = myjsonfile.read()
                    obj = json.loads(jsondata)
                    speak(str(obj['second']))
                    while True:
                        query = takeCommand().lower()
                        myjsonfile = open('head.json','r')
                        jsondata = myjsonfile.read()
                        obj = json.loads(jsondata)
                        speak(str(obj['six']))
                        while True:
                            query = takeCommand().lower()
                            for t in nouns:
                                if str(t) == 'spinal':
                                    myjsonfile = open('head.json','r')
                                    jsondata = myjsonfile.read()
                                    obj = json.loads(jsondata)
                                    speak(str(obj['seven']))
                                    exit()
                                elif str(t) == 'leg':
                                    myjsonfile = open('head.json','r')
                                    jsondata = myjsonfile.read()
                                    obj = json.loads(jsondata)
                                    speak(str(obj['eight']))
                                    exit()
                                elif str(t) == 'other body':
                                    myjsonfile = open('head.json','r')
                                    jsondata = myjsonfile.read()
                                    obj = json.loads(jsondata)
                                    speak(str(obj['nine']))
                                    exit()
                    
                elif str(t) == 'hairfall':
                    myjsonfile = open('head.json','r')
                    jsondata = myjsonfile.read()
                    obj = json.loads(jsondata)
                    speak(str(obj['second']))
                    while True:
                        query = takeCommand().lower()
                        myjsonfile = open('head.json','r')
                        jsondata = myjsonfile.read()
                        obj = json.loads(jsondata)
                        speak(str(obj['ten']))
                        exit()

                elif str(t) == 'uk':
                    myjsonfile = open('head.json','r')
                    jsondata = myjsonfile.read()
                    obj = json.loads(jsondata)
                    speak(str(obj['second']))
                    while True:
                        query = takeCommand().lower()
                        myjsonfile = open('head.json','r')
                        jsondata = myjsonfile.read()
                        obj = json.loads(jsondata)
                        speak(str(obj['eleven']))
                        exit()