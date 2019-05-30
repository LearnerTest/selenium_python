#coding:utf-8
import sys
import time
sys.path.append("F:/selenium")
from base.find_element import FindElement
from util.get_code import GetCode

class RegisterHandle():

    def __init__(self,driver):
        self.driver = driver
        self.find_element = FindElement(self.driver)

#输入邮箱
    def send_user_email(self,email):
        self.find_element.get_element('user_email').send_keys(email)
#输入用户名
    def send_user_name(self,username):
        self.find_element.get_element('user_name').send_keys(username)
#输入密码
    def send_user_password(self,password):
        self.find_element.get_element('password').send_keys(password)
#输入验证码
    def send_user_code(self,file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.find_element.get_element('code_text').send_keys(code)

#点击登录
    def click_register_button(self):
        self.find_element.get_element('register_button').click()

#获取注册按钮文字
    def register_button_text(self):
        self.find_element.get_element('register_button').text

#获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.find_element.get_element("user_email_error").text
            elif info =='user_name_error':
                text = self.find_element.get_element('user_name_error').text
            elif info == 'password_error':
                text = self.find_element.get_element('password_error').text
            else:
                text = self.find_element.get_element('code_text_error').text
        except:
            text = None
        return text


