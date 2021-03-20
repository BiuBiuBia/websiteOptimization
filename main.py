# 线程: 线程可以理解成执行代码的分支， 线程是执行对应的代码的， cpu调度线程去执行对应代码
import sys
import time
import threading
import random
from selenium.webdriver.firefox.options import Options
import requests
from selenium import webdriver
import math
import datetime
import numpy as np

def rule(self):
    # 获取当前时间
    now = datetime.datetime.now()
    #0-星期一，1-星期二，以此类推
    weekday=now.weekday()
    hour=now.hour
    # randNumList表示不同星期日子下的不同时间段的返回值的范围
    #第一行表示星期一的，往后以此类推
    randNumList=[
        [[0,5],[10,20],[20,30],[10,20]],
        [[0, 5], [10, 20], [20, 30], [10, 20]],
        [[0, 5], [10, 20], [20, 30], [10, 20]],
        [[0, 5], [10, 20], [20, 30], [10, 20]],
        [[0, 5], [10, 20], [20, 30], [10, 20]],
        [[0, 5], [10, 20], [20, 30], [10, 20]],
        [[0, 0], [15, 20], [15, 20], [0, 1]],
    ]
    shape=np.array(randNumList).shape
    # 根据当前星期日子weekday、时间段hour，获取对应的返回值
    for i in range(shape[0]):
        if weekday==i:
            if (hour >= 0 and hour < 8):
                randNum = random.randint(randNumList[i][0][0], randNumList[i][0][1])
            elif hour >= 8 and hour < 13:
                randNum = random.randint(randNumList[i][1][0], randNumList[i][1][1])
            elif hour >= 13 and hour < 20:
                randNum = random.randint(randNumList[i][2][0], randNumList[i][2][1])
            else:
                randNum = random.randint(randNumList[i][3][0], randNumList[i][3][1])
    chrome_num1=math.ceil(random.randint(math.ceil(randNum/3*2),randNum)*0.8)
    firefox_num1=math.ceil((randNum-chrome_num1)*0.8)
    chrome_num2=math.ceil(chrome_num1/4)
    firefox_num2=math.ceil(firefox_num1/4)
    return chrome_num1, firefox_num1,chrome_num2,firefox_num2


def direct_firefox(proxy):
    profile = webdriver.FirefoxProfile()
    ip, port = proxy.split(":")
    port = int(port)
    settings = {
        'network.proxy.type': 1,  # 0: 不使用代理；1: 手动配置代理
        'network.proxy.http': ip,
        'network.proxy.http_port': port,
        'network.proxy.ssl': ip,  # https的网站,
        'network.proxy.ssl_port': port,
    }
    # 更新配置文件
    for key, value in settings.items():
        profile.set_preference(key, value)
    profile.update_preferences()

    options = Options()
    firefox = webdriver.Firefox(executable_path='C:/Program Files (x86)/Mozilla Maintenance Service/geckodriver.exe',
                                firefox_profile=profile, options=options)
    firefox.get('http://med.ckcest.cn/index.html')
    event = threading.Event()
    event.wait(random.uniform(100, 120))
    firefox.find_element_by_id('searchText').send_keys("医药")
    firefox.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[2]/a').click()
    event.wait(10)
    firefox.quit()


def direct_chrome(ip):
    url = "http://med.ckcest.cn/index.html"
    proxy = ip
    chromeOptions = webdriver.ChromeOptions()  # 设置代理
    chromeOptions.add_argument('--proxy-server={0}'.format(proxy))
    driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe",
                              options=chromeOptions)
    driver.get(url)
    event = threading.Event()
    event.wait(random.uniform(100, 120))
    driver.find_element_by_id('searchText').send_keys("医药")
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[2]/a').click()
    event.wait(10)
    driver.quit()


if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor

    threadPool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="thread_")
    while True:
        # 各浏览器数目
        chrome_num ,firefox_num ,_,_= rule()
        # ip总数
        all_num = chrome_num + firefox_num
        ip_url = "http://api.wandoudl.com/api/ip?app_key=b342b861c460906ba70b171b7a758b0c&pack=0&num=" + str(
            all_num) + "&xy=1&type=1&lb=\r\n&mr=1&area_id= "
        ip = requests.get(ip_url).text
        ip_list = ip.split()
        # 记录各浏览器循环次数
        firefox_flag = firefox_num
        chrome_flag = chrome_num

        for i in range(chrome_num + firefox_num):
            if chrome_flag > 0:
                if random.randint(1, 2) == 1:
                    threadPool.submit(direct_chrome, ip_list[i])
                else:
                    print("chrome_click")
                chrome_flag = chrome_flag - 1
                i = i + 1

            if firefox_flag > 0:
                if random.randint(1, 2) == 1:
                    threadPool.submit(direct_firefox, ip_list[i])
                else:
                    print("firefox_click")
                firefox_flag = firefox_flag - 1
                i = i + 1

        ip_list = []
        event = threading.Event()
        event.wait(random.uniform(130, 150))
        print("over")
