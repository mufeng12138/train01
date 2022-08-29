# encoding: utf-8
"""
@version: 3.7
@author: mufeng
@file: test_case.py
@time: 2019/11/25 11:08
"""
from selenium import webdriver
import mf_log
import time
import base_page
import search_page

def test_case():
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
    # logging.info("===============================================")
    mf_init_log.log_teardown()