import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'
// import Welcome from '../components/Welcome'
import Users from '../components/user/Users'
import Rights from '../components/user/Rights'
import selfVedio from '../components/Video/selfVedio'
import simpleChat from '../components/Chat/simpleChat.vue'

Vue.use(VueRouter)

// 全局路由(隶属App.vue文件中的router-view)
const routes = [
    // 重定向
    {
        path: '/log',
        redirect: '/login'
    },
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/home',
        component: Home,
        // 重定向(访问的时候默认走下面这个路径)
        redirect: 'welcome',
        // 隶属于Home.vue中的router-view
        children: [{
                name: 'welcome',
                path: '/welcome',
                component: selfVedio
            },
            {
                name: 'users',
                path: '/goods1',
                component: Users
            },
            {
                name: 'roles',
                path: '/goods2',
                component: Rights
            },
            {
                name: 'simpleChat',
                path: '/rights1',
                component: simpleChat
            }
        ]
    }
]

// 创建router实例
const router = new VueRouter({
    routes
})

// 挂载路由导航守卫
router.beforeEach((to, from, next) => {
    // to 将要访问的路径
    // from 从哪里来
    // next 为一个函数, 表示放行, 默认为当前路由
    if (to.path === '/login') return next()
        // 获取token
    const tokenStr = window.sessionStorage.getItem('token')
        // 指定到/login页面
    if (!tokenStr) return next('/login')
    next()
})
export default router