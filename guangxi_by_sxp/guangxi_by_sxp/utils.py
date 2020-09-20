from os.path import realpath, dirname
import json
import logging
logging.basicConfig(filename='guangxi.log', level=logging.DEBUG, format='%(asctime)s: %(message)s')


def get_config(name):
    path = dirname(realpath(__file__)) + '/spiders/website_config/' + name + '/config.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


# 日志装饰器
def logger(fn):
    def logger_in(*args):
        logging.info("begin")
        result = fn(*args)
        logging.info("end")
        return result
    return logger_in
