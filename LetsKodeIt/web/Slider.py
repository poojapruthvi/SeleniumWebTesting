from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os
import time


class DragDrop:

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://jqueryui.com/slider/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)
        slider = driver.find_element(By.XPATH, "//div[@id='slider']/span")
        time.sleep(3)
        ActionChains(driver).drag_and_drop_by_offset(slider, 200, 0).perform()
        time.sleep(3)

cc = DragDrop()
cc.test()