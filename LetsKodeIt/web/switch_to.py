from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


class SwitchTo:

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.implicitly_wait(10)

        main_page_handle = driver.current_window_handle
        print(main_page_handle)

        time.sleep(3)
        driver.find_element(By.ID,"openwindow").click()
        time.sleep(3)

        all_handles = driver.window_handles
        for a in all_handles:
            print(a)
            if a!= main_page_handle:
                driver.switch_to.window(a)
                driver.find_element(By.ID, "search-courses").send_keys("Python")
                time.sleep(3)
                driver.close()
                break

        driver.switch_to.window(main_page_handle)
        driver.find_element(By.ID,"name").send_keys("successful")
        time.sleep(3)


abc = SwitchTo()
abc.test()