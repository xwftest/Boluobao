import os
import openpyxl


def getData(row_num, col_num):

    # 打开表文件
    workbook = openpyxl.load_workbook(os.path.dirname(os.path.dirname(__file__))+"/Data/data.xlsx")
    # 选中要读取的表
    sheet = workbook['Sheet1']
    # 读取指定行号和列号的内容
    value = sheet.cell(row=row_num, column=col_num).value
    # 关闭表文件
    workbook.close()
    return value


if __name__ == "__main__":
    value = getData(1,2)
    print(value)