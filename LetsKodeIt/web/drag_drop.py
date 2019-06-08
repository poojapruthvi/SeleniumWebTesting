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
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.switch_to.frame(0)
        time.sleep(2)
        drag_ele = driver.find_element(By.ID, "draggable")
        drop_ele = driver.find_element(By.ID, "droppable")
        #ActionChains(driver).drag_and_drop(drag_ele, drop_ele).perform()
        #ActionChains(driver).click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        #Above are the 2 ways of doing the same
        time.sleep(2)


cc = DragDrop()
cc.test()