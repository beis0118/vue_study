<template>
  <div class="login_container">
    <!--    创建一个登录盒子(容器)-->
    <div class="login_box">
      <!--      头像区域-->
      <div class="avatar_box">
        <img src="../assets/cxy.jpg">
      </div>
      <!--      登录表单区域-->
      <!--      ref 设置表单的实例名称, 以后都可以直接调用-->
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
        <!--        用户名-->
        <el-form-item label="" prop="username">
          <el-input v-model="loginForm.username" prefix-icon="el-icon-user-solid"></el-input>
        </el-form-item>
        <!--        密码-->
        <el-form-item label="" prop="password">
          <el-input v-model="loginForm.password" prefix-icon="el-icon-lock" type="password"></el-input>
        </el-form-item>
        <!--        按钮区域-->
        <el-form-item label="" class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="resetLoginForm">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      // 登录表单的数据绑定对象
      loginForm: {
        username: '',
        password: ''
      },
      //  表单验证规则
      loginFormRules: {
        // 验证用户名
        username: [{
          required: true,
          message: '请输入用户名',
          // 当文本框失去焦点时候,触发提示
          trigger: 'blur'
        }, {
          min: 3,
          max: 15,
          message: '长度在 3 到 15 个字符',
          trigger: 'blur'
        }],
        // 验证密码
        password: [{
          required: true,
          message: '请输入密码',
          // 当文本框失去焦点时候,触发提示
          trigger: 'blur'
        }
        ]
      }
    }
  },
  methods: {
    // 点击重置按钮,重置登录表单(使用Element表单提供的方法)
    resetLoginForm () {
      // this为当前组件实例对象, 重置的范围就是整个标签
      this.$refs.loginFormRef.resetFields()
    },
    // 设置弹窗提示
    login_sign (status) {
      if (status === '200') {
        this.$message({
          message: '登陆成功!',
          type: 'success'
        })
      } else {
        this.$message({
          message: '登陆失败!',
          type: 'error'
        })
      }
    },
    // 点击登录按钮, 先检验是否合法
    login () {
      // 使用validate()回调函数,valid为true即为合法
      this.$refs.loginFormRef.validate(async (valid) => {
        console.log(valid)
        if (!valid) return
        console.log(this.loginForm)
        // 保证获取值以后才进行下一步, 包含此方法最近的方法需要进行异步声明 async
        var loginForm = this.$qs.stringify(this.loginForm)
        const result = await this.$http.post('/user/login/', loginForm)
        console.log(result.data)
        // 检查有没有该用户
        if (result.data === 'No User!') return this.login_sign('0')
        // 根据状态值提示信息
        this.login_sign(result.data.meta.status)
        // 记录token
        // 把token保存在Storage中
        window.sessionStorage.setItem('token', result.data.data.token)
        // 通过编程式导航, 跳转到后台主页, 路由地址为 /home
        if (result.data.meta.status === '200') return this.$router.push('/home')
      })
    }
  }
}
</script>

<!--支持less语法格式, scope控制生效区间(只在当前组件中生效)-->
<style scoped>
.login_container {
  background-color: #2d4d6d;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: aliceblue;
  border-radius: 3px;
  position: absolute;
  /*距离左边50*/
  left: 50%;
  top: 50%;
  /*横轴移动50, 纵轴移动50*/
  transform: translate(-50%, -50%);
}

.login_box .avatar_box {
  height: 130px;
  width: 130px;
  border: 1px solid cornsilk;
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0 0 10px #ddd;
  position: absolute;
  left: 50%;
  /*50% 是根据宽度/高度进行计算的, 这里就是130/2 = 65*/
  transform: translate(-50%, -50%);
}

.login_box .avatar_box img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background-color: #dddddd;
  object-fit: cover;
}

.btns {
  display: flex;
  justify-content: flex-end;
}

.login_form {
  position: absolute;
  bottom: 0;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
}
</style>
