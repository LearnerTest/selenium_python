#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC 
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
import time
import random
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()#打开浏览器，最大化浏览器
time.sleep(5)
#print(EC.title_contains("注册"))
#for i in range(5):
#    user_email = ''.join(random.sample('123456789777',7))+'@163.com'#random.sample()方法随机生成数据,.join（）方法将list转换为字符串
#    print(user_email)


#locator = (By.CLASS_NAME,"controls")
#WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))#判断某个元素是否可见
#email_element = driver.find_element_by_id('register_email')
#print(email_element.get_attribute('placeholder'))#get_attribute方法获取属性对应的值
#email_element.send_keys('741297229@qq.com')
#print(email_element.get_attribute('value'))


driver.find_element_by_id('register_email').send_keys('741297229@qq.com')
driver.find_element_by_name('password').send_keys('123456')
user_name_element_node = driver.find_elements_by_class_name('controls')[1]
user_element = user_name_element_node.find_element_by_class_name('form-control')
user_element.send_keys('test')
#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys('111111')
#获取验证码图片

driver.save_screenshot("F:/selenium/02.png")#截取屏幕内容，保存到本地
code_element = driver.find_element_by_id('getcode_num')# 获取code元素坐标
#获取code图片坐标值
left_location = code_element.location['x']
top_location = code_element.location['y']
right_location = code_element.size['width'] + left_location
below_location = code_element.size['height'] + top_location
# 通过坐标值得到code image图
web_img = Image.open("F:/selenium/02.png")
code_img = web_img.crop((left_location,top_location,right_location,below_location))
#保存验证码图片
code_img.save("F:/selenium/03.png")
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"F:/selenium/03.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
time.sleep(3)
print(text) # 返回信息
driver.find_element_by_id('captcha_code').send_keys(text)
time.sleep(5)
driver.close()
