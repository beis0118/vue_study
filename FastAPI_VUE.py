# FastAPI后台
from typing import Optional, List
from fastapi import FastAPI, Form, Header, status, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from fastapi.responses import JSONResponse

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
    "http://localhost:8080",
    "http://192.168.1.9",
    "http://47.117.66.221:8080",
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
    # 服务器不支持，它应该返回一个HTTP 406响应
    if username is None or password is None:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE)
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
async def menus(Authorization:Optional[str] = Header(None)):
    # 验证token
    print(Authorization)
    if Authorization is not None:
        return menu
    return "Can't verify"

# WebSocket实现持久连接(在线测试WebSocket:http://ws.douqq.com/)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 接收消息
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # 使用await + send_text发送消息
        await websocket.send_text(f"Message text was: {data}")

# 处理断开连接和多个客户端
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    # 建立管理员连接, 相当于每个用户都跟管理员建立连接, 然后管理员发送给连接到管理员的所有用户
    await manager.connect(websocket)
    try:
        while True:
            # 建立连接后并保持接受消息状态
            data = await websocket.receive_text()
            print(data)
            # 返回给发送用户
            await manager.send_personal_message(f"id:{client_id}", websocket)
            # 广播消息, 发送给所有用户
            await manager.broadcast(f"{client_id} 说: {data}")
    # 断开连接的时候, websocket.receive_text()会引发WebSocketDisconnect异常
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # 广播该信息
        await manager.broadcast(f"Client #{client_id} left the chat")

if __name__ == '__main__':
    uvicorn.run(app, host='192.168.1.9', port=8082)