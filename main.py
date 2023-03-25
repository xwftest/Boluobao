import unittest
import os
import HTMLTestRunner
import time
from Public.send_email import send_email


def getSuite():
    # start_dir=加载所有的测试模块来执行,pattern=通过正则的模式加载所有的模块
    startdir = os.path.dirname(__file__) + "\TestCase"
    '''获取所有执行的测试模块'''
    suite = unittest.TestLoader().discover(
        start_dir=startdir,
        pattern='test_*.py'
    )
    return suite


# 获取当前时间
def getNowtime():
    return time.strftime("%y-%m-%d %H_%M_%S", time.localtime(time.time()))


# 执行获取的测试模块,并获取测试报告
def runAll(filename):
    #filename = os.path.join(os.path.dirname(__file__), 'Report', getNowtime() + "report.html")
    # 把测试报告写入文件中,b是以二进制的方式写入
    fp = open(filename, "wb")
    # HTMLTestRunner实例化的过程，stream是流式写入，title是测试报告的标题，description是对测试报告的描述
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="菠萝包UI自动化测试报告汇总",
        description="UI自动化测试报告"
    )
    runner.run(getSuite())


if __name__ == '__main__':
    filename = os.path.join(os.path.dirname(__file__), 'Report', getNowtime() + "report.html")
    runAll(filename)
    send_email(filename)
    print("执行完毕！")
