from selenium import webdriver

from selenium.webdriver.common.keys import Keys


Path = '/PATH/chromedriver'


driver = webdriver.Chrome( Path)


driver.get( "https://google.com")


SearchBox = driver.find_element_by_name( "q" )


SearchBox.send_keys( "What is Youtube?" )

SearchBox.send_keys(Keys.RETURN )