# 线程: 线程可以理解成执行代码的分支， 线程是执行对应的代码的， cpu调度线程去执行对应代码
import sys
import time
import threading
import random
from selenium.webdriver.firefox.options import Options
import requests
from selenium import webdriver
from princeple import princeple


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
        princ=princeple()
        chrome_num ,firefox_num ,_,_= princ.rule()
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
