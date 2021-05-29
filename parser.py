# import necessary libraries
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os



PAGES = 50
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279'
}
URL = 'https://www.lamoda.ru/c/519/clothes-muzhskie-shorty/?page='
FOLDER = 'data_shorts'
FILE = 'shorts'
SAVE_FOLDER = 'shorts'


# getting the page which you heed
def get_html_pages(pages, headers, save_folder, url):
    os.mkdir(save_folder)
    for i in range(1, pages+1):
        url = f'{url}{i}'

        req = requests.get(url, headers=headers)
        src = req.text

        # Page will save in your directory near the parser file

        with open(f'{save_folder}/index{i}.html', 'w') as file:
            file.write(src)


def parse(folder_path, pages):
    # read the file
    product_data = []

    for i in range(1, pages+1):
        with open(f'{folder_path}/index{i}.html') as f:
            src = f.read()

        # create soup class object
        soup = BeautifulSoup(src, 'lxml')

        # get all products links
        all_products_hrefs = soup.find_all(class_='products-list-item__link link')

        # get information from each product and fill the dictionary
        for item in all_products_hrefs:
            desc = item.find(class_='to-favorites js-to-favorites to-favorites_wish-groups')
            name_product = item.find(class_='products-list-item__type')

            item_name = name_product.text.strip()
            item_brand = desc.get('data-brand')
            item_category = desc.get('data-category')
            item_color = desc.get('data-color-family')
            item_gender = desc.get('data-gender')
            item_is_new = desc.get('data-is-new')
            item_is_sport = desc.get('data-is-sport')
            item_is_premium = desc.get('data-is-premium')
            item_price = desc.get('data-price-origin')

            item_link = 'https://www.lamoda.ru' + item.get('href')

            item_data =  [item_brand,item_category,item_name,item_color,item_gender,item_is_new,item_is_sport,item_is_premium,item_price,item_link]
            product_data.append(item_data)

    return product_data


def to_csv(product_data, save_folder, save_file_name):
    df = pd.DataFrame(product_data, columns=['item_brand','item_category', 'item_name','item_color', 'item_gender','item_is_new',
                                                        'item_is_sport','item_is_premium','item_price','link'])
    os.mkdir(save_folder)

    df.to_csv(f'{save_folder}/{save_file_name}.csv')


def run(url, pages, headers, folder, save_file_name, save_folder):
    get_html_pages(pages, headers, folder, url)
    product_data = parse(folder, pages)
    to_csv(product_data, save_folder, save_file_name)
    print('@-@-@ Success')


run(URL, PAGES, HEADERS, FOLDER, FILE, SAVE_FOLDER)








