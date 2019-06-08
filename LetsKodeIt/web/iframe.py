from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class IFrame:

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0, 1300);")
        time.sleep(4)
        driver.switch_to.frame("courses-iframe")
        driver.find_element(By.ID, "search-courses").send_keys("python")
        time.sleep(4)

        driver.execute_script("window.scrollBy(0, -1300);")
        time.sleep(4)

        driver.switch_to.default_content()
        driver.find_element(By.ID, "name").send_keys("Success")
        time.sleep(4)


cc = IFrame()
cc.test()

