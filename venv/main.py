# encoding: utf-8
"""
@version: 3.7
@author: mufeng
@file: main.py
@time: 2019/11/25 11:08
"""
import mf_log
import test_case
import mf_testtools

# url = r"https://cn.bing.com"
url = r"https://www.baidu.com"

def positive_search(driver):
    mf_testtools.locate_id(driver, "su")
    mf_testtools.tag_name(driver, "form")
    mf_testtools.link_text(driver, "新闻")
    mf_testtools.partial_link_text(driver, "主页")
    mf_testtools.class_name(driver, "s_ipt")
    mf_testtools.name(driver, "wd")
    mf_testtools.css_selector(driver, "#su")


def negative_search(driver):
    mf_testtools.locate_id(driver, "1")
    mf_testtools.tag_name(driver, "1")
    mf_testtools.link_text(driver, "1")
    mf_testtools.partial_link_text(driver, "1")
    mf_testtools.class_name(driver, "1")
    mf_testtools.name(driver, "1")
    mf_testtools.css_selector(driver, "1")

def main():
    mf_log.log_init()
    driver = mf_testtools.browser_init(url)
    # test_case.test_case()
    # mf_testtools.mf_email()

    # positive_search(driver)
    # negative_search(driver)
    # mf_testtools.clear_keys(driver)
    # mf_testtools.refresh(driver)

    # driver.find_element_by_link_text("新闻").click()
    # mf_testtools.get_url(driver)
    # mf_testtools.get_title(driver)
    # mf_testtools.fb_ward(driver)
    mf_testtools.create_new_tab(driver)
    mf_testtools.create_new_tab(driver)

    mf_testtools.driver_close(driver)

if __name__ == "__main__" :
    main()