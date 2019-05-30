#coding:utf-8
import sys
sys.path.append("F:/selenium")
from bussiness.register_bussiness import RegisterBussiness
from selenium import webdriver
import unittest
import os
import HTMLTestRunner
import time

class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_name ='../image/test001.png' 

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.register_bussiness = RegisterBussiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        #报错截图
        for method_name,error in self._outcome.errors:
            if error:
#                self.driver.save_screenshot('../report/o1.png')
                case_name = self._testMethodName
                file_path = "../report/"+case_name+".png"
                self.driver.save_screenshot(file_path)
        self.driver.close()
#    @classmethod
#    def tearDownClass(cls):
        

    def test_login_email_error(self):
        email_error = self.register_bussiness.login_email_error('7888','321dd11','111111',self.file_name)
        print(email_error)
        self.assertFalse(email_error,'邮箱不正确')
#        if email_error ==True:
#            print('注册成功,测试失败')
#        else:
#            print('测试成功')

    def test_login_username_error(self):
        username_error = self.register_bussiness.login_name_error('7888@qq.com','311','111111',self.file_name)
        self.assertFalse(username_error)


    def test_login_password_error(self):
        password_error = self.register_bussiness.login_password_error('7888@qq.com','3114ee3','11',self.file_name)
        self.assertFalse(password_error)

    def test_login_code_error(self):
        code_error = self.register_bussiness.login_code_error('7888@qq.com','31122ww','111111',self.file_name)
        self.assertFalse(code_error)


if __name__ == '__main__':
    file_path = "../report/htmlreport.html"#创建一个文件路径
    fp = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report',description='good')#实例化HTMLTestRunner里面的类
    #runner = unittest.TextTestRunner()
    runner.run(suite)
