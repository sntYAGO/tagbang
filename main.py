import os
import pathlib
import random
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


base_dir = pathlib.Path(__file__).resolve().parent

service = Service(executable_path=os.path.join(base_dir, 'chromedriver.exe'))

driver = webdriver.Chrome(
    service=service,
    options=webdriver.ChromeOptions()
)
driver.maximize_window()


def auto_answer(url, count): #main function
    done = 0
    while done < count:
        try:
            driver.get(url=url)
            time.sleep(1)
            while True:
                try:
                    questions = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
                    for question in questions:
                        answers = question.find_elements(By.CLASS_NAME, 'AB7Lab')
                        if answers:  # check question
                            choice = random.randint(0, len(answers) - 1)
                            driver.execute_script("arguments[0].click();", answers[choice])

                    next_button = driver.find_elements(By.XPATH, "//*[text()='Susunod']")
                    if len(next_button) > 0: # check next button
                        next_button[0].click()
                    else:
                        submit = driver.find_element(By.XPATH, "//*[text()='Submit']") # submit if next button is not present
                        driver.execute_script("arguments[0].click();", submit)
                        break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

            done += 1
            print(f'{done}/{count}')

            try:        #catch pop up
                time.sleep(2)
                alert = driver.switch_to.alert
                alert.accept()
                alert.send_keys(Keys.RETURN)
                print("Unexpected alert found and accepted.")
            except NoAlertPresentException:
                print("No alert found, Moving on...")

        except UnexpectedAlertPresentException:
            print("Unexpected alert found, Moving on...")
