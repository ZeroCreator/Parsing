# <input name="name" type="text" value="user name" />

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
# for selection input with name attribute "name"
name_input = driver.find_element_by_name("name")