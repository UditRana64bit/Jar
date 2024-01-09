import pyperclip # pip install pyperclip
import pyautogui # pip install pyautogui
import webbrowser # Inbuilt
from time import sleep # Inbuilt
import json # Inbuilt
import keyboard # pip install keyboard
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings
import win32gui
import win32con

def maximize_active_window():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)


warnings.simplefilter('ignore')
def CookieScrapper():
    print(".....")
    print(".....")
    webbrowser.open("https://bard.google.com/chat")
    sleep(2)
    maximize_active_window()
    pyautogui.click(x=1464, y=58)
    sleep(1)
    pyautogui.click(x=1431, y=56)
    sleep(7)
    pyautogui.click(x=1230, y=219)
    sleep(9)
    pyautogui.click(x=1200, y=94)
    sleep(1)
    keyboard.press_and_release('Ctrl + W')
    sleep(1)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        print("*The process of loading cookies has been executed without any issues, and the cookies are now successfully integrated into the system.*")
        pass

    except json.JSONDecodeError as e:
        print("*Cookies Loaded Unsuccessfully*")
        print("""*The error has been identified as a result of unsuccessful cookie replication from the Chrome extension, 
which is causing a disruption in the intended functionality.*""")
     
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    try:
        SIDValue = next((item for item in json_data if item["name"] == SID), None)
        TSValue = next((item for item in json_data if item["name"] == TS), None)
        CCValue = next((item for item in json_data if item["name"] == CC), None)

        if SIDValue is not None:
            SIDValue = SIDValue["value"]
        else:
            print(f"{SIDValue} not found in the JSON data.")

        if TSValue is not None:
            TSValue = TSValue["value"]
        else:
            print(f"{TSValue} not found in the JSON data.")
 
        if CCValue is not None:
            CCValue = CCValue["value"]
        else:
            print(f"{CCValue} not found in the JSON data.")

        cookie_dict = {
            "__Secure-1PSID": SIDValue ,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }

        return cookie_dict

    except Exception as e:
        print(e)





cookies=CookieScrapper()


def save_cookies():
    cookie_dict=cookies
    return cookie_dict

