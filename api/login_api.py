import requests
# 登陆的接类
class LoginApi:
    def __init__(self):
        # 初始化登陆接口的url
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"
    # 发送登陆请求
    def login_ihrm(self,json,header):
        return requests.post(url=self.login_url,json=json,headers=header)

