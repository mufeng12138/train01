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

