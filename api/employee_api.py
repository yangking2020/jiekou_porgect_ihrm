# 导包
import requests
# 封装添加员工接口
class EmployeeApi:
    def __init__(self):
        self.employee_url = "http://ihrm-test.itheima.net" + "/api/sys/user"
    # 添加员工
    def add_emp_api(self,username,mobile,headers):
        return requests.post(url=self.employee_url,
                                 json={"username": username,
                                       "mobile": mobile,
                                       "timeOfEntry": "2020-05-25",
                                       "formOfEmployment": 1,
                                       "departmentName": "测试部",
                                       "departmentId": "1063678149528784896",
                                       "correctionTime": "2020-05-30T16:00:00.000Z"},
                                 headers=headers)
    # 查询员工
    def query_emp_api(self,emp_id,headers):
        return requests.get(url=self.employee_url + '/'+ emp_id,
                            headers=headers)
    # 修改员工
    def modify_emp_api(self,emp_id,jsondata,headers):
        return requests.put(url=self.employee_url + '/'+ emp_id,
                        json = jsondata ,
                        headers = headers)
    # 删除员工
    def delete_emp_api(self,emp_id,headers):
        return requests.delete(url=self.employee_url + '/'+ emp_id,
                         headers = headers)

