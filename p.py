import requests
from bs4 import BeautifulSoup
import re

product_name = 'oppo enco x2'  # 替换为你要搜索的商品名

def get_jd_price(product):
    # 添加京东价格获取逻辑
    pass

def get_tb_price(product):
    # 添加淘宝价格获取逻辑
    url = f'https://s.taobao.com/search?q={product}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        prices = soup.find_all('div', class_='price')
        if prices:
            price_text = prices[0].text.strip()
            price_text = re.sub(r'[^\d.]', '', price_text)  # 清除非数字和小数点字符
            return float(price_text), "Taobao"
        else:
            return None, "Taobao"  # 返回 None 和平台
    else:
        raise Exception(f'Request to Taobao failed with status code {response.status_code}')

def get_pdd_price(product):
    # 添加拼多多价格获取逻辑
    pass

try:
    jd_price, jd_platform = get_jd_price(product_name)
    tb_price, tb_platform = get_tb_price(product_name)
    pdd_price, pdd_platform = get_pdd_price(product_name)

    prices = [(jd_price, jd_platform), (tb_price, tb_platform), (pdd_price, pdd_platform)]
    available_prices = [(price, platform) for price, platform in prices if price is not None]
    if available_prices:
        min_price, min_platform = min(available_prices)
        print(f'The lowest price for {product_name} is {min_price} on {min_platform}.')
    else:
        print(f'No price found for {product_name} on the specified platforms.')
except Exception as e:
    print(f'An error occurred: {e}')
