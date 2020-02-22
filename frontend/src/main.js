import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'whatwg-fetch' // fetch polyfill for IE10+
import api from './api'

Vue.config.productionTip = false

Vue.prototype.$api = api

Vue.prototype.$global = new Vue({
  data() {
    return {
      loggedIn: false,
      waiting: false
    }
  }
})

var vm = new Vue({
  router,
  render: function (h) { return h(App) }
})
api.setup(vm)
vm.$mount('#app')

router.afterEach((toRoute, fromRoute) => {
  vm.$global.waiting = false;
})