#  Universal parser for websites
Universal parser. You should change a few arguments for your own parser!

That's so easy to do!

1-Open the file in the your environment                                                                                                                                               
2-You must change first params                                                                                                                                                      

    PAGES = count of pages you want to parse

    HEADERS = {

        'Accept': '*/*',

        'User-Agent': 'your agent data'

    }

    URL = 'https://www.lamoda.ru/c/519/clothes-muzhskie-shorty/?page=' url like this, 'page=' should be in your url

    FOLDER = 'your folder which u need'

    FILE = 'your file which u need'

    SAVE_FOLDER = 'your folder which u need'

    3-Run the script, u will get the message '@-@-@ Success' and csv files will be in your folders.

That parser determines on lamoda.com, u should change parse data for your necessary website

    all_products_hrefs = soup.find_all(class_='products-list-item__link link')

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
