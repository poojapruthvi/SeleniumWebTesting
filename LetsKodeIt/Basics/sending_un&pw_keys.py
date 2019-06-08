from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By


class Find():
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
        email_id.send_keys("test@gmail.com")

        email_id.clear()

        email_id.send_keys("test@email.com")

        password = driver.find_element(By.ID, 'user_password')
        password.send_keys("abcabc")
        time.sleep(3)
        final_login_button = driver.find_element(By.NAME, 'commit')
        final_login_button.click()
        time.sleep(3)


sm = Find()
sm.test()