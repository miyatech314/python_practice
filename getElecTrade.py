# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# Chromeのpath
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# headlessモード
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。
driver = webdriver.Chrome(chrome_options=options)

# URLからページ取得
url = "http://www.jepx.org/market/index.html"
driver.get(url)

# レンダリングのための時間
time.sleep(2)

# レンダリング結果をchromedriverから取得
html = driver.page_source

# BeautifulSoupでレンダリング済みのhtmlを扱う
soup = BeautifulSoup(html, "html.parser")

# 見たいやつ見つけて出力
print ("DA-24 : " + soup.find(id="chartDAAll").string)
print ("DA-DT : " + soup.find(id="chartDADay").string)
print ("DA-PT : " + soup.find(id="chartDAPeak").string)
print ("TTV   : " + soup.find(id="chartsumVolume").string)

# 終了
driver.quit()
