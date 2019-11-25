# train01
20191122_ui_test
PO Tutorial
PO教程
Definition	定义
PO 即 page object 页面对象，
1.是一种设计模式,用来管理维护一组页面元素的对象库。
2.在PO下,应用程序的每一个页面都有一个对应的Page类.
3.每一个Page类维护着该页面的元素集和操作这些元素的方法.
4.和面向对象的特性相同。面向对象的特性：封装、继承、多态。


Subject		主题
设计模式之PO设计模式在UI自动化上的应用

 

Disadvantages of traditional script	传统脚本的弊端
1.测试脚本未分离，维护成本高，牵一发而动全身。
2.可扩展性差，复用性低，只针对某个问题做解决方案。

Advantage	优势
二次封装，使开发者专注于变化的参数。
1.代码可读性强，掌握函数后，只专注于变化的参数，并作修改。
2.可维护性高，每次只改写特定的几个参数，不改内部函数。
3.复用性高，针对不同场景，封装了简便易用的函数，可直接调用，或任意搭配。

PO的核心要素：
1.在PO模式中抽象封装成一个BasePage类，该基类应该拥有一个只实现webdriver实例的属性。
2．每个一个page都继承BasePage，通过driver来管理本page中元素，将page中的操作封装成一个个的方法。

设计的原则
1.抽象每一个页面
2.页面中元素不暴露,仅报错操作元素的方法
3.页面不应该有繁琐的继承关系
4.页面中不是所有元素都需要涉及到,核型业务元素做建模使用
5.把页面划分功能模块,在Page中实现这些功能方法

案例1：baidu.py
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get(“http://www.baidu.com”)

driver.find_element_by_xpath("//input[@id=‘kw’]").send_keys(“Bela”)
driver.find_element_by_xpath("//input[@id=‘su’]").click()
sleep(5)
driver.quit()

分析
通过对baidu.py脚本的分析，可以提取到：
不同的运行脚本环境，浏览器不同：驱动webdriver.Firefox()可以剥离，
请求地址的变化（生产环境与测试环境）：url=http://www.baidu.com可以剥离
实际测试场景中，可能有多个测试场景，如果每个测试场景都需要维护url、浏览器驱动、元素定位等，效率会非常低。
因此基于对上面的分析，是否可以设计一个所有测试页面（selenium本身是对B/S系统开展测试）的基类，来维护一些公共的方法。

案例2：BasePage.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
“””
BasePage封装所有页面都公用的方法，例如driver, Find_Element等
“”"
# 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
# __init__方法不能有返回值，只能返回None
def __init__(self,selenium_driver,base_url):
    self.driver = selenium_driver
    self.base_url = base_url
    # self.pagetitle = pagetitle

def on_page(self,pagetitle):
    return pagetitle in self.driver.title

def _open(self,url):
    self.driver.get(url)
    self.driver.maximize_window()

def open(self):
    self._open(self.base_url,self.pagetitle)

def find_element(self,*loc):  #*loc任意数量的位置参数（带单个星号参数）
    # return self.driver.find_element(*loc)
    try:
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    except:

        print("%s 页面未能找到 %s 元素"%(self,loc))

def script(self,src):
    self.driver.excute_script(src)

def send_keys(self, loc, vaule, clear_first=True, click_first=True):
    try:
        loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
        if click_first:
            self.find_element(*loc).click()
        if clear_first:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(vaule)
    except AttributeError:
        print("%s 页面中未能找到 %s 元素" % (self, loc))


本例中设计了BasePage类，对一些webdriver的方法进行了二次封装
案例3：
from selenium.webdriver.common.by import By
from PODemo.BasePage import BasePage #假设baidu.py、BasePage.py均在PODemo.BasePage目录下
from selenium import webdriver

class SearchPage(BasePage):
# 定位元素
search_loc = (By.ID,"kw")
btn_loc = (By.ID,"su")

def open(self):
    self._open(self.base_url)

def search_content(self,content):
    BaiduContent = self.find_element(*self.search_loc)
    BaiduContent.send_keys(content)

def btn_click(self):
    BaiduBtn = self.find_element(*self.btn_loc)
BaiduBtn.click()


本例是basepage的子类，编写了实际应用场景中所用到的函数。在main文件中调用并实现。见github和文末代码。

参考文献
https://blog.csdn.net/hn8081com/article/details/82878468
 

番外篇——python命名规则
模块名：
小写字母，单词之间用_分割
参考python：logging
包名:
小写字母，单词之间用_分割
参考python：logging
类名：
单词首字母大写
参考：python class LogRecord(object):
普通变量：
小写字母，单词之间用_分割
参考：exc_info
实例变量：
以开头，小写字母，单词之间用分割
参考:_exc_info
以一个下划线开头的标识符(_xxx)，不能访问的类属性，但可通过类提供的接口进行访问，
不会被语句 “from module import *” 语句加载
私有实例变量：
以_开头（2个下划线），小写字母，单词之间用分割
参考:__private_var
外部访问会报错
专有变量：
开头，结尾，一般为python的自有变量，不要以这种方式命名
参考:doc
是系统定义的，具有特殊意义的标识符
普通函数：
小写字母，单词之间用_分割：
参考:get_name()
私有函数：
以__开头（2个下划线），小写字母，单词之间用分割
参考:__get_name()
外部访问会报错
注意：
_单下划线开头：弱“内部使用”标识，如：”from M import *”，将不导入所有以下划线开头的对象，包括包、模块、成员
单下划线结尾_：只是为了避免与python关键字的命名冲突
__双下划线开头：模块内的成员，表示私有成员，外部无法直接调用
包和模块：模块应该使用尽可能短的、全小写命名，可以在模块命名时使用下划线以增强可读性。同样包的命名也应该是这样的，虽然其并不鼓励下划线。
以上这些主要是考虑模块名是与文件夹相对应的，因此需要考虑文件系统的一些命名规则的，比如Unix系统对大小写敏感，而过长的文件名会影响其在Windows/Mac/Dos等系统中的正常使用。
类：几乎毫无例外的，类名都使用首字母大写开头(Pascal命名风格)的规范。使用_单下划线开头的类名为内部使用，上面说的from M import *默认不被告导入的情况。
异常：因为异常也是一个类，所以遵守类的命名规则。此外，如果异常实际上指代一个错误的话，应该使用“Error”做后缀

参考文献
https://blog.csdn.net/buhappy/article/details/50960861
 
代码黏贴
main.py
# encoding: utf-8
"""
@version: 3.7
@author: mufeng
@file: main.py
@time: 2019/11/25 11:08
"""

from selenium import webdriver
import base_page
import search_page
import time
import logging

LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] ' \
             '%(levelname)s %(message)s'
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'

logging.basicConfig(filename = r"log\my.log",
                    level = logging.INFO,
                    format = LOG_FORMAT,
                    datefmt = DATE_FORMAT)


def main():
    # url = r"https://cn.bing.com"
    url = r"https://www.baidu.com"
    driver = webdriver.Firefox()
    mf_content = r"python"
    mf_content2 = r"pycharm"
    # dr = base_page.BasePage(driver, url)
    dr2 = search_page.SearchPage(driver, url)
    dr2.open()
    logging.info("open browser")
    dr2.search_content(mf_content)
    logging.info("input content:{}".format(mf_content))
    dr2.btn_click()
    logging.info("click")
    time.sleep(5)
    logging.info("wait for 5 seconds")
    driver.close()
    logging.info("close browser")
    logging.info("===============================================")


if __name__ == "__main__" :
    main()

base_page.py
# encoding: utf-8

"""
@version: 3.7
@author: mufeng
@file: base_page.py
@time: 2019/11/25 11:08
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
# import time

# BasePage封装所有页面都公用的方法，例如driver, Find_Element等
# 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
# __init__方法不能有返回值，只能返回None
class BasePage(object):
    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url = base_url
        # self.pagetitle = pagetitle

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def open(self):
        self._open(self.base_url)#,self.pagetitle)

    def find_element(self,*loc):  #*loc任意数量的位置参数（带单个星号参数）
        # return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:

            print("%s 页面未能找到 %s 元素"%(self,loc))

    def script(self,src):
        self.driver.excute_script(src)

    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self, loc))

search_page.py
# encoding: utf-8

"""
@version: 3.7
@author: mufeng
@file: search_page.py
@time: 2019/11/25 11:08
"""

from selenium.webdriver.common.by import By
# from PODemo.BasePage \
import base_page
#假设baidu.py、BasePage.py均在PODemo.BasePage目录下
from selenium import webdriver

class SearchPage(base_page.BasePage):
    # 定位输入框元素
    search_loc = (By.ID,"kw")
    # 定位“百度一下”按钮元素
    btn_loc = (By.ID,"su")

    def open(self):
        self._open(self.base_url)

    def search_content(self,content):
        BaiduContent = self.find_element(*self.search_loc)
        BaiduContent.send_keys(content)

    def btn_click(self):
        BaiduBtn = self.find_element(*self.btn_loc)
        BaiduBtn.click()


