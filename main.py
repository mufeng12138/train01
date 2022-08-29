# encoding: utf-8
"""
@version: 3.7
@author: mufeng
@file: main.py
@time: 2019/11/25 11:08
"""
import mf_log
import test_case
import mftools
import logging

url_bing = r"https://cn.bing.com"
url = r"https://www.baidu.com"

def positive_search(driver):
    mftools.locate_id(driver, "su")
    mftools.tag_name(driver, "form")
    mftools.link_text(driver, "新闻")
    mftools.partial_link_text(driver, "主页")
    mftools.class_name(driver, "s_ipt")
    mftools.name(driver, "wd")
    mftools.css_selector(driver, "#su")

def negative_search(driver):
    mftools.locate_id(driver, "1")
    mftools.tag_name(driver, "1")
    mftools.link_text(driver, "1")
    mftools.partial_link_text(driver, "1")
    mftools.class_name(driver, "1")
    mftools.name(driver, "1")
    mftools.css_selector(driver, "1")

def main():
    mf_log.log_init()
    driver = mftools.browser_init(url)
    # test_case.test_case()
    # mftools.mf_email()

    # positive_search(driver)
    # negative_search(driver)
    # mftools.clear_keys(driver)
    # mftools.refresh(driver)

    driver.find_element_by_link_text("新闻").click()
    try:
        assert "新闻" in driver.title
        logging.info("Assertion test pass.")
    except Exception as e:
        logging.error(e)
    # mftools.get_url(driver)
    # mftools.get_title(driver)
    # mftools.fb_ward(driver)
    # block
    # mftools.radio_button(driver)# fail



    # mftools.create_new_tab(driver, url_bing)
    # mftools.create_new_tab(driver)
    # mftools.tag_name(driver, "body")
    mftools.driver_close(driver)

if __name__ == "__main__" :
    main()