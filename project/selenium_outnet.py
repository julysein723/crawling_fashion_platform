from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('https://www.verishop.com/brands')

drive.implicitly_wait(50)

l = []

names = drive.find_elements_by_css_selector('div > div > div > div > a')

for name in names:
    name_text = name.text
    l.append(name_text)

df = pd.DataFrame(l, columns=['브랜드명'])
df.to_csv('verishop.csv', index=False)


#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()