# 导包
import unittest
from parameterized import parameterized
import app
from api.employee_api import EmployeeApi
from api.login_api import LoginApi
import logging
from utils import assert_common, read_emp_data


# 测试类

class TestEmpioyee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化
        cls.employee_api = EmployeeApi()
        cls.login_api = LoginApi()

    # 测试用例 登陆成功
    def test01_login_success(self):
        # 调用登陆
        response = self.login_api.login_ihrm({"mobile": "13800000002", "password": "123456"},
                                             {"Content-Type": "application/json"})
        # 打印登陆结果
        logging.info(response.json())
        assert_common(self, 200, 10000, True, '操作成功', response)
        # 获取令牌
        token = 'Bearer ' + response.json().get('data')
        # 将令牌拼接成headers
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info(app.HEADERS)

    filepath2 = app.BASE_DIR + "/data/employee_data.json"

    # 添加员工
    @parameterized.expand(read_emp_data(filepath2, "add_emp"))
    def test02_add_emp(self, username, mobile, success, code, message, http_code):
        # 调用添加员工接口
        response = self.employee_api.add_emp_api(username, mobile, app.HEADERS)
        # 打印结果
        logging.info(response.json())
        # 提取员工id
        app.EMP_ID = response.json().get('data').get('id')
        # 打印员工id
        logging.info(app.EMP_ID)
        assert_common(self, http_code, code, success, message, response)

    # 查询员工接口
    @parameterized.expand(read_emp_data(filepath2, "query_emp"))
    def test03_query_emp(self, success, code, message, http_code):
        # 调用查询员工接口
        response = self.employee_api.query_emp_api(app.EMP_ID, app.HEADERS)
        # 打印内容
        logging.info(response.json())
        assert_common(self, http_code, code, success, message, response)

    @parameterized.expand(read_emp_data(filepath2, "modify_emp"))
    def test04_modify_emp(self, username, success, code, message, http_code):
        # 调用修改员工接口
        response = self.employee_api.modify_emp_api(app.EMP_ID, {"username": username}, app.HEADERS)
        # 打印内容
        logging.info(response.json())
        assert_common(self, http_code, code, success, message, response)

    @parameterized.expand(read_emp_data(filepath2, "delete_emp"))
    def test05_delete_emp(self, success, code, message, http_code):
        # 调用修改员工接口
        response = self.employee_api.delete_emp_api(app.EMP_ID, app.HEADERS)
        # 打印内容
        logging.info(response.json())
        assert_common(self, http_code, code, success, message, response)
