from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import *

# 简单地说:定位文件用的
app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r"/*")

# 已注册的用户
userList = [
    ('nio', '123123'),
    ('beis', '456456'),
    ('chuxiny', '789789')
]
# 登陆成功信息
success_ful = {
    'msg': '登陆成功',
    'status': '200'
}
# 登录失败信息
fail_ful = {
    'msg': '登陆失败',
    'status': '405'
}
# 用户信息
userInfo = {
    'nio': {
        'data': {
            'id': 500,
            'rid': 0,
            'username': 'Nio',
            'email': '774801556@qq.com',
            'token': 'a',
        },
    }, 'beis': {
        'data': {
            'id': 600,
            'rid': 0,
            'username': 'Beis',
            'email': '000118@qq.com',
            'token': 'b',
        },
    }, 'chuxiny': {
        'data': {
            'id': 700,
            'rid': 0,
            'username': 'ChuXinY',
            'email': '111@qq.com',
            'token': 'c',
        },
    },
}
# 左侧菜单数据
menu = {
    "data":
        [
            {
                "id": 101,
                "authName": "商品管理",
                "path": "goods",
                "children": [
                    {
                        "id": 104,
                        "authName": "商品列表",
                        "path": 'goods1',
                        "children": [
                            {
                        "id": 903,
                        "authName": "角色列表",
                        "path": 'goods1',
                            },
{
                        "id": 904,
                        "authName": "权限列表",
                        "path": 'goods2',
                            }
                        ]
                    }
                ]
            },
{
                "id": 103,
                "authName": "权限管理",
                "path": "rights",
                "children": [
                    {
                        "id": 114,
                        "authName": "权限列表",
                        "path": 'rights1',
                        "children": [
                            {
                        "id": 901,
                        "authName": "角色列表",
                        "path": 'rights1',
                            },
{
                        "id": 902,
                        "authName": "权限列表",
                        "path": 'rights2',
                            }
                        ]
                    }
                ]
            },{
                "id": 102,
                "authName": "订单管理",
                "path": "orders",
                "children": [
                    {
                        "id": 124,
                        "authName": "订单列表",
                        "path": 'orders',
                        "children": [
                            {
                        "id": 905,
                        "authName": "角色列表",
                        "path": 'orders1',
                            },
{
                        "id": 906,
                        "authName": "权限列表",
                        "path": 'orders2',
                            }
                        ]
                    }
                ]
            },{
                "id": 145,
                "authName": "数据统计",
                "path": "reports",
                "children": [
                    {
                        "id": 134,
                        "authName": "数据列表",
                        "path": 'reports',
                        "children": [
                            {
                        "id": 907,
                        "authName": "角色列表",
                        "path": 'reports1',
                            },
{
                        "id": 908,
                        "authName": "权限列表",
                        "path": 'reports2',
                            }
                        ]
                    }
                ]
            },
        ]
,
    "meta":{
        "msg":"获取菜单列表成果",
        "status":200
    }
}

@app.route('/index')
@cross_origin()
def index():
    return 'This is index!'


# 导出环境变量
# set FLASK_APP=basicFlask.py
# 运行flask, 默认端口为5000
# flask run --host=0.0.0.0 --port=8001

# axios发送两次请求:1.options请求,用于检测网络请求是否正常;2.设置的POST请求
@app.route('/login', methods=['GET', 'POST'])
# 用于跨域验证
@cross_origin()
def login():
    print(request)
    if request.method == 'POST':
        print(request)
        # post请求+表单
        try:
            username = request.form.get("username").lower()
            password = request.form.get('password')
        except:
            try:
                # post请求+非表单
                username = request.values.get("username").lower()
                password = request.values.get('password')
                print(username)
            except:
                # axios和flask通信, 必须使用get_json才能收到数据
                data = request.get_json()
                username = data['username'].lower()
                password = data['password']

        print(username, password)
        # 认证登录信息
        try:
            ret_info = {}
            # 如果正确
            if (username, password) in userList:
                ret_info = userInfo[username]
                ret_info['meta'] = success_ful
            else:
                ret_info['data'] = 'null'
                ret_info['meta'] = fail_ful
            # json格式返回数据
            print(ret_info)
            return jsonify(ret_info)
        except Exception as e:
            print(e)
            return 'No User!'
    else:
        return 'Null Value!'

@app.route('/menus',methods=['GET'])
@cross_origin()
def menus():
    # 获得请求体所有内容
    headers = request.headers
    # 验证token
    if headers['Authorization'] is not None:
        return jsonify(menu)
    return '获取失败!'

app.run(host='192.168.1.9', port=8081)
