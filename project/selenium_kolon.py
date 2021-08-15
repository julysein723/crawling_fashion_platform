from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('https://www.kolonmall.com/')

drive.implicitly_wait(50)
result = drive.find_element_by_css_selector("a.sc-1gooan9-4 span").click()
print(result)
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
