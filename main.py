# !pip install selenium
# !pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")


driver = webdriver.Chrome(options=chrome_options)

website = f"{getcwd()}\\index.html"

driver.get(website)

rec_file = f"{getcwd()}\\input.txt"

def listen():
    try:
        startButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        startButton.click()
        print("Listening...")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "output")))
            current_text = output_element.text.strip()
            if "Start" in startButton.text and is_second_click:
                if output_text:
                    is_second_click = False
            elif "Stop" in startButton.text:
                is_second_click = True
            
            if current_text != output_text:
                output_text = current_text
                with open(rec_file, "w") as file:
                    file.write(output_text.lower())
                    print("USER: "+ output_text)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

listen()