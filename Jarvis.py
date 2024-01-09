from time import sleep # Inbuilt
from playsound import playsound
import multiprocessing
print ("Wait")
def pl():
    playsound ("C://Users//soni//Desktop//Jarvis//pl.mp3")

sleep(20)

from bardapi import BardCookies # pip install bardapi
import datetime # pip install datetime
import pyttsx3
import speech_recognition as sr
from win10toast import ToastNotifier
import time
from cookie import save_cookies
import re
import warnings
import threading





warnings.simplefilter('ignore')


from datetime import datetime
def greeting():
    # Get the current hour
    current_hour = datetime.now().hour

    # Define greeting messages for different time ranges
    greetings = {
        0: "Good Morning Sir!",
        12: "Good Afternoon Sir!",
        18: "Good Evening Sir!",
        24: "Good Evening Sir!",
    }

    # Choose the greeting based on the hour
    for threshold, greeting in greetings.items():
        if current_hour < threshold:
            print(greeting)
            return greeting

    # Handle edge cases for 24-hour format
    if current_hour == 24:
        return greetings[0]

    # If no greeting matches, return a default
    return "Hello Sir!"


def times():
    # Get the current time as a tuple of seconds since midnight
    current_time = time.time()

    # Convert seconds to hours, minutes, and seconds
    hours, minutes, seconds = time.gmtime(current_time).tm_hour, time.gmtime(current_time).tm_min, time.gmtime(current_time).tm_sec

    # Determine AM or PM
    am_pm = "AM" if hours < 12 else "PM"

    # Adjust hour for 12-hour format
    if hours > 12:
        hours -= 12

    # Format the time string
    time_string = f"{hours}:{minutes:02}:{seconds:02} {am_pm}"

    # Print the time
    return time_string

message = f"It`s currently {times()} at your current location. Tell me how I can be of your service sir."


def noti():
    # Create a notifier object
    toast = ToastNotifier()

    # Get and ensure valid greeting
    title = greeting()
    if title is None:
        title = "Good Day Sir!"

    # Define the notification content
    message1 = f"I am Jarvis, it is currently {times()} at your current location. Tell me how I can be of your service sir."

    # Customize the notification (optional)
    duration = 10  # Display for 10 seconds
    threaded = True  # Run in a separate thread

    # Show the toast notification
    toast.show_toast(title, message1, duration=duration, threaded=threaded)

    # Run your program logic here...








from time import sleep # Inbuilt
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options # pip install selenium
from selenium.webdriver.common.by import By # pip install selenium
import warnings # Inbuilt
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



Link = "https://readloud.net/english/british/1-male-voice-brian.html"
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--headless-new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(Link)



def WaitForWeb():
    sleep(2)
    while True:
        try:                        
            driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea')
            break
            
        except:
            pass


def speak(Text):
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea').send_keys(Text)
    
    except:
        pass

    sleep(0.8)
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/span/input').click()
    
    except:
        pass
    
    sleep(0.8)

    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea').clear()
    
    except:
        pass








def command():
    try:
        r=sr.Recognizer()
        print("Listening for command...")
        with sr.Microphone() as source:
            audio = r.listen(source,0,8)  # Listen for 5 seconds
        command = r.recognize_google(audio)
        return (command)
        # Process the command here
    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
        print("Please enter your command as text: ")
        command = input()
        print(f'User: {command}')
        return command
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))



cookie_dict=save_cookies()
   

pl()
noti()
speak(message)



bard=BardCookies(cookie_dict=cookie_dict)



while True:
    while True:
        try:
            Question = command()
            results = bard.get_answer(Question)['content']
            speak(results)
            print(results)
           
        except Exception as e:
            print(e)
