# coding=utf-8
# author = "mufeng"
# title = 摘取网页上全部邮箱

from selenium import webdriver
import mf_email
import base_page
import search_page
import time


def main():
    # url = r"https://cn.bing.com"
    url = r"https://www.baidu.com"
    driver = webdriver.Chrome()
    mf_content = r"python"
    mf_content2 = r"pycharm"
    # mfemail.mf_email()
    # dr = base_page.BasePage(driver, url)
    dr2 = search_page.SearchPage(driver, url)
    dr2.open()
    dr2.search_content(mf_content)
    dr2.btn_click()
    time.sleep(5)


if __name__ == "__main__" :
    main()