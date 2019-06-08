from selenium import webdriver
import os

from selenium.webdriver.common.by import By


class interactions():

    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://www.apricity.co.in/")

        driver.maximize_window()
        print("maximized the window")

        title = driver.title
        print("the title of the page is {}".format(title))

        cu_url = driver.current_url
        print("the url of the page is {}".format(cu_url))

        element = driver.find_element(By.TAG_NAME, 'h1')
        element.text
        print(element.text)

        driver.refresh()
        print("refreshed current page")

        driver.get("https://github.com/PruthviKumarBK/PROTON")
        print("Iam on the next page")


cd = interactions()
cd.test()