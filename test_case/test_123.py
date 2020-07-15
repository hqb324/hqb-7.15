import random

import allure
import requests

from config.conf import API_URL

@allure.feature("用户管理")
@allure.story("扣款模块")
@allure.title("扣款接口-扣款成功")
def test_charge(db):
    with allure.step("第一步：执行SQL"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
    with allure.step("第二步：随机获取acc_name"):
        acc_name = random.choice(res)[0]
    with allure.step("第三步：准备请求数据"):
        data = {
        "accountName": acc_name,
        "changeMoney": 1
    }
    with allure.step("第四步：发送请求"):
        r = requests.post(API_URL+"/acc/charge",json=data)
    with allure.step("第五步：获取响应内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响应正文",allure.attachment_type.TEXT)
    # print(r.text)
    with allure.step("第六步：断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("扣款成功","预期结果",allure.attachment_type.TEXT)
        assert "扣款成功" in r.text