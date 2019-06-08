from selenium import webdriver
import os

class Find():
    def test(self):

        driverLocation = "/usr/lib/chromium-browser/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://letskodeit.teachable.com/p/practice")


        elementbyid = driver.find_element_by_id("name")
        if elementbyid is not None:
            print("found by id")

        elementbyname = driver.find_element_by_name("show-hide")
        if elementbyname is not None:
            print("found by name")

        elementbyclass = driver.find_element_by_class_name("displayed-class")
        if elementbyclass is not None:
            print("found by class")


        elementbytag = driver.find_element_by_tag_name("h1")
       #text = elementbytag.text
        if elementbytag is not None:
            print("found by tag and the tag name is {}".format(elementbytag.text))


sm = Find()
sm.test()