#coding:utf-8
import xlrd

class OperatExcel():

    def __init__(self,file_name=None,sheets_id=None):
        if file_name ==None:
            self.file_name = '../config/casedata.xls'
            self.sheets_id = 0
        else:
            self.file_name = file_name
            self.sheets_id = sheets_id
        self.data = self.get_tables()

    def get_tables(self):#获取表格数据
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheets_id]
        return tables

    def get_nrows(self):#获取行数
        tables = self.data
        rows =tables.nrows
        return rows

    def get_data(self):
        result = []
        rows = self.get_nrows()
        for i in range(rows):
            col = self.data.row_values(i)
            result.append(col)
        return result





if __name__ == '__main__':
    op =OperatExcel()
    print(op.get_data())
