import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.wconcept.co.kr/Brand?mcd=M83985861"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

names = soup.select('.brand_result ul > li > a')
l = []
for name in names :
    split_name = name.text.replace(" ", "")
    split_name = split_name.replace("\r", "")
    list_name = split_name.split('\n')
    l.append([list_name[2], list_name[4]])
    # list_name
df = pd.DataFrame(l, columns=['영문명', '국문명'])
df.to_csv('Wconcept_m.csv', index=False)
# title = soup.find_all('a')

