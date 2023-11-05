import requests
from bs4 import BeautifulSoup
  # 你要搜索的商品

product = input("请输入商品:")



def get_jd_price(product):

    url = f"https://search.jd.com/Search?keyword={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(class_='gl-item')
    if items:
        item = items[0]
        link = "https:" + item.find(class_='p-img').a['href']
        price = item.find(class_='p-price').strong.i.get_text()
        return price, link
    else:
        return None, None

def get_taobao_price(product):
    url = f"https://s.taobao.com/search?q={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(class_='item J_MouserOnverReq')
    if items:
        item = items[0]
        link = "https:" + item.find(class_='pic-link').get('href')
        price = item.find(class_='price').get_text()
        return price, link
    else:
        return None, None

def get_pinduoduo_price(product):
    url = f"http://search.pinduoduo.com/search?keyword={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(class_='item')
    if items:
        item = items[0]
        link = "http://yangkeduo.com" + item.find(class_='goods-name').a['href']
        price = item.find(class_='price').get_text()
        return price, link
    else:
        return None, None


jd_price, jd_link = get_jd_price(product)
taobao_price, taobao_link = get_taobao_price(product)
pinduoduo_price, pinduoduo_link = get_pinduoduo_price(product)

prices = [price for price in [jd_price, taobao_price, pinduoduo_price] if price is not None]
min_price = min(prices)
min_price_index = prices.index(min_price)

if min_price_index == 0:
    print(f"京东最低价格: {jd_price}, 链接: {jd_link}")
elif min_price_index == 1:
    print(f"淘宝最低价格: {taobao_price}, 链接: {taobao_link}")
else:
    print(f"拼多多最低价格: {pinduoduo_price}, 链接: {pinduoduo_link}")
