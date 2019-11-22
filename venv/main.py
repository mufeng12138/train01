# coding=utf-8
# author = "mufeng"
# title = 摘取网页上全部邮箱

from selenium import webdriver
import re
import logging

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
# DATE_FORMAT = "%m/%d/%Y  &H:%M:%S  %P"
# logging.basicConfig(filename = "my.log",
#                     level= logging.DEBUG,
#                     format = LOG_FORMAT,
#                     datefmt = DATE_FORMAT)

logging.basicConfig(filename = "my.log",
                    level = logging.INFO,
                    format = LOG_FORMAT,
                    datefmt = DATE_FORMAT)

url = r"http://home.baidu.com/contact.html"

def mf_email():
    # print("hello mf")
    driver = webdriver.Chrome()
    logging.info("open browser")
    # logging.debug("User %s is loging" % 'jeck')
    # logging.info("User %s attempted wrong password" % 'fuzj')
    # logging.warning("user %s attempted wrong password more than 3 times" % 'mary')
    # logging.error("select db is timeout")
    # logging.critical("server is down")
    driver.get(url)
    # logging.info("link url")
    doc = driver.page_source
    # logging.info("get page")
    emails = re.findall(r'[\w]+@[\w\.-]+', doc)
    for email in emails:
        print(email)
    # driver.close()


def main():
    mf_email()

if __name__ == "__main__" :
    main()