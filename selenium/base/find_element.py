#coding:utf-8
import sys
import time
sys.path.append("F:/selenium")
from selenium import webdriver
from util.read_ini import ReadIni


class FindElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        readini = ReadIni()
        data = readini.get_value(key)
        by = data.split('>')[0] #以‘>’切片
        value = data.split('>')[1]
        #print(value)
        try:
            if by =='id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
#            self.driver.save_screenshot('../report/o1.png')
            return None

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()#打开浏览器，最大化浏览器
    fd =FindElement(driver)
    driver.find_element_by_id('register_email').send_keys('741')
    driver.find_element_by_name('password').send_keys('123456')
    print(fd.get_element("user_email_error"))


