from selenium import webdriver
import pandas as pd

drive = webdriver.Chrome(executable_path = 'drivers/chromedriver')
drive.get('https://www.beams.co.jp/global/label/')

drive.implicitly_wait(50)

l = []
drive.find_elements_by_css_selector('div.main-category-tab ul > li.main-category-tab-btn > a')[1].click()

alphabets = drive.find_elements_by_css_selector('div.sub-category-tab > ul > li > a')

for alphabet in alphabets:
    alphabet.click()
    names = drive.find_elements_by_css_selector('div > div > div > ul > li > a')
    for name in names:
        name_text = name.text
        if (name_text != ""):
            print(name_text)
            l.append(name_text)

df = pd.DataFrame(l, columns=['브랜드명'])
df.to_csv('beams.csv', index=False)


#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()