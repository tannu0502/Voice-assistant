import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import musiclibary


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
   
def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour <12:
         speak("good morning")
     elif hour>=12 and hour<18:
         speak("good afternnon ")
     else:
         speak("good evening ")
     speak("i am here to help you")
     
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening")
        r.pause_threshold =1
        audio = r.listen(source)
        
    try:
        print("recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        #print(e)
        
        print('say that again please ..')
        return 'None'
    return query
def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()  # Start TLS encryption
        server.login('misstannu0805@gmail.com', 'tannu@123')  # Use environment variables for security
        server.sendmail('misstannu0805@gmail.com', to, content)
        server.close()
        speak("Email has been sent.")
    except Exception as e:
        print(e)
        speak("Sorry, I am unable to send the email at the moment.")
        
               
if __name__ == '__main__':
    wishMe()
    while True:  
        query = takeCommand().lower()
        
        if 'exit' in query:
            speak("Goodbye!")
            break  # Exit the loop
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia", "").strip()  # Clean up the query
            
            if query:  # Check if the query is not empty
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I could not find any information on that topic.")
        elif 'open google' in query:
                speak("Opening google")
                webbrowser.open("www.google.com")
        elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("www.youtube.com")
        elif "open linkedin" in query:
                speak("opening linkedin")
                webbrowser.open("https://linkedin.com")
        elif query.startswith("play"):
            print("attempting to play song..")
            parts = query.split(" ")
            if len(parts)>=2:
                song = parts[1]
                print("song name: ",song)
                link = musiclibary.music.get(song)
                if link:
                    webbrowser.open(link)
                else:
                    speak('song not found')
            else:
                speak("Invalid song name")
                
                
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")
            
        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to ="tannusgtian2002@gmail.com"
                sendEmail(to,content)
                speak("Email has send")
            except Exception as e:
                print(e)
                speak("sorry i am unable to send email at a moment")