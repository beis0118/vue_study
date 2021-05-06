import Vue from 'vue'
import { Button, Form, FormItem, Input, Message, Alert, Container, Header, Aside, Main, Menu, Submenu, MenuItemGroup, MenuItem, Footer } from 'element-ui'

// 全局注册
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Alert)
Vue.use(Container)
Vue.use(Header)
Vue.use(Aside)
Vue.use(Main)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItemGroup)
Vue.use(MenuItem)
Vue.use(Footer)
Vue.prototype.$message = Message
