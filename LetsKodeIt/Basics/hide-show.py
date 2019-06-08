from selenium import webdriver
import os
import time


class Find:

    def test(self):

        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)


        ele = driver.find_element_by_id("displayed-text")
        state = ele.is_displayed()
        print(state)
        time.sleep(3)

        hidebtn = driver.find_element_by_id("hide-textbox")
        hidebtn.click()
        state = ele.is_displayed()
        print(state)
        time.sleep(3)

        showbtn = driver.find_element_by_id("show-textbox")
        showbtn.click()
        state = ele.is_displayed()
        print(state)
        time.sleep(3)



cc = Find()
cc.test()

