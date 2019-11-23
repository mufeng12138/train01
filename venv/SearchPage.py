from selenium.webdriver.common.by import By
# from PODemo.BasePage \
import basePage
#假设baidu.py、BasePage.py均在PODemo.BasePage目录下
from selenium import webdriver

class SearchPage(basePage.base_page):
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

