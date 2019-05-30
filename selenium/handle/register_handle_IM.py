#coding:utf-8
import sys
#import time
sys.path.append("F:/selenium")
from base.find_element import FindElement

class RegisterHandleIM():

    def __init__(self,driver):
        self.driver = driver
        self.find_element = FindElement(self.driver)
        
    def send_user_name(self,user_name):
        self.find_element.get_element('user_name').send_keys(user_name)

    def send_user_password(self,password):
        self.find_element.get_element('password').send_keys(password)

#点击登录
    def click_login_button(self):
        self.find_element.get_element('login').click()

    #获取注册按钮文字
    def login_button_text(self):
        return self.find_element.get_element('login').text

    #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info =='user_name_error':
                text = self.find_element.get_element('user_name_error').text
            else:
                text = self.find_element.get_element('password_error').text
        except:
            text = None
        return text
    #点击服务管理
    def click_servers(self):
        self.find_element.get_element('service').click()
    #点击服务管理
    def click_service_manger(self):
        self.find_element.get_element('service_manger').click()

    def click_add(self):
        self.find_element.get_element('add').click()

    def send_code(self,code):
        self.find_element.get_element('code').send_keys(code)

    def send_name(self,name):
        self.find_element.get_element('name').send_keys(name)

    def click_sure(self):
        self.find_element.get_element('sure').click()

    def click_user_manger(self):#点击用户管理
        self.find_element.get_element('usermanger').click()

    def click_login_user(self):
        self.find_element.get_element('loginuser').click()

    def click_modify_phone(self):
        self.find_element.get_element('modifyphone').click()

    def send_new_phone(self,phone):
        self.find_element.get_element('newphone').send_keys(phone)
        
    def click_save_button(self):
        self.find_element.get_element('savabutton').click()
    

    