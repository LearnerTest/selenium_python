#coding:utf-8
import sys
sys.path.append("F:/selenium")
from bussiness.register_bussinessIM import RegisterBussinessIM
from selenium import webdriver
import unittest
import time 
import HTMLTestRunner


class FirstCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://yd.epsoft.com.cn/eps/#/login')
        self.driver.maximize_window()
        self.register_bussiness = RegisterBussinessIM(self.driver)


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

#    def test_login_success(self):
#        success = self.register_bussiness.user_base('admin','ydkf2000')
#        self.assertFalse(success)

#    def test_register_manger(self):
#        ver = self.register_bussiness.register_manger('admin','ydkf2000','01311','测试赛')
#        self.assertFalse(ver)


    def test_modify(self):
        phone = self.register_bussiness.register_user('admin','ydkf2000','18800000001')
        self.assertFalse(phone)



if __name__ == '__main__':
    file_path = "../report/htmlreport.html"#创建一个文件路径
    fp = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report',description='公共服务测试')#实例化HTMLTestRunner里面的类
    #runner = unittest.TextTestRunner()
    runner.run(suite)