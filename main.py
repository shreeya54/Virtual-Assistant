import time
from Jarvis import JarvisAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import openai
import pyjokes
import times
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.config import config
from Jarvis.features import weather
from Jarvis.features import wolf

obj = JarvisAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello saya", "saya", "wake up saya", "you there saya", "time to work saya", "hey saya",
             "ok saya", "are you there"]
GREETINGS_RES = ["always there for you ", "i am ready ",
                 "your wish my command", "how can i help you maam?", "i am online and ready"]



def speak(text):
    obj.tts(text)
    #jarvis.setText(text)



app_id = config.wolframalpha_id


def computational_intelligence(question): 

    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except Exception as e:
        print(e)
        speak("Sorry mam I couldn't fetch your question's answer. Please try again ")
        return None
    
def startup():
    speak("Checking the internet connection")
    speak("Now I am online")
    
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Assistant. Online and ready. Please tell me how may I help you")
# if __name__ == "__main__":


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        wish()

        while True:
            command = obj.mic_input()

            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"mam the time is {time_c}")

            elif re.search('launch', command):
                dict_app = {
        
                    'browser':'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
                }
                try:
                    app = command.split(' ', 1)[1]
                    path = dict_app.get(app)

                    if path is None:
                        speak('Application path not found')
                        print('Application path not found')

                    else:
                        speak('Launching: ' + app + 'for you mam!')
                        print('launching browser')
                        obj.launch_any_app(path_of_app=path)
                        print('after launch')
                except:
                    speak("Failed to Launch, specify what you want to launch")
                    
            elif "close browser" in command or "close the browser" in command: 
                speak("Closing browser for you mam")
                os.system("taskkill /f /im msedge.exe")

            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)    
                speak(f'Alright mam !! Opening {domain}')
                print(open_result)

            elif re.search('temperature', command):
                city = command.split(' ')[-1]
                weather_res = obj.weather() #tryt
                print(weather_res)
                
                speak(weather_res)

            elif re.search('tell me about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry mam. I couldn't load your query from my database. Please try again")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of Nepal')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day!!..')

            elif 'search' in command:
                print("search detected in input")
                g_reply=wolf.wolf_search(command)
                #g_reply=obj.search_anything_google(command)

                speak(g_reply)
            
            elif "play music" in command or "hit some music" in command:
                music_dir = "D://song"
                songs = os.listdir(music_dir)
                for song in songs:
                    os.startfile(os.path.join(music_dir, song))


            elif "stop music" in command or "close music player" in command:
                speak("Stopping music")
                os.system("taskkill /f /im Microsoft.Media.Player.exe")
                    

            elif 'youtube' in command:
                video = command.split(' ')[1]
                speak(f"Okay, playing {video} on youtube")
                pywhatkit.playonyt(video)

            #elif "close youtube" in command or "close the youtube" in command:
                #speak("Closing youtube mam")
                #os.system("taskkill /f / im http://www.youtube.com")
        
            elif "calculate" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)
            
            elif "what is" in command or "who is" in command:
                answer = wolf.wolf_search(command)
                speak(answer)

            elif "what do i have" in command or "do i have plans" or "am i busy" in command:
                obj.google_calendar_events(command)

            if "make a note" in command or "write this down" in command or "remember this" in command:
                speak("What would you like me to write down?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that")
                

            elif "close the note" in command or "close notepad" in command:
                speak("Okay, closing notepad")
                os.system("taskkill /f /im Notepad.exe")

            if "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                try:
                    current_loc, target_loc, distance = obj.location(place)
                    city = target_loc.get('city', '')
                    state = target_loc.get('state', '')
                    country = target_loc.get('country', '')
                    time.sleep(1)
                

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Here is the map of your location maam."
                    speak(res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry mam, I coundn't fetch your current location. Please try again")
                

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright mam, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"D:\\Shreeya\\ScreenshotsV\\{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in command:
                try:
                    img = Image.open(name)
                    img.show(img)
                    speak("Here it is mam")
                    time.sleep(2)

                except Exception as e:
                    print(e)
                    speak("Sorry mam, I am unable to display the screenshot")
            
            elif "ask gpt" in command:
                ask=command+"in very short"
                output=openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    
                    {"role": "assistant", "content": "Reply anything asked about"},
                    {"role": "user", "content": f"{ask}"}
                    ]
                )
                print(output['choices'][0]['message']['content'])
                


            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("mam, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak("mam, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

           # elif "calculate" in command or "what is" in command:
                # query = command
                # answer = computational_intelligence(query)
                 #speak(answer)

            

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright mam, going offline. It was nice working with you")
                sys.exit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
    def setText(self,text):
        self.ui.textBrowser_3.setText(text)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
