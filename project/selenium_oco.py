from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('https://www.ocokorea.com/shop/goods/brand.do')

drive.implicitly_wait(50)

l = []

names = drive.find_elements_by_css_selector('div.brandlist div > div > a > div.text')

for name in names:
    name_text = name.text
    name_split = name_text.split('\n')
    print(name_split)
    l.append(name_split)

df = pd.DataFrame(l, columns=['국문명', '영문명'])
df.to_csv('OCO.csv', index=False)


#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()