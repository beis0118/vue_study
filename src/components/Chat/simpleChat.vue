<template>
  <div>
    <el-card> </el-card>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <h1 style="font-size:20px">WebSocket Chat</h1>
        <h2>Your ID: {{ clientid }}<span id="ws-id"></span></h2>
        <el-input v-model="text" placeholder="请输入内容"></el-input>
        <el-button @click="sendMessage()">发送</el-button>
        <ul id="messages"></ul>
      </div>
      <el-row>
        <el-col :span="12" :offset="0">
          我发送的消息:
          <div
            v-for="o in myMessage"
            :key="o"
            class="text item grid-content bg-purple"
          >
            {{ o }}
          </div>
        </el-col>
        <el-col :span="12" :offset="0">
          我接受到的消息:
          <div
            v-for="o in getMessage"
            :key="o"
            class="text item grid-content bg-purple"
          >
            {{ o }}
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "simpleChat",
  data() {
    return {
      // 设置用户标识
      clientid: 0,
      text: "",
      // socket程序
      ws: null,
      // 获取消息列表
      getMessage: [],
      myMessage: []
    };
  },
  methods: {
    sendMessage() {
      if (typeof WebSocket === "undefined") {
        console.log("您的浏览器不支持WebSocket");
      } else {
        console.log("您的浏览器支持WebSocket");
        console.log('{"contentText":"' + this.text + '"}');
        console.log(window.sessionStorage.getItem("token"));
        this.ws.send(
          window.sessionStorage.getItem("token") + " 说: " + this.text
        );
        this.myMessage.push("我说: " + this.text);
      }
    }
  },
  created() {
    console.log("1111111111111111111111111111111");
    this.clientid = window.sessionStorage.getItem("token");
    if (typeof WebSocket === "undefined") {
      console.log("您的浏览器不支持WebSocket");
    } else {
      console.log("您的浏览器支持WebSocket");
      // 实现化WebSocket对象，指定要连接的服务器地址与端口  建立连接
      // 等同于socket = new WebSocket("ws://localhost:8888/xxxx/im/25");
      // var socketUrl="${request.contextPath}/im/"+$("#userId").val();
      var socketUrl = "http://192.168.1.9:8082/ws/" + this.clientid;
      // 设置ws(websocket协议)
      socketUrl = socketUrl.replace("https", "ws").replace("http", "ws");
      console.log(socketUrl);
      // 清空socket
      if (this.ws != null) {
        this.ws.close();
        this.ws = null;
      }
      // 初始化ws对象
      this.ws = new WebSocket(socketUrl);
      // 打开事件
      this.ws.onopen = function() {
        console.log("websocket已打开");
        this.ws.send("这是来自客户端的消息" + location.href + new Date());
      };
      // 获得消息事件
      // 设置this指向, 指向vue
      var _this = this;
      this.ws.onmessage = function(msg) {
        console.log(msg.data); // 这里面的this 是全局的window
        // 发现消息进入
        // 更新用户id
        console.log(msg.data.substring(0, 3));
        if (msg.data.substring(0, 3) === "id:") {
          _this.clientid = msg.data.substring(3, msg.data.length);
          return;
        }
        var clientFrom = msg.data[0];
        console.log(clientFrom, _this.clientid.toString());
        if (clientFrom === _this.clientid.toString()) return;
        // 加入到消息列表
        console.log("不一样");
        _this.getMessage.push(msg.data.substring(4, msg.data.length));
      };
      // 关闭事件
      this.ws.onclose = function() {
        console.log("websocket已关闭");
      };
      // 发生了错误事件
      this.ws.onerror = function() {
        console.log("websocket发生了错误");
      };
    }
  }
};
</script>
<style scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
