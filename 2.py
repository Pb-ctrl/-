import requests
from bs4 import BeautifulSoup

def get_jd_price(product):
    url = f"https://search.jd.com/Search?keyword={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('div', class_='p-price').find('strong').i.get_text()
    return f"京东: {price}"

def get_taobao_price(product):
    url = f"https://s.taobao.com/search?q={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('div', class_='price').get_text()
    return f"淘宝: {price}"

def get_pinduoduo_price(product):
    url = f"http://search.pinduoduo.com/crawler_result?query={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('span', class_='price').get_text()
    return f"拼多多: {price}"

product = "gpw" # 你可以将其替换为你感兴趣的任何商品

print(get_jd_price(product))
print(get_taobao_price(product))
print(get_pinduoduo_price(product))
