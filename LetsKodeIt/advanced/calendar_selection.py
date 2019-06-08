from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By


class Calendar:

    def test(self):

        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://www.expedia.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        flight_btn = driver.find_element(By.ID,"tab-flight-tab-hp")
        flight_btn.click()
        time.sleep(4)

        departing_btn = driver.find_element(By.ID, "flight-departing-hp-flight")
        departing_btn.click()
        time.sleep(4)

        xpath = "//div[@class='datepicker-cal-month']/table/tbody[1]/tr[3]/td[1]/button[1]"
        date = driver.find_element(By.XPATH,xpath)
        date.click()
        time.sleep(4)


aa = Calendar()
aa.test()