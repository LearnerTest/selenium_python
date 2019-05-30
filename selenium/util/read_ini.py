#coding:utf-8
import configparser#py3中需要小写

class ReadIni():
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'F:/selenium/config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()#初始化
        read_ini.read(self.file_path)#读取文件
        return read_ini
#通过key获取value
    def get_value(self,key,selection=None):
        if selection == None:
#            self.selection = 'RegisterElementIM'
            self.selection = 'RegisterElementIM'
        else:
            self.selection = selection
        try:
            value = self.data.get(self.selection,key)
        except :
            value = None
        return value

if __name__ == '__main__':
    readini = ReadIni()
    print(readini.get_value('user_name','RegisterElementIM'))