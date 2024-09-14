import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os #pip install os
import smtplib #pip install smtplib
import pyautogui #pip install PyautoGui 
import time #pip install time
import random # pip install random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

voice = [0,1]
x = random.choice(voice)
engine.setProperty('voice', voices[x].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Akshit")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Akshit")   

    else:
        speak("Good Evening! Akshit")  

    speak("Please tell me how may I help you, aap kesee hoo")       

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/z/")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            #Write the path of your vs code here
            codePath = ""
            os.startfile(codePath)
        elif 'hello' in query:
            webbrowser.open("https://www.google.com")
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                #Write your Email here
                to = "akshitjain6661@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")
        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'music' in query or 'song' in query:
            webbrowser.open("https://www.youtube.com/")
            s = 'hindi songs'
            time.sleep(5)
            pyautogui.keyDown("/")
            for i in s:
                pyautogui.keyDown(i)
            else:
                pyautogui.keyDown("enter")
        elif 'search for' in query or 'search on google' in query:
            webbrowser.open("https://www.google.com/")
            time.sleep(3)
            query.strip('search for')
            for i in query:
                pyautogui.keyDown(i)
            pyautogui.keyDown("enter")
            pyautogui.keyDown("enter")
        elif 'search on youtube' in query:
            webbrowser.open('https://youtube.com/')
            time.sleep(5)
            pyautogui.keyDown("/")
            for i in query:
                pyautogui.keyDown(i)
            else:
                pyautogui.keyDown("enter")
        elif 'end' in query or 'stop' in query or 'thank you' in query:
            speak("Thank you for using me and have a nice day !!!")
            break