from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import requests
import os
import time


driver = Chrome(executable_path='./chromedriver')                   
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {   
    "source": """
       Object.defineProperty(navigator, 'webdriver', {
         get: () => undefined
       })
     """
})
# 有些網站有擋BadBot惡意機器人檢測目前瀏覽器的window.navigator(表示瀏覽器的信息)是否包含webdriver對象，在正常使用瀏覽器的情况下，屬性為未賦值undefined，
# 但使用了selenium後，屬性就被初始化為 true，很多網站就通過 Javascript 判斷這個屬性實現反 selenium爬蟲。
# 解決方式為在程式碼內告訴網站webdriver對象屬性為undefined，就能夠成功爬取。

url = ""  # 要爬的網站網址 
url_start = ""  # 換頁


def pic_catch(soup):                            
    for a in soup.select("a.js-photo-link"):
        imageSrc = a.img["src"]
        image = requests.get(imageSrc)
        imageContent = image.content
        i = str(a["href"]).split("/")[3]         
        path = f"{dir}/{i}.jpg"
        file = open(path, "wb")                  
        file.write(imageContent)
        file.close()
        time.sleep(0.5)
        # print(i)


dir = "Mask_data"
if not os.path.isdir(dir):
    os.makedirs(dir)


for p in range(2, 5):                 
    driver.get(url)                   

    driver.maximize_window()

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    pos = 0 # Selenium下拉滾輪
    for x in range(4):                 
        pos += x * 500  # 每次下滾500
        js = "document.documentElement.scrollTop=%d" % pos
        driver.execute_script(js)
        time.sleep(1)

    pic_catch(soup)
    time.sleep(5)
    url = url_start + f"{p}"


driver.close()
