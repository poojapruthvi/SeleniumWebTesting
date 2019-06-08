from selenium import webdriver
import os


class interactions():
    def test(self):
        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")

        driver.maximize_window()
        print("maximized the window")

        title = driver.title
        print("the title of the page is {}".format(title))

        cu_url = driver.current_url
        print("the url of the page is {}".format(cu_url))

        driver.refresh()
        print("refreshed current page")

        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        print("Iam on the next page")

        driver.back()
        print("Iam on the previous page")

        driver.forward()
        print("next page")

        driver.quit()


cd = interactions()
cd.test()