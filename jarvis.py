# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:17:45 2020

@author: Suhanshu
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speak function will speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Initializing Jarvis...")

def wishMe():
    hour=int(datetime.datetime.now().hour)
   
    if hour>=0 and hour<12:
        speak("Good Morning,Suhanshu")
    elif hour>=12 and hour<18:
        speak("Good Afternoon,Suhanshu")
    else:
        speak("Good Evening,Suhanshu")
    speak("I am Jarvis,How may I help you?") 

wishMe()
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

query=takeCommand()
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('patel1.suhanshu@gmail.com', 'Hellokaun96')
    server.sendmail('patel1.suhanshu@gmail.com', to, content)
    server.close()
    

if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    speak(results)
    
elif 'open youtube' in query.lower():
    url="youtube.com"
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'open google' in query.lower():
    url="google.com"
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
elif 'play music' in query.lower():
    songs_dir=r"C:\Users\Suhanshu\Downloads\Music"
    songs=os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[0]))
    
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, the time is {strTime}")
            

elif 'open code' in query.lower():
    codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
            

elif 'email to me' in query.lower():
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "suhanshu.patel@yahoo.in"    
        sendEmail(to, content)
        speak("Email has been sent!")
                            
    except Exception as e:
        print(e)
        speak("Sorry . I am not able to send this email")
      

                


























