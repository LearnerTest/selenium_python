#coding:utf-8
import sys
import time
sys.path.append("F:/selenium")
from handle.register_handle_IM import RegisterHandleIM

class RegisterBussinessIM():

    def __init__(self,driver):
        self.driver = driver
        self.register_handle_IM = RegisterHandleIM(self.driver)

    def user_base(self,username,password):
        self.register_handle_IM.send_user_name(username)
        self.register_handle_IM.send_user_password(password)
        self.register_handle_IM.click_login_button()
        

    def register_manger(self,username,password,code,name):
        self.user_base(username,password)
        time.sleep(2)
        self.register_handle_IM.click_servers()
        time.sleep(3)
        self.register_handle_IM.click_service_manger()
        time.sleep(3)
        self.register_handle_IM.click_add()
        time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[-1])#切换到弹框定位
        
        self.register_handle_IM.send_code(code)
        self.register_handle_IM.send_name(name)
        self.register_handle_IM.click_sure()


    def register_user(self,username,password,phone):
        self.user_base(username,password)
        time.sleep(2)
        self.register_handle_IM.click_user_manger()
        time.sleep(1)
        self.register_handle_IM.click_login_user()
        time.sleep(1)
        self.register_handle_IM.click_modify_phone()
        time.sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.register_handle_IM.send_new_phone(phone)
        self.register_handle_IM.click_save_button()


    def login_success(self):
        if self.register_handle_IM.login_button_text() ==None:
            return True
        else:
            return False