import webbrowser as wb
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import pyautogui
import psutil
import pyjokes
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir")
    time()
    date()
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good afternoon sir!")
    elif 18 <= hour < 24:
        speak("Good evening sir")
    else:
        speak("Good night!")

    speak("JARVIS is at your service please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashuvishwakarma009@gmail.com', 'Password')
    server.sendmail('ashuvishwakarma009@gmail.com', to, content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:\\Users\\Ashu\\Jarvis\\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery= psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__== "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace("wikipedia", "")
            result= wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak('what should i do ?')
                content= takeCommand()
                to = 'ashusharma3535@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent')
            except  Exception as e:
                print(e)
                speak('Unable to send the email')


        elif 'search in chrome' in query:
            speak("what should i search?")
            chromepath='C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ '.com')
        
        elif 'logout' in query:
            os.system("shutdown -1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'kill the window' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            song_dir = 'D:\\Music'
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0]))
        
        elif 'screenshot' in query:
            screenshot()
            speak("Ok Done!")

        elif 'cpu' in query:
            cpu()
        elif 'tell me a joke' in queryL:
            jokes()

        elif 'offline' in query:
            quit()
