from selenium import webdriver
from selenium.webdriver import ActionChains
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
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)
        mouse_hover_btn = driver.find_element(By.ID,"mousehover")

        try:
            ActionChains(driver).move_to_element(mouse_hover_btn).perform()
            time.sleep(2)
            reload_btn = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Reload']")
            ActionChains(driver).move_to_element(reload_btn).click().perform()
            time.sleep(3)
        except:
            print("Invalid")


cc = AlertConfirm()
cc.test()