from selenium import webdriver
from time import sleep

driver = 'Chrome_WebDriver_Path'

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(driver)

        self.username = username
        self.password = password

        self.driver.get("https://www.instagram.com/")

        sleep(5)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

        sleep(5)


InstaBot('Your Username', 'Your Password')
