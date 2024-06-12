from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set the link to your HTML file
Link = r"http://127.0.0.1:5500/voice.html"

# Setup Firefox options
firefox_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
firefox_options.set_preference("general.useragent.override", user_agent)
firefox_options.add_argument("--use-fake-ui-for-media-stream")
firefox_options.add_argument("--use-fake-device-for-media-stream")

# Initialize the WebDriver
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open the HTML file
driver.get(Link)

def SpeechRecognitionModel():
    driver.find_element(by=By.ID, value="start").click()
    print("Listening")
    while True:
        try:
            Text = driver.find_element(by=By.ID, value="output").text
            if Text:
                driver.find_element(by=By.ID, value="end").click()
                return Text
            else:
                sleep(0.333)
        except:
            pass

# Example usage of the SpeechRecognitionModel function
try:
    recognized_text = SpeechRecognitionModel()
    print(f"Recognized Text: {recognized_text}")
finally:
    driver.quit()
