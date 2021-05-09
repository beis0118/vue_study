<template>
  <el-container class="home-container">
    <!--    头部区域-->
    <el-header>
      <div style="height: 100%">
        <img src="../assets/cxy.jpg" alt="">
        <span class="name">Ainio</span>
      </div>

      <el-button @click="logout" type="primary">退出登录</el-button>
    </el-header>
    <el-container>
      <!--      侧边栏-->
      <el-aside ref="aside" :width="this.col?'64px':'200px'">
        <!--        折叠/展开侧边栏-->
        <div class="toggle-button" @click="toggleCollapse">{{ dir_char }}</div>
        <!--        侧边栏菜单区域, 在这里设置相关属性,包括背景色,激活后文字颜色等-->
        <el-menu
          ref="menu"
          background-color="#3C3F41"
          text-color="#fff"
          active-text-color="#409EFF"
          :unique-opened="true"
          :collapse="col"
          :collapse-transition="col_tran"
          router
          :default-active="activePath"
        >
          <el-menu-item @click="saveNavState('welcome')" index="welcome">
            <template slot="title">
              <i class="el-icon-ship"></i>
              <span>首页</span>
            </template>
          </el-menu-item>
          <!--          一级菜单, index设置成不同值(必须是字符串,隐式转换), 因为element是通过index的值进行相应的, 这里 key就绑定了id的特殊值-->
          <el-submenu :index="item.id+''" v-for="item in menuList" :key="item.id">
            <!--            设置图标以及文本,这是个模板,用于生成每个导航栏-->
            <template slot="title">
              <i :class="iconsObj[item.id]"></i>
              <!--              显示各自的导航栏名称-->
              <span>{{ item.authName }}</span>
            </template>
            <!--            一级菜单下的二级菜单-->
            <el-submenu :index="subItem.id +''" v-for="subItem in item.children" :key="subItem.id">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span>{{ subItem.authName }}</span>
              </template>
              <!--              生成该导航栏下的选项-->
              <el-menu-item :index="btn.path +''" v-for="btn in subItem.children" :key="btn.id"
                            @click="saveNavState(btn.path)">
                <template slot="title">
                  <i class="el-icon-ship"></i>
                  <span>{{ btn.authName }}</span>
                </template>
                <!--                下面和上面的template效果一样-->
                <!--                <i class=></i>-->
                <!--                {{subItem.authName}}-->
              </el-menu-item>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!--      主体和结尾包裹在一个container内-->
      <el-container>
        <!--      主题区-->
        <el-main>
          <!--          所有在home组件内的子组件在这里进行跳转-->
          <router-view></router-view>
        </el-main>
        <!--        结尾区-->
        <el-footer style="background-color: #2B2B2B">
          <router-view name="roles"></router-view>
        </el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      // 定义菜单数组
      menuList: [],
      // 定义导航栏的图标对应
      iconsObj: {
        101: 'el-icon-s-goods',
        102: 'el-icon-shopping-cart-full',
        103: 'el-icon-user-solid',
        145: 'el-icon-s-data'
      },
      // 设置折叠展开是否启用动画效果
      col_tran: false,
      // 是否折叠
      col: false,
      dir_char: '>>>',
      // 激活的地址
      activePath: ''
    }
  },
  components: {},
  methods: {
    // 退出登录
    logout () {
      window.sessionStorage.removeItem('token')
      this.$router.push('/login')
    },
    // 从后台获取菜单列表
    async getMenuList () {
      // 解构赋值, 讲获取的数据中的data复制到res中
      const { data: res } = await this.$http.get('/info/menus/')
      if (res.meta.status !== 200) return this.$message.error(res.meta.status)
      // 赋值
      this.$data.menuList = res.data
      console.log(res, this.menuList)
    },
    // 折叠/启动展示转换
    toggleCollapse () {
      this.col = !this.col
      if (this.col) {
        this.dir_char = '<<<'
      } else {
        this.dir_char = '>>>'
      }
    },
    // 存储当前选定的模块, 刷新时自动定位
    saveNavState (activePath) {
      window.sessionStorage.setItem('activePath', activePath)
    }
  },
  // created后已经将整个vue基本建立好了,包括data以及methods, 这里可以用来进行数据初始化, 做一些挂载前的工作(此时模板还没有生成)
  created () {
    // 获取菜单
    this.getMenuList()
    // 设置activePath值(因为每次点选项实际上是跳转了一个链接, 所以后退/刷新 都是重新渲染,
    // 所以应该在data和method等数据都挂载好后,取activePath值放在这里面
    this.activePath = window.sessionStorage.getItem('activePath')
  }
}
</script>

<style scoped>
.home-container {
  height: 100%;
}

.name {
  position: absolute;
  transform: translate(0, 70%);
}

.el-header {
  background-color: #2B2B2B;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;
  font-size: 20px;
}

.el-header img {
  height: 100%;
  width: 100px;
  object-fit: cover;
  position: center;
  transform: translate(-10%, 0%);
}

.el-aside {
  background-color: #3C3F41;
}

.el-menu {
  border-right: 0;
}

.el-main {
  background-color: #666666;
}

.toggle-button {
  background-color: #4A5064;
  font-size: 10px;
  /*行高:是指文本行基线间的垂直距离. 和height效果不一样*/
  line-height: 24px;
  /*height: 24px;*/
  color: #ffffff;
  /*字符之间间隔*/
  letter-spacing: 0.2em;
  /*文本位置*/
  text-align: center;
  /*选中时显示小手*/
  cursor: pointer;
}
</style>
