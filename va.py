import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi im V A, how may I help you")


def takecommand():
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

        query = takecommand().lower()

        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)



        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.bing.com/search?q={cm}")

        elif "open youtube" in query:
            speak("sir,what should i search on youtube")
            x = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")

        elif "open meet" in query:
            webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        elif "play music" in query:
            music_dir = 'C:\\Users\\saumen\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "play video" in query:
            speak("ok i am playing videos")
            video_dir = 'C:\\Users\\saumen\\Music'
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[4]))

        elif "play song on cloud" in query:
            speak("which song do you want to play?")
            p = takecommand()
            webbrowser.open(f"https://soundcloud.com/search?q={p}")



        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open project csv" in query:
            codePath = "C:\\Users\\saumen\\Documents\\vgsales.csv"
            os.startfile(codePath)

        elif "open micro" in query:
            codepath = "C:\\Program Files (x86)\\MCU 8051 IDE\\mcu8051ide.exe"
            os.startfile(codepath)
            speak('opening sir')

        elif "open command prompt" in query:
            os.system('start cmd')



        elif "why do you exist?" in query:
            speak("I don't know,you're the one who made me you tell me")


        elif "what is your name?" in query:
            speak("Thanks for asking my name, its V A by the way")


        elif "send mail" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "receiver email address"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")


        elif "exit" in query:
            speak("hope you were satisfied with my service, have a good day")
            sys.exit()
