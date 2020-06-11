# 导包
import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
from app import BASE_DIR

# 生成测试套件
suite = unittest.TestLoader().discover('./script','test*.py')
# 定义报告名
# file_name = BASE_DIR +'/report/ihrm%s.html' % time.strftime('%Y%m%d%H%M%S')
file_name = BASE_DIR +'/report/report.html'
# 运行并写入
with open(file_name,'wb') as f:
    runner = HTMLTestRunner(f,title='ihrm测试报告',description='完美的报告')
    runner.run(suite)