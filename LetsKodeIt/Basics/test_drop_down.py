from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Find():
    def test(self):

        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID,"carselect")
        sel = Select(element)

        sel.select_by_index("2")
        time.sleep(3)

        sel.select_by_value("benz")
        time.sleep(3)

        sel.select_by_visible_text("BMW")
        time.sleep(3)


cc = Find()
cc.test()