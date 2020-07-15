from tools.api import request_tool


def test_sign(pub_data):
    # pub_data["username"] = "hqb123456"
    # pub_data["phone"] = "14578945615"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "phone": "自动生成 手机号",
  "pwd": "hqb123",
  "rePwd": "hqb123",
  "userName": "自动生成 字符串 5 数字 hqb"
}
    '''
    status_code = 200  # 响应状态码
    expect = "注册成功"  # 预期结果
    json_path = [{"cstid":'$.data.cstId'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_post_json(pub_data):
    pub_data["certno"] = "自动生成 身份证号"
    pub_data["cstName"] = "自动生成 姓名"
    pub_data["email"]="自动生成 邮箱"
    header = {"token":pub_data["token"]}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户认证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "cstId": "${cstid}",
  "customerInfo": {
    "birthday": "2020-01-01",
    "certno": "${certno}",
    "city": "上海市区",
    "cstName": "${cstName}",
    "email": "${email}",
    "province": "上海市",
    "sex": 1
  }
}
    '''
    status_code = 200  # 响应状态码
    expect = "认证成功"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(headers = header,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)