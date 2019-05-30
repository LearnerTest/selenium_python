#coding:utf-8
import sys
sys.path.append("F:/selenium")
import os
import ddt
import time
import unittest
import HTMLTestRunner
from selenium import webdriver
from bussiness.register_bussiness import RegisterBussiness
from util.operat_excel import OperatExcel

ox = OperatExcel()
data = ox.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):

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
                case_name = self._testMethodName
                file_path = "../report/"+case_name+".png"
                self.driver.save_screenshot(file_path)
        self.driver.close()
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    @ddt.data(*data)
    def test_register_error(self,data):
        email,username,password,file_name,assertCode,assertText = data
        email_error = self.register_bussiness.register_function(email,username,password,self.file_name,assertCode,assertText)
        #print(email_error)
        self.assertFalse(email_error,'邮箱不正确')

if __name__ == '__main__':
    file_path = "../report/htmlreport1.html"
    fp = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report',description='good')#实例化HTMLTestRunner里面的类
    #runner = unittest.TextTestRunner()
    runner.run(suite)
