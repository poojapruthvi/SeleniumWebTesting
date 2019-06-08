import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Scroll:

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print(height)
        print(width)

        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(4)

        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(4)

        element = driver.find_element(By.ID,'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(4)
        driver.execute_script("window.scrollBy(0, -150);")


cc = Scroll()
cc.test()