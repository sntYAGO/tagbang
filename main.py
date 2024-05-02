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
    while True:
        try:
            questions = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
            for question in questions:
                answers = question.find_elements(By.CLASS_NAME, 'AB7Lab')
                if answers:  # check question
                    #time.sleep(2)  # 2 sec per choice
                    choice = random.randint(0, len(answers) - 1)
                    driver.execute_script("arguments[0].click();", answers[choice])

            next_button = driver.find_elements(By.XPATH, "//*[text()='Susunod']")
            if len(next_button) > 0:
                # chek next
                next_button[0].click()
                #time.sleep(2)   # wait 2
                  
            else:
                # if next = 1 submit
                submit = driver.find_element(By.XPATH, "//*[text()='Submit']")
                driver.execute_script("arguments[0].click();", submit)
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

while done < count:
    try:
        driver.get(url=url)
        time.sleep(1)
        auto_answer()
        done += 1
        print(f'{done}/{count}')

        # check pop up
        try:
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
            alert.send_keys(keys.RETURN)
            print("Unexpected alert found and accepted.")
        except NoAlertPresentException:
            print("No alert found, Moving on...")

    except UnexpectedAlertPresentException:
        print("Unexpected alert found, Moving on...")
#git config --global user.email "you@example.com"
#  git config --global user.name "Your Name"
