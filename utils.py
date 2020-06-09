# 导包
import json
import app
from logging import handlers
import logging
# 封装类 生成日志
def init_logging():
    # 生成日志器
    logger = logging.getLogger()
    # 设置级别
    logger.setLevel(level=logging.INFO)
    # 处理器 (控制台,文件)
    sh = logging.StreamHandler()
    file_name = app.BASE_DIR + '/log/ihrm.log'
    tr = logging.handlers.TimedRotatingFileHandler(file_name,when='M',interval=1,backupCount=2,encoding='utf-8')
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    sh.setFormatter(formatter)
    tr.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(tr)
# 封装断言
def assert_common(self,http_code,code,success,message,response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(code, response.json().get('code'))
    self.assertEqual(success, response.json().get('success'))
    self.assertIn(message, response.json().get('message'))
def read_jsondata(filepath):
    new_list = []
    # 读取数据文件
    with open(filepath,encoding='utf-8') as f:
        # 专成py格式
        jsondata = json.load(f)
        # 遍历
        for i in jsondata:
            new_list.append(list(i.values()))
        # 返回
        return new_list
# 编写读取员工模块的数据函数
def read_emp_data(filepath, interface_name):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 把数据文件加载成json格式
        jsonData = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        emp_data = jsonData.get(interface_name) #type:dict
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = []
        result_list.append(tuple(emp_data.values()))
        # 返回数据
    print("读取的{}员工数据为:{}".format(interface_name,result_list))
    return result_list

if __name__ == '__main__':
    # # 定义数据文件的目录（注意这个路径指向数据文件一定需要存在）
    # filepath = app.BASE_DIR + "/data/login_data.json"
    # # 读取路径中的数据，并接收返回结果
    # result = read_login_data(filepath)
    # # 打印返回的结果
    # print("返回的result_list的结果为：", result)

    # 定义员工数据路径
    filepath2 = app.BASE_DIR + "/data/employee_data.json"
    # 读取员工数据
    read_emp_data(filepath2, 'add_emp')
    read_emp_data(filepath2, 'query_emp')
    read_emp_data(filepath2, 'modify_emp')
    read_emp_data(filepath2, 'delete_emp')