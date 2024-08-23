from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, pyttsx3
from googlesearch import search



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)


def google_search(command):
    print("gogle function called")
    reg_ex = re.search('search google for (.*)', command)
    search_for = command.split("for", 1)[1]
    op = list(search(search_for, advanced=True, sleep_interval=1, num_results=1))
    first_result = op[0]
    print("Description:", first_result.description)
    speak(first_result.description)

    # url = 'https://www.google.com/'
    # if reg_ex:
    #     subgoogle = reg_ex.group(1)
    #     url = url + 'r/' + subgoogle
    # speak("Okay mam!")
    # speak(f"Searching for {subgoogle}")
    # driver = webdriver.Chrome(
    #     executable_path='driver/chromedriver.exe')
    # driver.get('https://www.google.com')
    # search = driver.find_element_by_name('q')
    # search.send_keys(str(search_for))
    # search.send_keys(Keys.RETURN)