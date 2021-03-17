# 线程: 线程可以理解成执行代码的分支， 线程是执行对应的代码的， cpu调度线程去执行对应代码
import time
import threading
from selenium import webdriver


def zgyq():
    opt = webdriver.ChromeOptions()  # 创建浏览器
    # opt.set_headless()                            #无窗口模式
    driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
    driver.get('https://www.baidu.com/')  # 打开网页
    # driver.maximize_window()                      #最大化窗口  # 加载等待

    # driver.find_element_by_xpath("./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys(
    #    "ZGYQ")  # 利用xpath查找元素进行输入文本
    driver.find_element_by_id('kw').send_keys("ZGYQ")

    # driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()  # 点击按钮
    driver.find_element_by_xpath("//input[@value='百度一下']").click()
    # driver.find_element_by_link_text("ZGYQ_企业商标大全_商标信息查询_爱企查").click()
    # driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input[type='submit'][value='百度一下']").click()#候选方法,多条件匹配
    time.sleep(20)


# 唱歌
def xmu():
    opt = webdriver.ChromeOptions()  # 创建浏览器
    # opt.set_headless()                            #无窗口模式
    driver = webdriver.Chrome(options=opt)  # 创建浏览器对象
    driver.get('https://www.baidu.com/')  # 打开网页
    # driver.maximize_window()                      #最大化窗口
    # 加载等待

    # driver.find_element_by_xpath("./*//span[@class='bg s_ipt_wr quickdelete-wrap']/input").send_keys(
    #     "魅族")  # 利用xpath查找元素进行输入文本
    driver.find_element_by_id('kw').send_keys("xmu") #候选方法

    # driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input").click()  # 点击按钮
    driver.find_element_by_xpath("//input[@value='百度一下']").click()
    # driver.find_element_by_xpath("//span[@class='bg s_btn_wr']/input[type='submit'][value='百度一下']").click()#候选方法,多条件匹配

    time.sleep(20)


if __name__ == '__main__':

    # 获取当前执行代码的线程
    current_thread = threading.current_thread()
    print("main:", current_thread)
    # 获取程序活动线程的列表
    thread_list = threading.enumerate()
    # print("111:", thread_list)
    # 创建跳舞的线程
    baidu_thread = threading.Thread(target=xmu)
    ZGYQ_thread = threading.Thread(target=zgyq)
    # print("sing_thread:", sing_thread)
    thread_list = threading.enumerate()
    # 启动线程执行对应的任务
    baidu_thread.start()
    thread_list = threading.enumerate()
    print("222:", thread_list)
    ZGYQ_thread.start()
    # 提示:线程执行完成任务以后该线程就会销毁
    thread_list = threading.enumerate()
    print("333:", thread_list, len(thread_list))
    # 扩展-获取活动线程的个数
    active_count = threading.active_count()
    print(active_count)
    # 注意点： 线程之间执行是无序的，由cpu调度决定的
