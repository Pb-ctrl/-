import requests
from bs4 import BeautifulSoup
import tkinter as tk
import pyperclip

# 创建GUI窗口
window = tk.Tk()
window.title("商品价格比较")
window.geometry("600x400")

# 创建输入窗口
input_label = tk.Label(window, text="请输入商品:")
input_label.pack(pady=20)
input_entry = tk.Entry(window, width=30)
input_entry.pack(pady=10)

# 获取输入的商品名称
def get_product():
    product = input_entry.get()
    return product

# 获取价格信息的函数
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

# ... (其他函数保持不变)
def get_amazon_price(product):
        url = f"https://www.amazon.com/s?k={product}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all(class_='s-result-item')
        if items:
            item = items[0]
            link = "https://www.amazon.com" + item.find(class_='a-link-normal').get('href')
            price = item.find(class_='a-offscreen').get_text()
            return price, link
        else:
            return None, None

# 更新比较价格函数
def compare_prices(prices, platforms):
    min_price = min(prices)
    min_price_index = prices.index(min_price)
    return f"{platforms[min_price_index]}最低价格: {min_price}"


def get_alibaba_price(product):
    url = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={product}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(class_='organic-list-offer-outter J-offer-wrapper')
    if items:
        item = items[0]
        link = "https:" + item.find(class_='title').find('a').get('href')
        price = item.find(class_='price').get_text()
        return price, link
    else:
        return None, None


def get_dangdang_price(product):
    url = f"https://search.dangdang.com/?key={product}&act=input"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all(class_='bigimg')
    if items:
        item = items[0]
        link = item.find(class_='pic').find('a').get('href')
        price = item.find(class_='search_now_price').get_text()
        return price, link
    else:
        return None, None

# 创建结果标签
result_entry = tk.Entry(window, width=60)
result_entry.pack(pady=20)

# 创建并显示结果标签
def show_result():
    product = get_product()
    jd_price, jd_link = get_jd_price(product)
    taobao_price, taobao_link = get_taobao_price(product)
    pinduoduo_price, pinduoduo_link = get_pinduoduo_price(product)
    amazon_price, amazon_link = get_amazon_price(product)
    alibaba_price, alibaba_link = get_alibaba_price(product)
    dangdang_price, dangdang_link = get_dangdang_price(product)

    prices = [price for price in [jd_price, taobao_price, pinduoduo_price, amazon_price, alibaba_price, dangdang_price]
              if price is not None]
    platforms = ['京东', '淘宝', '拼多多', '亚马逊', '阿里巴巴', '当当']

    if prices:
        result_text = compare_prices(prices, platforms)
        result_entry.delete(0, tk.END)  # Clear the text in the Entry
        result_entry.insert(tk.END, result_text)
    else:
        result_entry.delete(0, tk.END)
        result_entry.insert(tk.END, "未找到商品信息")

# 创建显示结果按钮
result_button = tk.Button(window, text="显示结果", command=show_result)
result_button.pack(pady=10)

# 创建复制结果按钮
def copy_result():
    result_text = result_entry.get()
    pyperclip.copy(result_text)

# 创建复制结果按钮
copy_button = tk.Button(window, text="复制结果", command=copy_result)
copy_button.pack(pady=10)

# 开始窗口事件循环
window.mainloop()
