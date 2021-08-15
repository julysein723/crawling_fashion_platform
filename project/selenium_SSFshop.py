from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('https://www.ssfshop.com/selectAllBrandList')

drive.implicitly_wait(80)

drive.find_elements_by_css_selector('ul.brands > li > label')[5].click()

l = []
drive.implicitly_wait(200)

namess = drive.find_elements_by_css_selector('section.brand_list ul > li > a')

for name in namess:
    name_text = name.text
    name_split = name_text.split('\n')

    l.append(name_split)

df = pd.DataFrame(l, columns=['영문명', '국문명'])
df.to_csv('SSF_beaker.csv', index=False)


# #elem.clear()
# #elem.send_keys("pycon")
# #elem.send_keys(Keys.RETURN)
# #assert "No results found." not in driver.page_source
# #driver.close()