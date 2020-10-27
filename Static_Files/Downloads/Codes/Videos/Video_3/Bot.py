from selenium import webdriver
from time import sleep

driver = 'Chrome_WebDrvier'


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


    def FindMyFollowers(self, number_of_followers_to_find, your_url_username):
        sleep(5)
        self.driver.get('https://instagram.com/' + your_url_username)
        sleep(2)
        self.driver.find_element_by_xpath('//a[@href="/' + your_url_username + '/followers/"]').click()
        sleep(1)
        popup = self.driver.find_element_by_class_name('isgrP')
        Followers_Array = []


        i = 1
        while len(Followers_Array) <= number_of_followers_to_find:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            sleep(0.4)
            Followers = self.driver.find_elements_by_class_name('FPmhX')

            for Follower in Followers:
                if Follower not in Followers_Array:
                    Followers_Array.append(Follower.text)

            i += 1

        print(Followers_Array)

        self.followers = Followers_Array

    def FollowTheirFollowers(self, number_of_followers_to_follow):
        for Follower in self.followers:
            self.driver.get('https://instagram.com/' + Follower)
            sleep(2)
            if(len(self.driver.find_elements_by_xpath("//*[contains(text(), 'This Account is Private')]")) > 0):
                # If they're private, we can't see their follower list, so skip them
                continue

            self.driver.find_element_by_xpath(
                '//a[@href="/' + Follower + '/followers/"]').click()
            sleep(3)

            follow = self.driver.find_elements_by_xpath(
                "//button[contains(text(), 'Follow')]")

            i = 1

            for follower in follow:
                if(i != 1):
                    self.driver.execute_script("arguments[0].click();", follower)

                elif(i > number_of_followers_to_follow):
                    break

                i += 1

            sleep(2)


Bot = InstaBot('Your_Username', 'Your_Password')
Bot.FindMyFollowers(10, 'Your_Url_Username')
Bot.FollowTheirFollowers(10)

