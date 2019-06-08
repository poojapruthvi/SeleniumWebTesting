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


        bmwrabtn = driver.find_element_by_id("bmwradio")
        bmwrabtn.click()

        time.sleep(5)

        benzrabtn = driver.find_element_by_id("benzradio")
        benzrabtn.click()

        time.sleep(5)

        bmwchbtn = driver.find_element_by_id("bmwcheck")
        bmwchbtn.click()

        time.sleep(5)

        benzchbtn = driver.find_element_by_id("benzcheck")
        benzchbtn.click()

        time.sleep(5)

        allbtns = driver.find_elements(By.XPATH,"//div[@id='radio-btn-example']/fieldset//label")
        size = len(allbtns)
        print(size)


        for a in allbtns:
                a.is_selected()
                a.click()
                time.sleep(3)


sm = Find()
sm.test()