# FastAPI后台
from typing import Optional
from fastapi import FastAPI, Form, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
            }, {
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
        }, {
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
    "meta": {
        "msg": "获取菜单列表成果",
        "status": 200
    }
}

app = FastAPI()

# uvicorn Postman_test:app --reload --host 192.168.1.9 --port 8081
# 设置跨域验证(https://fastapi.tiangolo.com/zh/tutorial/cors/)
# 将允许的url请求连接放入这里面
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    # vue 的url
    "http://192.168.1.9:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # 允许所有方法
    allow_methods=["*"],
    # 允许所有请求头
    allow_headers=["*"],
)
class info(BaseModel):
    username:str
    password:str

# 解决axios的post传参问题
@app.post('/user/login/')
async def login(username:str=Form(None),password:str=Form(None)):
    print(username, password)
    username = username.lower()
    ret_info ={}
    if (username,password) in userList:
        ret_info = userInfo[username]
        ret_info['meta'] = success_ful
    else:
        ret_info['data'] = 'null'
        ret_info['meta'] = fail_ful
    return ret_info

@app.get('/info/menus/')
def menus(Authorization:Optional[str] = Header(None)):
    # 验证token
    print(Authorization)
    if Authorization is not None:
        return menu
    return "Can't verify"