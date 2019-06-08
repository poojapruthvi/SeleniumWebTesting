from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class AlertConfirm:

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "name").send_keys("Pruthvi")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        a1 = driver.switch_to.alert
        a1.accept()
        time.sleep(2)

        driver.find_element(By.ID, "name").send_keys("Pooja")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        a2 = driver.switch_to.alert
        a2.dismiss()
        time.sleep(2)


cc = AlertConfirm()
cc.test()