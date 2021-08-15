from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('https://www.eqlstore.com/brands/home?ga_param=MENUbrand')

drive.implicitly_wait(50)

l = []

names = drive.find_elements_by_css_selector('ul.brand-list li > div > a')

for name in names:
    name_text = name.text
    name_split = name_text.split('\n')
    l.append(name_split)

df = pd.DataFrame(l, columns=['영문명', '국문명'])
df.to_csv('EQL.csv', index=False)


#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()