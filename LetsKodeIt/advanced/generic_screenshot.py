from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class GenericScreenshots:

    def test(self):

        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        login_button = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        time.sleep(5)
        login_button.click()
        time.sleep(5)

        email_id = driver.find_element(By.ID,'user_email')
        email_id.send_keys("abc@email.com")
        time.sleep(5)

        password = driver.find_element(By.ID, 'user_password')
        password.send_keys("abc")
        time.sleep(3)
        final_login_button = driver.find_element(By.NAME, 'commit')
        final_login_button.click()
        time.sleep(3)

        filename = str(round(time.time() * 1000)) + ".png"
        path = "/home/pk/pichu/selenium_practise/"
        ss = path + filename
        driver.save_screenshot(ss)
        print("saved")

abcd = GenericScreenshots()
abcd.test()
