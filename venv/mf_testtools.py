# encoding: utf-8
"""
@python version: 3.7
@author: mufeng12138
@file: mf_email.py
@time: 2019/11/25 18:30
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import mf_log
import logging
import time

def browser_init(url):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    # driver.set_window_size(768, 900)
    # driver.set_window_position(484, 0)
    # driver.set_window_size(1024,768)
    # driver.implicitly_wait(2)
    return driver

def mf_email():
    url = r"http://home.baidu.com/contact.html"
    # print("hello mf")
    driver = webdriver.Firefox()
    logging.info("open browser")
    # logging.debug("User %s is loging" % 'jeck')
    # logging.info("User %s attempted wrong password" % 'fuzj')
    # logging.warning("user %s attempted wrong password more than 3 times" % 'mary')
    # logging.error("select db is timeout")
    # logging.critical("server is down")
    driver.get(url)
    logging.info("link url")
    doc = driver.page_source
    logging.info("get page")
    emails = re.findall(r'[\w]+@[\w\.-]+', doc)
    for email in emails:
        print(email)
    driver.close()
    # logging.info("======================================")
    mf_init_log.log_teardown()

def locate_id(driver, loid):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_id(loid)
        logging.info(u'test pass: ID \"{}\" found'.format(loid))
    except Exception as e:
        logging.error(e)


def tag_name(driver, tagName):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_tag_name(tagName)
        logging.info(u'test pass: tag name \"{}\" found'.format(tagName))
    except Exception as e:
        logging.error(e)


def link_text(driver, linkText):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_link_text(linkText)
        # print(linkText)
        logging.info('test pass: link text \"{}\" found'.format(linkText))
    except Exception as e:
        logging.error(e)


def partial_link_text(driver, partial_link_text):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_partial_link_text(partial_link_text)
        # print(linkText)
        logging.info('test pass: element by partial link text \"{}\" found '
                     .format(partial_link_text))
    except Exception as e:
        logging.error(e)

def class_name(driver, class_name):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_class_name(class_name)
        # print(linkText)
        logging.info('test pass: element by class name \"{}\" found '
                     .format(class_name))
    except Exception as e:
        logging.error(e)

def name(driver, name):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_name(name)
        # print(linkText)
        logging.info('test pass: element by name \"{}\" found '
                     .format(name))
    except Exception as e:
        logging.error(e)

def css_selector(driver, css_selector):
    # driver = browser_init()
    # driver.get(url)
    try:
        driver.find_element_by_css_selector(css_selector)
        # print(linkText)
        logging.info('test pass: element by css_selector \"{}\" found '
                     .format(css_selector))
    except Exception as e:
        logging.error(e)

def clear_keys(driver):
    # driver = browser_init()
    # driver.get(url)
    driver.find_element_by_id("kw").send_keys("Selenium")
    time.sleep(2)
    try:
        driver.find_element_by_id("kw").clear()  # 调用clear()方法去清除
        logging.info('test pass: clear successful')
        time.sleep(2)
    except Exception as e:
        logging.error(e)

def refresh(driver):
    # driver = browser_init()
    # driver.get(url)
    driver.find_element_by_id("kw").send_keys("Selenium")
    time.sleep(2)
    try:
        driver.refresh()  # 刷新方法 refresh
        logging.info('test pass: refresh successful')
        time.sleep(2)
    except Exception as e:
        logging.error(e)

def fb_ward(driver):
    # elem_news = driver.find_element_by_link_text("新闻")
    # elem_news.click()
    # logging.info('click button')
    # time.sleep(1)
    driver.back()
    logging.info('get back')
    time.sleep(1)

    driver.forward()
    logging.info('go forward')
    time.sleep(1)

def get_url(driver):
    # version = driver.current_url
    # driver.find_element_by_link_text("新闻").click()
    logging.info('get current_url:{}'.format(driver.current_url))
    time.sleep(1)
    # print(driver.current_url)

def get_title(driver):
    # version = driver.current_url
    # driver.find_element_by_link_text("新闻").click()
    logging.info('get title:{}'.format(driver.title))
    time.sleep(1)

def create_new_tab(driver, url):
    try:
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, 'n')
        driver.get(url)
        logging.info("create a new tab")
        time.sleep(2)
    except Exception as e:
        logging.error(e)

def radio_button(driver):

    try:
        driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@name='memberPass']").click()
        logging.info("select the radio")
        time.sleep(2)
    except Exception as e:
        logging.error(e)



def driver_close(driver):
    driver.quit()
    mf_log.log_teardown()