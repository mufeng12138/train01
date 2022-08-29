# encoding: utf-8
"""
@python version: 3.7
@author: mufeng12138
@file: mf_init_log.py
@time: 2019/11/25 18:30
"""
import logging


def log_init():
    logging.FileHandler(filename=r"log\my.log", encoding="utf-8")
    LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] ' \
                 '%(levelname)s %(message)s'
    DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'

    logging.basicConfig(filename = r"log\my.log",
                        level = logging.INFO,
                        format = LOG_FORMAT,
                        datefmt = DATE_FORMAT)

def log_teardown():
    logging.info("================================================")