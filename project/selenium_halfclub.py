from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('http://www.halfclub.com/brandSearch?tabNo=2')
drive.implicitly_wait(50)
names = drive.find_elements_by_css_selector('a > span.name')

l = []
for name in names:
    if (name.text != '') :
        l.append([name.text])

print(l)
df = pd.DataFrame(l, columns=['브랜드명'])
df.to_csv('halfclub2.csv', index=False)

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
