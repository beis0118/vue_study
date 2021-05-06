import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
// 引入移动端适配
import 'lib-flexible'

// 导入全局样式表
import './assets/css/global.css'

// 配置网络请求
import axios from 'axios'

// 引入video.js
import 'video.js/dist/video-js.css'

// axios配置后台API接口根路径
axios.defaults.baseURL = 'http://192.168.1.9:8081/'
axios.interceptors.request.use(config => {
  // 处理config的参数
  config.headers.Authorization = window.sessionStorage.getItem('token')
  // 在方法最后必须return config
  return config
})
// 全局挂载axios, 直接用http即可访问
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
