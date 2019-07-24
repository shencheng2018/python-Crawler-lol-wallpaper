from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib import request

# 获得html
def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)

    for i in range(3):
        html1 = driver.page_source
        driver.execute_script('window.scrollTo(0,1000000)')
        time.sleep(10)
        html = driver.page_source
        if html == html1:
            break
        else:
            continue

    return html

# 分析html里面的数据
def analyze_data(html):
    soup = BeautifulSoup(html, "html.parser")
    wallpaper = soup.select("div.fusion-image-wrapper a img")

    data = []
    for i in range(len(wallpaper)):
        data.append(wallpaper[i].get("srcset"))

    wallpaper_url = []
    for i in data:
        b = i.split("http")
        c = "http" + b[-1]
        d = c[:c.find(" ")]
        wallpaper_url.append(d)

    return wallpaper_url
# 保存数据
def sava_data(wallpaper_url,flie, header):
    for i in range(len(wallpaper_url)):
        print(wallpaper_url[i])
        opener = request.build_opener()
        opener.addheaders = [header]
        request.install_opener(opener)
        request.urlretrieve(wallpaper_url[i], flie + "/" + str(i) + ".jpg")

def main():
    header = ("User-Agent", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')
    flie = "C:/Users/Shinelon/Desktop/aaa"
    url = "http://www.lol-wallpapers.com/official-artwork/"
    html = get_html(url)
    wallpaper_url = analyze_data(html)
    sava_data(wallpaper_url, flie, header)

if __name__ == '__main__':
    main()