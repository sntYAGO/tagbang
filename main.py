import os
import pathlib
import random
import time
import settings
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


base_dir = pathlib.Path(__file__).resolve().parent

service = Service(executable_path=os.path.join(base_dir, 'chromedriver.exe'))

driver = webdriver.Chrome(
    service=service,
    options=webdriver.ChromeOptions()
)
driver.maximize_window()

url = settings.google_form_url
count = settings.answers_count
done = 0

def auto_answer():
    questions = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
    for question in questions:
        answers = question.find_elements(By.CLASS_NAME, 'AB7Lab')
        if answers:  # Check if the list is not empty
            choice = random.randint(0, len(answers) - 1)
            driver.execute_script("arguments[0].click();", answers[choice])

while done < count:
    try:
        driver.get(url=url)
        time.sleep(1)
        auto_answer()
        next_button = driver.find_elements(By.XPATH, "//*[text()='Susunod']")
        if len(next_button) > 0:
            # If 'Next' button is present, click it
            next_button[0].click()
            auto_answer()
        else:
            # If 'Next' button is not present, click 'Submit'
            submit = driver.find_element(By.XPATH, "//*[text()='Submit']")
            submit.click()


        done += 1
        print(f'{done}/{count}')

    except UnexpectedAlertPresentException:
        try:
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
            alert.send_keys(keys.RETURN)
            print("Unexpected alert found and accepted.")
        except NoAlertPresentException:
            print("No alert found, Moving on...")
        
