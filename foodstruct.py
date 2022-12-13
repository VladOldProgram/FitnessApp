import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def get_product_nutrients_data(product_name: str):
    if (not isinstance(product_name, str) or product_name == ''):
        return TypeError
    
    product_name = '-'.join(product_name.split())

    url = 'https://foodstruct.com/ru/food/' + product_name
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        return http_err

    soup = BeautifulSoup(response.text, 'lxml')
    product_nutrients_table = soup.find('table', id='all-nutrients')
    product_nutrients_data_list = []
    for tr in product_nutrients_table.find_all('tr')[2:6]:
        row_data = tr.find_all('td')[3]
        for e in row_data:
            e = e.replace('\t', '').replace('\n', '').replace('g', '').replace('kcal', '')
            product_nutrients_data_list.append(e)

    product_nutrients_data = dict()
    product_nutrients_data['calories'] = float(product_nutrients_data_list[3])
    product_nutrients_data['proteins'] = float(product_nutrients_data_list[0])
    product_nutrients_data['fats'] = float(product_nutrients_data_list[1])
    product_nutrients_data['carbohydrates'] = float(product_nutrients_data_list[2])

    return product_nutrients_data

def get_service_recommendations(product_name: str):
    if (not isinstance(product_name, str) or product_name == ''): 
        return TypeError

    product_name = '-'.join(product_name.split())

    url = 'https://foodstruct.com/search_multilang.php?lang=ru&q=' + product_name
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        return http_err

    soup = BeautifulSoup(response.text, 'lxml')
    service_recommendations = []
    i = 0
    for child in soup.body.children:
        service_recommendations.append(child.get_text())
        if (i == 9):
            break
        i += 1
    
    return service_recommendations
