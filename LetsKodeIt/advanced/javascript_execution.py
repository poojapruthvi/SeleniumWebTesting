from selenium import webdriver
import time
import os


class JavascriptExecution:

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        #driver.get("https://letskodeit.teachable.com/p/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';" )
        driver.maximize_window()
        driver.implicitly_wait(10)
        #ele = driver.find_element(By.ID, "name")
        ele = driver.execute_script("return document.getElementById('name');")
        ele.send_keys("Test")
        time.sleep(3)

    def size(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        #driver.get("https://letskodeit.teachable.com/p/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.maximize_window()
        driver.implicitly_wait(10)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print(height)
        print(width)


cc = JavascriptExecution()
cc.test()
cc.size()