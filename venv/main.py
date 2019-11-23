# coding=utf-8
# author = "mufeng"
# title = 摘取网页上全部邮箱

from selenium import webdriver
import mfemail
import basePage
import SearchPage


def main():
    url = r"https://cn.bing.com"
    driver = webdriver.Chrome()
    # mfemail.mf_email()
    dr = basePage.base_page(driver, url)
    dr.open()
    dr.find_element()

if __name__ == "__main__" :
    main()