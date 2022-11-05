'''
import requests
from bs4 import BeautifulSoup
import pandas as pd



url = 'https://foodstruct.com/ru/food/огурец'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

product_nutrients_table = soup.find('table', id='all-nutrients')

data_frame = pd.DataFrame(columns=[1])

for tr in product_nutrients_table.find_all('tr')[2:6]:
    row_data = tr.find_all('td')[3]
    row = [i.text.replace('\t', '').replace('\n', '') for i in row_data]
    length = len(data_frame)
    data_frame.loc[length] = row

pass
'''
