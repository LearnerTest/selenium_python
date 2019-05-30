#coding:utf-8
import sys
import time
sys.path.append("F:/selenium")
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time

class GetCode():

    def __init__(self,driver):
        self.driver =driver

    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)#截取屏幕内容，保存到本地
        code_element = self.driver.find_element_by_id('getcode_num')# 获取code元素坐标
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
        time.sleep(2)

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
        #print(text)
        time.sleep(2)
        return text