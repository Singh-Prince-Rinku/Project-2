from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Link = r"C:\Users\princ\OneDrive\Desktop\Project 2\voice.html"
chrome_Options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
chrome_Options.add_argument(f"user-agent = {user_agent}")
chrome_Options.add_argument("--use-fake-ui-for-media-stream")
chrome_Options.add_argument("--use-fake-device-for-media-stream")
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service = service, options=chrome_Options)
driver.get(Link)

def SpeechRecognitionModel():
    driver.find_element(by=By.ID, value="start").click()
    print("Listening")
    while True:
        try:
            Text = driver.find_element(by=By.ID, value = "output").text
            if Text:
                driver.find_element(by=By.ID, value = "end").click()
                return Text
            else:
                sleep(0.333) 
        except:
            pass    

while True:
    pass
    # print("Speech Recognition")
#
