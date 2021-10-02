import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os 
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio
os.system('cls')
engine = pyttsx3.init('sapi5')
engine.setProperty("rate",178)
engine.setProperty("volume",0.55)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(text):
  engine.say(text)
  engine.runAndWait()
  
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
      speak("Hello,Good Morning")
      print("Hello,Good Morning")
      
    elif hour >= 12 and hour < 18:
      speak("Hello,Good Afternoon")
      print("Hello,Good Afternoon")
      
    elif hour >= 18 and hour < 24:
      speak("Hello,Good Evening")
      print("Hello,Good Evening")
      
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
          print("Listening...")
          audio = r.listen(source)
          
          try:
            statement = r.recognize_google(audio,language = 'en-in')
            print(f"user said:{statement}\n")
            
          except Exception as e:
            #speak(" ")
            return "None"
          return statement
 
print("Loading ur AI personal assistant HOI")
speak("Loading ur AI personal assistant HOI")
wishMe()

if __name__=='__main__':
  
  while True:
    statementssss = takeCommand().lower()
    
    if "hey" in statementssss:
      speak("How can I help u")
      statement = takeCommand().lower()
      
      if statement == 0:
        engine.runAndWait()
        
      if "goodbye" in statement or "okay bye" in statement or "stop" in statement:
        speak('ur personal assistant HOI is shutting down,Good bye')
        print('ur personal assistant HOI is shutting down,Good bye')
        break
        
      #if 'wikipedia' ini statement:
      #  speak('Searching Wikipedia...')
      #  statement = statement.replace("wikipedia"," ")
      #  results = wikipedia.summary(statement, sentences = 3)
      #  speak("According to Wikipedia")
      #  print(results)
      #  speak(results)
      
      elif 'youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        #time.sleep(5)
        
      elif 'papago' in statement:
        webbrowser.open_new_tab("https://papago.naver.com")
        speak("papago is open now")
        #time.sleep(5)
      
      elif 'google' in statement:
        webbrowser.open_new_tab("https://google.com")
        speak("Google chrome is open now")
        #time.sleep(5)
        
      elif 'gmail' in statement:
        webbrowser.open_new_tab("https://gmail.com")
        speak("Gmail is open now")
        #time.sleep(5)
        
      elif 'time' in statement:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
        
      elif 'news' in statement:
        news = webbrowser.open_new_tab("https://www.nytimes.com/")
        speak('Here are some headlines frome the Times of Newyork, Happy reading')
        #time.sleep(5)
      
      #elif 'camera' in statement or 'take a photo' in statement:
      #  ec.capture(0, "robo camera", "img.jpg")
        
      #elif "song" in statement:
      #  webbrowser.open_new_tab("https://music.youtube.com")
      #  speak("Youtube music is open now")
        #time.sleep(5)
      elif "music" in statement:
        speak("What do u want")
        state = takeCommand().lower()
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={state}")
        speak("searching")
        #time.sleep(5)
      
      elif "find" in statement:
        speak("Tell me What u want")
        stat = takeCommand().lower()
        webbrowser.open_new_tab(f"https://google.com/search?q={stat}")
        speak("searching...")
        
    else:
      continue
      
 
