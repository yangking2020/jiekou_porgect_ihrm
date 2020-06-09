# 导包
import unittest

from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import assert_common, read_jsondata


# 测试类
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化
        cls.login_api = LoginApi()
    file_path = app.BASE_DIR + '/data/login_data.json'
    # 测试用例 登陆成功
    @parameterized.expand(read_jsondata(file_path))
    def test01_login_success(self,case_name,request_body,success,code,message,http_code):
        # 调用登陆
        response = self.login_api.login_ihrm(request_body,
                                  {"Content-Type": "application/json"})
        print(response.json())
        # 调用工具  断言
        assert_common(self,http_code,code,success,message,response)
    # 账号为空  有bug
    # def test02_login_account_null(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mobile": "", "password": "00000"},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,20001,False,'密码错误',response)
    # # 密码为空
    # def test03_login_password_null(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mobile": "13800000002", "password": ""},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,20001,False,'密码错误',response)
    # # 密码错误
    # def test04_login_password_error(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mobile": "13800000002", "password": "1230215"},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,20001,False,'密码错误',response)
    # # 无参
    # def test05_login_params_null(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,20001,False,'密码错误',response)
    # # 传入null
    # def test06_login_null(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm(None,
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     assert_common(self, 200, 99999, False, '系统繁忙', response)
    # # 多参
    # def test07_login_more_params(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mobile": "13800000002", "password": "123456","code":"0000"},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,10000,True,'操作成功',response)
    # # 少参 mobile
    # def test08_login_few_mobile(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"password": "123456"},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,20001,False,'密码错误',response)
    #
    # # 少参 password
    # def test09_login_few_password(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mobile": "13800000002"},
    #                                          {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self, 200, 20001, False, '密码错误', response)
    #
    # # 错误参数
    # def test10_login_wrong_password(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mboile": "13800000002","password": "123456"},
    #                                          {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self, 200, 20001, False, '密码错误', response)
    # # 账号错误
    # def test11_login_account_wrong(self):
    #     # 调用登陆
    #     response = self.login_api.login_ihrm({"mobile": "13800002222", "password": "123456"},
    #                               {"Content-Type": "application/json"})
    #     print(response.json())
    #     # 调用工具  断言
    #     assert_common(self,200,20001,False,'密码错误',response)