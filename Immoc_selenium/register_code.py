#coding:utf-8
import sys
import time
sys.path.append("F:/selenium")
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from ShowapiRequest import ShowapiRequest
import random
from base.find_element import FindElement

class RegisterCode():

    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #初始化driver
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Edge()
        driver.get(url)#打开浏览器
        driver.maximize_window()#打开浏览器，最大化浏览器
        return driver
        time.sleep(5)

    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    #获取元素
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    #随机获取用户信息
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567897adjfljljjlfsvs',8))#random.sample()方法随机生成数据,.join（）方法将list转换为字符串
        return user_info
    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)#截取屏幕内容，保存到本地
        code_element = self.get_user_element('code_image')# 获取code元素坐标
        #获取code图片坐标值
        left_location = code_element.location['x']
        top_location = code_element.location['y']
        right_location = code_element.size['width'] + left_location
        below_location = code_element.size['height'] + top_location
        # 通过坐标值得到code image图
        web_img = Image.open(file_name)
        code_img = web_img.crop((left_location,top_location,right_location,below_location))
        #保存验证码图片
        code_img.save(file_name)

    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
    #    r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        print(text)
        return text

    def run_main(self):
         user_name_info = self.get_range_user()
         user_email = user_name_info + '@163.com'
         file_name = 'F:/selenium/image/03.png'
         code_text = self.code_online(file_name)
         self.send_user_info('user_email',user_email)
         self.send_user_info('user_name',user_name_info)
         self.send_user_info('password','111111')
         self.send_user_info('code_text',code_text)
         self.get_user_element('register_button').click()
         code_error = self.get_user_element('code_text_error')
         tamp = int(time.time())
         filename = '../image/ %s.png' %tamp
         if code_error == None:
            print('注册成功')
         else:
            self.driver.save_screenshot(filename)

         time.sleep(5)
         self.driver.close()

if __name__ == '__main__':
    registercode = RegisterCode('http://www.5itest.cn/register',1)
    registercode.run_main()






