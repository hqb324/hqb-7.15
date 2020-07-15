import os
import pytest

from tools.data import excel_tool
from tools.api import request_tool

data = excel_tool.get_test_case("D:\\software\\Python\\auto_api_2006A\\test_case\\新建 XLSX 工作表 (3).xls")
# 充值
@pytest.mark.parametrize("acc_name,money,expect",data[1],ids=data[0])
def test_recharge(pub_data,acc_name,money,expect):
    pub_data["acc_name"] = acc_name
    pub_data["money"] = money
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    # story = '用户充值'  # allure报告中二级分类
    # title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=6aaac293f7b34392b1b1f50dfe9d501d; StuID=510'}
    status_code = 200  # 响应状态码
    expect = expect  # 预期结果
    json_data='''{
  "accountName": "${acc_name}",
  "changeMoney": "${money}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,json_data=json_data)